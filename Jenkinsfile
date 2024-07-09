@Library('my_library')
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps{
                script {
                    def config =[
                        url: 'https://github.com/Sourabh-VN/jenkinsjob.git'
                        branch: 'main'
                        credId: 'my_git_id'
                    ]

                }
            }
        }
    }
}