pipeline {
    agent any

    environment {
        PROJECT_DIR = '/home/ubuntu/Society-Backend-sample'
        VENV = '/home/ubuntu/Society-Backend-sample/venv/bin'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/harivijay8681-sudo/Society-Backend-sample.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    cd $PROJECT_DIR
                    $VENV/pip install -r requirements.txt
                '''
            }
        }

        stage('Database Migration') {
            steps {
                sh '''
                    cd $PROJECT_DIR
                    $VENV/python manage.py migrate
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                sh '''
                    cd $PROJECT_DIR
                    $VENV/python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Restart Gunicorn') {
            steps {
                sh '''
                    sudo systemctl restart gunicorn
                    sudo systemctl status gunicorn
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Deployment failed!'
        }
    }
}
