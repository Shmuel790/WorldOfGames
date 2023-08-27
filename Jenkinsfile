
pipeline {
    agent any

    stages {
        stage ('#1 Git checkout') {
            steps {
                git branch: 'master',
                credentialsId: 'shmuel',
                url: 'https://github.com/Shmuel790/WorldOfGames.git'
                }
        }
        stage ('#2 Build Dockerfile') {
            steps {
                bat 'docker build -t Shmuel790/worldofgames .'

                }
        }
        stage ('#3 run Dockerfile') {
            steps {
                bat 'docker run --name games-container -d -t -p 8777:80 Shmuel790/worldofgames'

                }
        }
        stage ('#4 run tests') {
            steps {
                bat 'docker exec -t -d games-container python /mainScores.py'
                bat 'docker exec -t -d games-container python /tests/e2e.py'
                }
        }
        stage ('#5 stop and delete containers') {
            steps {
                bat 'docker stop games-container'
                bat 'docker push Shmuel790/worldofgames'
                bat 'docker rm games-container'
                }
        }



    }
}