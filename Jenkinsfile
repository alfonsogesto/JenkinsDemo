pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Deploy') {
      steps {
        sh '''
          # main => v2, otras ramas => v1
          if [ "$BRANCH_NAME" = "main" ]; then
            kubectl set image deployment/notas-rolling notas=notas-api:v2
          else
            kubectl set image deployment/notas-rolling notas=notas-api:v1
          fi

          kubectl rollout status deployment/notas-rolling
        '''
      }
    }
  }
}
