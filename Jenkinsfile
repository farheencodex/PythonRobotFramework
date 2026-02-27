// ============================================================
// Jenkinsfile - Boodmo Robot Framework CI/CD Pipeline
// Repo: farheencodex/PythonRobotFramework
// ============================================================
// Triggers: Push to main, Manual, Nightly (12 AM)
// Environment: Production
// ============================================================

pipeline {
    agent any

    // --------------------------------------------------------
    // Triggers: GitHub webhook, poll SCM, nightly schedule
    // --------------------------------------------------------
    triggers {
        githubPush()                     // On every push to main
        cron('H 0 * * *')               // Nightly at ~12 AM
    }

    // --------------------------------------------------------
    // Build parameters for manual runs
    // --------------------------------------------------------
    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['production', 'qa', 'staging'],
            description: 'Target environment for test execution'
        )
        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox', 'edge'],
            description: 'Browser to run tests on'
        )
        string(
            name: 'TAGS',
            defaultValue: '',
            description: 'Robot Framework tags to include (e.g., smoke, regression). Leave empty to run all.'
        )
    }

    // --------------------------------------------------------
    // Environment variables
    // --------------------------------------------------------
    environment {
        ENVIRONMENT = "${params.ENVIRONMENT ?: 'production'}"
        BROWSER     = "${params.BROWSER ?: 'chrome'}"
        ROBOT_TAGS  = "${params.TAGS ?: ''}"
        RF_PROJECT  = "BoodmoRobotFramework"
    }

    // --------------------------------------------------------
    // Pipeline options
    // --------------------------------------------------------
    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '20'))
        disableConcurrentBuilds()
    }

    stages {

        // ====================================================
        // Stage 1: Checkout
        // ====================================================
        stage('Checkout') {
            steps {
                checkout scm
                echo "Branch: ${env.BRANCH_NAME ?: 'main'}"
                echo "Environment: ${ENVIRONMENT}"
                echo "Browser: ${BROWSER}"
            }
        }

        // ====================================================
        // Stage 2: Setup Python Environment
        // ====================================================
        stage('Setup Environment') {
            steps {
                dir("${RF_PROJECT}") {
                    bat '''
                        python -m venv .venv
                        call .venv\\Scripts\\activate.bat
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        // ====================================================
        // Stage 3: Dry Run (Syntax Validation)
        // ====================================================
        stage('Dry Run') {
            steps {
                dir("${RF_PROJECT}") {
                    bat '''
                        call .venv\\Scripts\\activate.bat
                        robot --dryrun ^
                              --variablefile variables/env_%ENVIRONMENT%.py ^
                              --outputdir results/dryrun ^
                              tests/
                    '''
                }
            }
        }

        // ====================================================
        // Stage 4: Run UI Tests
        // ====================================================
        stage('UI Tests') {
            steps {
                dir("${RF_PROJECT}") {
                    script {
                        def tagOption = ROBOT_TAGS ? "--include ${ROBOT_TAGS}" : ''
                        bat """
                            call .venv\\Scripts\\activate.bat
                            robot --variablefile variables/env_${ENVIRONMENT}.py ^
                                  --variable BROWSER:${BROWSER} ^
                                  ${tagOption} ^
                                  --outputdir results/ui ^
                                  --loglevel DEBUG ^
                                  --timestampoutputs ^
                                  --name "UI_Tests_${ENVIRONMENT}" ^
                                  tests/ui/ || exit 0
                        """
                    }
                }
            }
        }

        // ====================================================
        // Stage 5: Run API Tests
        // ====================================================
        stage('API Tests') {
            steps {
                dir("${RF_PROJECT}") {
                    script {
                        def tagOption = ROBOT_TAGS ? "--include ${ROBOT_TAGS}" : ''
                        bat """
                            call .venv\\Scripts\\activate.bat
                            robot --variablefile variables/env_${ENVIRONMENT}.py ^
                                  ${tagOption} ^
                                  --outputdir results/api ^
                                  --loglevel DEBUG ^
                                  --timestampoutputs ^
                                  --name "API_Tests_${ENVIRONMENT}" ^
                                  tests/api/ || exit 0
                        """
                    }
                }
            }
        }

        // ====================================================
        // Stage 6: Merge Results
        // ====================================================
        stage('Merge Results') {
            steps {
                dir("${RF_PROJECT}") {
                    bat '''
                        call .venv\\Scripts\\activate.bat
                        rebot --outputdir results/merged ^
                              --name "Boodmo_Full_Suite" ^
                              --merge ^
                              results/ui/output*.xml ^
                              results/api/output*.xml || exit 0
                    '''
                }
            }
        }
    }

    // --------------------------------------------------------
    // Post-build actions
    // --------------------------------------------------------
    post {
        always {
            // Archive Robot Framework reports
            archiveArtifacts artifacts: "${RF_PROJECT}/results/**/*.*",
                             allowEmptyArchive: true

            // Publish Robot Framework results (requires Robot Framework plugin)
            script {
                try {
                    step([
                        $class: 'RobotPublisher',
                        outputPath: "${RF_PROJECT}/results/merged",
                        outputFileName: 'output.xml',
                        reportFileName: 'report.html',
                        logFileName: 'log.html',
                        passThreshold: 80.0,
                        unstableThreshold: 60.0,
                        otherFiles: '*.png'
                    ])
                } catch (Exception e) {
                    echo "Robot Framework plugin not installed. Skipping report publish."
                }
            }

            // Cleanup workspace virtual env
            dir("${RF_PROJECT}/.venv") {
                deleteDir()
            }
        }

        success {
            echo "BUILD SUCCESS: All tests completed on ${ENVIRONMENT}"
        }

        failure {
            echo "BUILD FAILED: Check Robot Framework reports for details"
        }

        unstable {
            echo "BUILD UNSTABLE: Some tests failed on ${ENVIRONMENT}"
        }
    }
}
