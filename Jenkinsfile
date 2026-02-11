pipeline {
  agent any
  stages {
    stage('Demo') {
      steps {
        sh 'echo "Hola Jenkins"'
        sh 'echo "Branch: $BRANCH_NAME"'
        sh 'ls -la'
      }
    }
  }
}
