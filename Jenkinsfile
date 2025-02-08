pipeline{
    agent any
    stages{
        stage('Checkout Code'){
            steps{
            git branch 'main', url:'https://github.com/happynaik/PytestPlaywright.git'
            }
        }
        stage('SetUp Python & Dependencies'){
            steps{
                 sh 'python3 -m venv venv'  // Create a virtual environment
                 sh 'source venv/bin/activate && pip install --upgrade pip'  // Upgrade pip
                 sh 'source venv/bin/activate && pip install pytest pytest-playwright'  // Install Pytest & Playwright
                 sh 'source venv/bin/activate && playwright install'  // Install Playwright browsers
            }
        }
        stage('Run Playwright Tests with Pytest') {
                    steps {
                        sh 'source venv/bin/activate && pytest tests/ --browser chromium --html=playwright-report/report.html --self-contained-html'
                    }
        }
        stage('Archive Playwright Reports') {
            steps {
                archiveArtifacts artifacts: 'playwright-report/**', fingerprint: true
            }
        }
    }
    post {
            success {
                echo '✅ Playwright tests passed successfully!'
            }
            failure {
                echo '❌ Playwright tests failed! Check the logs.'
            }
        }
}