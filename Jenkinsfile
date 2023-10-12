pipeline {
  agent any
  parameters {
        string(name: 'url', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
        string(name: 'count', defaultValue: '', description: 'Enter some information about the person')
  }
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
        sh 'pip3 install requests'
      }
    }
    stage('API Testing') {
      steps {
        script{
            def url = params.url
            def count = params.count
            sh 'python3 api.py ${url} ${count}'
        }
      }
    }
  }
}