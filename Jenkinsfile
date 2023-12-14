pipeline {
    options {
        timestamps()
    }

    agent none

    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Build'){
            steps{
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u=root'
                }
            }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'pip install unittest2==1.1.0'
                // sh 'pip install --upgrade pip wheel setuptools requests'
                sh 'pip install xmlrunner'
                sh 'python3 test.py'
            }
            
            post {
                always {
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
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image
                    def DOCKER_IMAGE = 'anne738/my-repo'
                    sh "docker build -t ${DOCKER_IMAGE} -f Dockerfile ."

                    withCredentials([usernamePassword(credentialsId: 'LandPDOCKER', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                    }
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }
    }
}