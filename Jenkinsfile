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
        stage('Docker login') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'ilovemyPASSWORD', variable: 'DOCKER_PASSWORD')]) {
                    sh 'docker login -u paxawok -p $DOCKER_PASSWORD'
                }
            }
        }
        stage('Create Docker image') {
            agent any
            steps {
                sh "docker build -t paxawok/jenkins_l3:latest -f Dockerfile ."
            }
        }
        stage('Docker Push') {
            agent any
            steps {
                sh "docker push paxawok/jenkins_l3:latest"
            }
        }
    }
}