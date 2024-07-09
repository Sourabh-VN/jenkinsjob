@Library('my_library') _

pipeline {
    agent any
    environment{
        DOCKER_IMAGE_NAME= 'sourabhvn/project'
        DOCKER_IMAGE_TAG= 'latest'
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
                    docker.withRegistry('','dockerRegistry'){
                    dockerBuildAndPush(DOCKER_IMAGE_NAME, DOCKER_IMAGE_TAG, DOCKER_FILE_PATH, 'dockerRegistry')


                   }
                }
            }
        }
    }
}