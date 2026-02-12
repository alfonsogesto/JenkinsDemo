pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install kubectl') {
      steps {
        sh '''
          curl -LO https://dl.k8s.io/release/v1.35.0/bin/linux/amd64/kubectl
          chmod +x kubectl
        '''
      }
    }

    stage('Deploy') {
      steps {
        sh '''
          if [ "$BRANCH_NAME" = "main" ]; then
            ./kubectl set image deployment/notas-rolling notas=notas-api:v2
          else
            ./kubectl set image deployment/notas-rolling notas=notas-api:v1
          fi

          ./kubectl rollout status deployment/notas-rolling
        '''
      }
    }
  }
}
