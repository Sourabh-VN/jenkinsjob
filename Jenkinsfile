@Library('my_library') _

pipeline {
    agent any
    environment{
        DOCKER_IMAGE_NAME= 'python'
        DOCKER_IMAGE_TAG= '3.9.19-slim-bullseye'
        DOCKER_FILE_PATH='./Dockerfile'
    }
    stages {
        stage('Checkout') {
            steps {
                script{
                    def config = [
                        url: 'https://github.com/Sourabh-VN/jenkinsjob.git',
                        branch: 'main',
                        credId: 'gitthubtoken'
                    ]

                    gitCheckout(config)
                    }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    dockerBuildAndPush(DOCKER_IMAGE_NAME, DOCKER_IMAGE_TAG, DOCKER_FILE_PATH, 'dockerRegistry')


                }
            }
        }
    }
}