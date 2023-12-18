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

        stage('Test'){
            agent{
                docker {
                    image 'alpine'
                    args '-u=root'
                }
            }
            steps {
                script {
                    sh 'apk add --update python3 py3-pip'
                    //sh 'pip install Flask xmlrunner'
                    sh 'python3 app_test.py'
                }
            }

            post{
                always{
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Tests failed."
                }
            }
        }
    }
}