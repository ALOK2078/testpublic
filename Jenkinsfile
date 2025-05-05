pipeline {
    agent any

    stages {
        clearWs()      
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
            archiveArtifacts artifacts: '*.txt'
        }
        }
    }
}
