pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\SHASHANK\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"${env.PYTHON}\" -m pip install pytest"
            }
        }

        stage('Unit Tests') {
            steps {
                bat "mkdir test-results || exit 0"
                bat "\"${env.PYTHON}\" -m pytest --junitxml=test-results/results.xml"
            }
        }

        stage('Run Sensor Analysis') {
            steps {
                dir('src') {
                    bat "\"${env.PYTHON}\" analyze.py"
                }
            }
        }
    }

    post {
        always {
            junit 'test-results/results.xml'
        }
    }
}
