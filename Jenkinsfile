pipeline {
  agent any

  environment {
    IMAGE_NAME = "prahlad8ac/quote-backend"
  }

  stages {
    stage('Clone Code') {
      steps {
        git 'https://github.com/Godfatherleop/Demo-Jenkins.git'
      }
    }

    stage('Test') {
      steps {
        sh '''
          cd backend
          pip install -r requirements.txt
          pytest test_app.py
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh '''
          docker build -t $IMAGE_NAME:latest backend/
        '''
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push $IMAGE_NAME:latest
          '''
        }
      }
    }

    stage('Deploy with Compose') {
      steps {
        sh '''
          docker-compose down || true
          docker-compose up -d --build
        '''
      }
    }
  }

  post {
    success {
      echo "✅ Pipeline completed. Image pushed to Docker Hub and app deployed."
    }
    failure {
      echo "❌ Build or test failed."
    }
  }
}
