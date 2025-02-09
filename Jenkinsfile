pipeline {
    agent any

    environment {
        REPORT_DIR = "playwright-report"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/happynaik/PytestPlaywright.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pytest-playwright .'
            }
        }

        stage('Run Playwright Tests in Docker') {
            steps {
                sh 'docker run --rm -v $(pwd)/playwright-report:/app/playwright-report pytest-playwright'
            }
        }

        stage('Archive Playwright Reports') {
            steps {
                archiveArtifacts artifacts: 'playwright-report/**', fingerprint: true
                publishHTML([
                    reportName: 'Playwright Test Report',
                    reportDir: REPORT_DIR,
                    reportFiles: 'report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ])
            }
        }
    }

    post {
        success {
            echo '✅ Playwright tests passed successfully!'
        }
        failure {
            echo '❌ Playwright tests failed! Check the logs and reports.'
        }
    }
}
