pipeline {
    agent { 
        docker { 
            image 'python:3.9.6-alpine'
        } 
    }
    environment {
        workdir = "app_python"
        docker = "trnsprntt/devops"
    }
    stages {
        def app
        stage('Prepare environment') {
            steps {
                checkout scm
                sh 'pip install -r $workdir/requirements.txt'
            }
        }

        stage('Test and lint') {
            steps {
                parallel (
                    'lint with flake8': { 
                        sh 'python flake8 $workdir'
                    },
                    'run tests': {
                        sh 'pytest $workdir/tests'
                    }
                )
            }
        }
        stage('Build and push') {
            steps {
                dir("${workdir}") {
                    script {
                        app = docker.build('$docker')
                        docker.withRegistry("https://registry.hub.docker.com", "git") {
                            app.push("${env.BUILD_NUMBER}")
                        }
                    }
                }
            }
        }
    }
}
