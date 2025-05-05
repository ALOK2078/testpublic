pipeline {
    agent any

    stages {
        cleanWs()      
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
