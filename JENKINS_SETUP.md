# Jenkins Setup Guide - Boodmo Robot Framework

## 1. Install Jenkins (Windows)

### Download & Install
1. Go to **https://www.jenkins.io/download/**
2. Download **Windows** installer (LTS recommended)
3. Run the `.msi` installer
4. During install, it will ask for a port — default is **8080**
5. Jenkins will install as a **Windows service** and start automatically

### First-Time Setup
1. Open browser → **http://localhost:8080**
2. Get the initial admin password:
   ```
   type "C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword"
   ```
3. Paste the password and click **Continue**
4. Choose **Install suggested plugins** (wait for install)
5. Create your admin user account
6. Set Jenkins URL: `http://localhost:8080/`
7. Click **Start using Jenkins**

---

## 2. Install Required Plugins

Go to **Manage Jenkins** → **Plugins** → **Available plugins**, search and install:

| Plugin | Purpose |
|--------|---------|
| **Git** | Clone repo from GitHub |
| **GitHub Integration** | Webhook triggers on push |
| **Pipeline** | Run Jenkinsfile pipelines |
| **Robot Framework** | Parse & publish RF test results |
| **Timestamper** | Add timestamps to console output |

After installing, **restart Jenkins** when prompted.

---

## 3. Configure Tools

### Python
Go to **Manage Jenkins** → **Tools** (or Global Tool Configuration):
- Ensure `python` is in system PATH
- Verify: Open cmd → `python --version` should show 3.11+

### Git
- Jenkins auto-detects Git if it's in PATH
- Verify: `git --version` in cmd

### Chrome / ChromeDriver
- Chrome must be installed on the Jenkins machine
- `webdriver-manager` in requirements.txt handles ChromeDriver automatically

---

## 4. Add GitHub Credentials (SSH)

1. **Manage Jenkins** → **Credentials** → **System** → **Global credentials**
2. Click **Add Credentials**
3. Kind: **SSH Username with private key**
4. ID: `github-farheencodex`
5. Username: `git`
6. Private Key → **Enter directly** → paste contents of:
   ```
   type %USERPROFILE%\.ssh\id_ed25519_farheencodex
   ```
7. Passphrase: *(leave empty)*
8. Click **Create**

---

## 5. Create the Pipeline Job

1. From Jenkins Dashboard → **New Item**
2. Name: `Boodmo-Robot-Framework`
3. Type: **Pipeline**
4. Click **OK**

### Configure the Job

#### General
- ✅ **This project is parameterized** (already defined in Jenkinsfile)
- ✅ **GitHub project**: `https://github.com/farheencodex/PythonRobotFramework/`

#### Build Triggers
- ✅ **GitHub hook trigger for GITScm polling** (push trigger)
- ✅ **Build periodically**: `H 0 * * *` (nightly at ~12 AM)

#### Pipeline
- Definition: **Pipeline script from SCM**
- SCM: **Git**
- Repository URL: `git@github.com:farheencodex/PythonRobotFramework.git`
- Credentials: Select `github-farheencodex` (created in step 4)
- Branch: `*/main`
- Script Path: `Jenkinsfile`

Click **Save**.

---

## 6. Setup GitHub Webhook (Auto-trigger on Push)

1. Go to **github.com/farheencodex/PythonRobotFramework**
2. **Settings** → **Webhooks** → **Add webhook**
3. Payload URL: `http://<your-jenkins-url>:8080/github-webhook/`
   - For local, you need a public URL (use **ngrok** — see below)
4. Content type: `application/json`
5. Events: **Just the push event**
6. ✅ Active
7. Click **Add webhook**

### Using ngrok for Local Jenkins
If Jenkins runs locally and isn't publicly accessible:
```bash
# Install ngrok: https://ngrok.com/download
ngrok http 8080
```
Use the generated `https://xxxx.ngrok.io` URL as webhook payload URL:
```
https://xxxx.ngrok.io/github-webhook/
```

---

## 7. Run the Job

### Manual Run
1. Go to `Boodmo-Robot-Framework` job
2. Click **Build with Parameters**
3. Select Environment: `production` / `qa` / `staging`
4. Select Browser: `chrome` / `firefox` / `edge`
5. Tags: `smoke`, `regression`, or leave empty for all
6. Click **Build**

### Auto Triggers
- **Push**: Automatically triggers on any push to `main`
- **Nightly**: Runs at ~12 AM every night

---

## 8. View Results

After a build completes:
- **Console Output**: Full execution log
- **Robot Results**: Click on build → **Robot Results** tab (if plugin installed)
- **Artifacts**: Download full Robot Framework HTML reports from **Build Artifacts**

### Reports Location in Build
```
BoodmoRobotFramework/results/merged/report.html  → Combined report
BoodmoRobotFramework/results/merged/log.html     → Detailed log
BoodmoRobotFramework/results/ui/                  → UI test results
BoodmoRobotFramework/results/api/                 → API test results
```

---

## Quick Reference - Pipeline Stages

| Stage | Description |
|-------|-------------|
| **Checkout** | Clones repo from GitHub |
| **Setup Environment** | Creates venv, installs dependencies |
| **Dry Run** | Validates Robot syntax (no browser) |
| **UI Tests** | Runs UI test suites against boodmo.com |
| **API Tests** | Runs API test suites |
| **Merge Results** | Combines UI + API results into one report |
