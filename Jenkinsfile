pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh '''
                    ls -l
                    echo 'alok mishra'
                '''
            
            }
        }
    }
    post {
        success {
            echo 'time to Archive the artifacts'
            archiveArtifaacts artifacts: '*.txt'
        }
        always {
            echo 'This will always run'
            cleanWs()
        }
    }
}
