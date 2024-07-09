@Library('my_library') _

pipeline {
    agent any
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
    }
}