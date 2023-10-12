pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('API Testing') {
      steps {
        sh 'python3 api.py'
      }
    }
  }
}