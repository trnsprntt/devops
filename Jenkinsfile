pipeline {
    agent { 
        docker { 
            image 'python:3.9.6-alpine'
            args '-u 0 -v $HOME/.cache:/root/.cache -v /var/run/docker.sock:/var/run/docker.sock -v /usr/local/bin/docker:/usr/local/bin/docker'
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
                sh 'pip install docker'
            }
        }

        stage('Test and lint') {
            steps {
                parallel (
                    'lint with flake8': { 
                        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                            sh 'flake8 $workdir'
                        }
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