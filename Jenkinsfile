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
                    bat '"C:\\Users\\SHASHANK\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" analyze.py'
'
                }
            }
        }
    }
}
