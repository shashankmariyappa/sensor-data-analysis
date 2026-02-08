pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\SHASHANK\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pip install pytest'
            }
        }

        stage('Unit Tests') {
            steps {
                bat '"C:\\Users\\SHASHANK\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pytest --junitxml=test-results/results.xml'
            }
        }

        stage('Run Sensor Analysis') {
            steps {
                dir('src') {
                    bat '"C:\\Users\\SHASHANK\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" analyze.py'
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
