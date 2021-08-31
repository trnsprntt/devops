pipeline {
    agent { 
        docker { 
            image 'python:3.9.6-alpine'
        } 
    }
    environment {
        workdir = "python_app"
        docker = "trnsprntt/devops"
    }
    stages {
        stage('Prepare environment') {
            steps {
                checkout scm
                sh 'ls'
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
                        def app = docker.build('$docker')
                        docker.withRegistry("https://registry.hub.docker.com", "git") {
                            app.push("${env.BUILD_NUMBER}")
                        }
                    }
                }
            }
        }
    }
}
