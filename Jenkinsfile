pipeline {
    agent {
        docker {
            image 'docker:stable'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        IMAGE_NAME = "my-python-api-test"
        REGISTRY = "vbappur422/my-python-api-test" 
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image for the application
                    sh 'docker build -t $REGISTRY:$BUILD_NUMBER .'
                }
            }
        }
        
        stage('Deploy Docker Image') {
            steps {
                script {
                    // Deploy the container 
                    sh 'docker run -d --name test-container -p 5000:5000 $REGISTRY:$BUILD_NUMBER'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Run the test using pytest in the container
                    sh 'docker exec test-container pytest test_api.py'
                }
            }
        }
        
        stage('Clean Up') {
            steps {
                script {
                    // Stop and remove the container after tests
                    sh 'docker stop test-container'
                    sh 'docker rm test-container'
                }
            }
        }
    }
}
