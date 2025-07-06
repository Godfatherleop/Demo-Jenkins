pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/YOUR_USERNAME/quote-microservice.git'
      }
    }

    stage('Build & Run') {
      steps {
        sh '''
          docker-compose down || true
          docker-compose up -d --build --pull never
        '''
      }
    }
  }

  post {
    success {
      echo "🚀 Application is running at http://localhost:8080"
    }
    failure {
      echo "Build failed 💥 Check logs."
    }
  }
}
