pipeline {
  agent any
  stages {
    stage('Demo') {
      steps {
        sh 'echo "Hola desde Jenkins en Linux"'
        sh 'echo "Branch: $BRANCH_NAME"'
        sh 'ls -la'
      }
    }
  }
}
