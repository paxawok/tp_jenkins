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
                    junit allowEmptyResults: true, testResults: 'test-reports/*.xml', skipPublishingChecks: true, skipMarkingBuildUnstable: true

                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            }     
        }
        stage('Build and Push Docker Image') {
            agent any
            steps {
                script {
                    // Build Docker image
                    def DOCKER_IMAGE = 'paxawok/jenkins_l3'
                    sh "docker build -t ${DOCKER_IMAGE} -f Dockerfile ."

                    withCredentials([usernamePassword(credentialsId: 'ilovemyPASSWORD', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    }
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }
}