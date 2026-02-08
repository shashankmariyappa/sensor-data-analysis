pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Sensor Analysis') {
            steps {
                dir('src') {
                    bat 'python analyze.py'
                }
            }
        }
    }
}
