pipeline {
    agent any
    stages {
        stage ('SCM checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shrirangpendke/flask.git'
            }
        }
        
        stage ('Docker image build') {
            steps {
                sh '/usr/bin/docker image build -t shrirangpendke/flsk1 .'
            }
        }
        
        stage ('Docker login') {
            steps {
                sh 'echo dckr_pat_aREFZRKZcYR6WzyEC7sXWHRyFWY | /usr/bin/docker login -u shrirangpendke --password-stdin'
            }
        }
        
        stage ('Docker image push') {
            steps {
                sh '/usr/bin/docker image push shrirangpendke/flsk1'
            }
        }
        
        stage ('remove existing service') {
            steps {
                sh '/usr/bin/docker service rm srv1'
            }
        }
        
        stage ('create a docker service') {
            steps {
                sh '/usr/bin/docker service create --name srv1 -p 4000:4000 --replicas 2 shrirangpendke/flsk1'
            }
        }
    }
}
