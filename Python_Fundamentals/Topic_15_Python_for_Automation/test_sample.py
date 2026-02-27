"""
test_sample.py — Sample pytest test file
==========================================
Demonstrates pytest test structure, assertions, fixtures, and markers.

Run with:
    pytest test_sample.py -v
    pytest test_sample.py -v -m smoke
    pytest test_sample.py -v --tb=short

NOTE: This file uses ONLY pytest (no Selenium).
      It demonstrates testing concepts with simple Python assertions.
"""

import pytest


# ============================================================
# FIXTURES — Setup/Teardown for tests
# ============================================================

@pytest.fixture
def sample_user():
    """Fixture: Provides a sample user dictionary."""
    # SETUP — runs before the test
    user = {
        "username": "testuser@boodmo.com",
        "password": "Test@123",
        "role": "customer",
        "is_active": True,
    }
    print(f"\n  [SETUP] Created user: {user['username']}")
    
    yield user  # Pass the user to the test
    
    # TEARDOWN — runs after the test (even if test fails)
    print(f"  [TEARDOWN] Cleaned up user: {user['username']}")


@pytest.fixture
def cart():
    """Fixture: Provides an empty shopping cart."""
    cart_data = {"items": [], "total": 0.0}
    print(f"\n  [SETUP] Cart initialized")
    yield cart_data
    print(f"  [TEARDOWN] Cart cleared")


# ============================================================
# BASIC TESTS — Assertions
# ============================================================

class TestBasicAssertions:
    """Group: Basic assertion tests."""
    
    def test_addition(self):
        """Test basic addition."""
        assert 2 + 2 == 4
    
    def test_string_contains(self):
        """Test string containment."""
        url = "https://boodmo.com/search?q=brake+pad"
        assert "boodmo.com" in url
        assert "search" in url
    
    def test_list_length(self):
        """Test list length."""
        browsers = ["Chrome", "Firefox", "Edge"]
        assert len(browsers) == 3
    
    def test_dict_key_exists(self):
        """Test dictionary key existence."""
        config = {"browser": "Chrome", "timeout": 30}
        assert "browser" in config
        assert config["timeout"] == 30


# ============================================================
# TESTS WITH FIXTURES
# ============================================================

class TestUserLogin:
    """Group: User login tests using fixtures."""
    
    @pytest.mark.smoke
    def test_user_has_username(self, sample_user):
        """Test that user has a valid username."""
        assert sample_user["username"] is not None
        assert "@" in sample_user["username"]
    
    @pytest.mark.smoke
    def test_user_is_active(self, sample_user):
        """Test that user is active."""
        assert sample_user["is_active"] is True
    
    def test_user_has_password(self, sample_user):
        """Test that user has a password."""
        assert len(sample_user["password"]) >= 6
    
    def test_user_role(self, sample_user):
        """Test user role is valid."""
        valid_roles = ["admin", "customer", "guest"]
        assert sample_user["role"] in valid_roles


# ============================================================
# TESTS WITH CART FIXTURE
# ============================================================

class TestShoppingCart:
    """Group: Shopping cart tests."""
    
    def test_cart_starts_empty(self, cart):
        """Test that cart starts with no items."""
        assert len(cart["items"]) == 0
        assert cart["total"] == 0.0
    
    def test_add_item_to_cart(self, cart):
        """Test adding an item to cart."""
        item = {"name": "Brake Pad", "price": 1500.0, "qty": 2}
        cart["items"].append(item)
        cart["total"] += item["price"] * item["qty"]
        
        assert len(cart["items"]) == 1
        assert cart["total"] == 3000.0
    
    def test_add_multiple_items(self, cart):
        """Test adding multiple items to cart."""
        items = [
            {"name": "Oil Filter", "price": 500.0, "qty": 1},
            {"name": "Air Filter", "price": 800.0, "qty": 1},
        ]
        for item in items:
            cart["items"].append(item)
            cart["total"] += item["price"] * item["qty"]
        
        assert len(cart["items"]) == 2
        assert cart["total"] == 1300.0


# ============================================================
# PARAMETRIZED TESTS — Run same test with different data
# ============================================================

class TestParametrized:
    """Group: Demonstrating parametrized tests."""
    
    @pytest.mark.parametrize("browser", ["Chrome", "Firefox", "Edge"])
    def test_supported_browsers(self, browser):
        """Test runs once for each browser."""
        supported = ["Chrome", "Firefox", "Edge", "Safari"]
        assert browser in supported
    
    @pytest.mark.parametrize("email,is_valid", [
        ("user@boodmo.com", True),
        ("admin@test.com", True),
        ("invalid-email", False),
        ("@no-username.com", False),
        ("user@", False),
    ])
    def test_email_validation(self, email, is_valid):
        """Test email validation with multiple inputs."""
        # Simple email validation (checks for @ and .)
        result = "@" in email and "." in email.split("@")[-1] and email.index("@") > 0
        assert result == is_valid


# ============================================================
# MARKERS — Categorize tests
# ============================================================

@pytest.mark.smoke
def test_homepage_loads():
    """Smoke test: Homepage should be accessible."""
    status_code = 200  # Simulated
    assert status_code == 200


@pytest.mark.regression
def test_search_returns_results():
    """Regression test: Search should return results."""
    results = ["Brake Pad", "Brake Disc"]  # Simulated
    assert len(results) > 0


@pytest.mark.skip(reason="Feature not implemented yet")
def test_wishlist():
    """Skipped test: Wishlist feature not ready."""
    assert True


@pytest.mark.xfail(reason="Known bug: BUG-1234")
def test_coupon_code():
    """Expected failure: Known coupon code bug."""
    discount = 0  # Bug: discount not applied
    assert discount > 0  # Will fail but marked as expected
