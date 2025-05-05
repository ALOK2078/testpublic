pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh '''
                #!/bin/bash
                # This is a simple shell script\
                ls -l
                echo 'alok mishra'
                '''
            
            }
        }
    }
    post {
        success {
            echo 'It's time to Archive the artifacts'
            archiveArtifaacts artifacts: '*.txt'
        }
        always {
            echo 'This will always run'
            cleanWs()
        }
    }
}
