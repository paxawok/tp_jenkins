pipeline{
    options{timestamps() }

    agent none
    stages{
        stage('Check scm') {
            agent any
            steps{
                checkout scm
            }
        }
        
        stage('Build'){
            steps{
                echo "Building...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }

        stage('Test') {
            agent { docker { image 'alpine'
                    args '-u=\"root\"'
                    }
                  }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'pip install Flask --break-system-packages'
                sh 'pip install xmlrunner --break-system-packages'
                sh 'python3 app_test.py'
            } 
            post {
                always {
                    junit 'test-reports/results.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }     
        }
    }
}