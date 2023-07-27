pipeline {
    agent any
    stages {
        stage ('SCM checkout') {
            steps {
               git branch: 'main', url: 'https://github.com/shrirangpendke/flask.git' 
            }
            
        }
        
        stage ('docker image build') {
            steps {
                sh '/usr/bin/docker image build -t shrirangpendke/flskapp .'
            }
        }
        
        stage ('docker login') {
            steps {
                sh 'echo dckr_pat_aREFZRKZcYR6WzyEC7sXWHRyFWY | /usr/bin/docker login -u shrirangpendke --password-stdin'
            }
        }
        
        stage ('docker image push') {
            steps {
                sh '/usr/bin/docker image push shrirangpendke/flskapp'
            }
        }
        
        stage ('get confirmation from user') {
            steps {
                input 'Do you want to deploy this app?'
            }
        }
        
        stage ('remove existing service') {
            steps {
                sh '/usr/bin/docker service rm service1'
            }
            
        }
        
        stage ('create a docker service ') {
            steps {
                sh '/usr/bin/docker service create --name service1 -p 4000:4000  shrirangpendke/flskapp'
            }
            }
        }
    }
