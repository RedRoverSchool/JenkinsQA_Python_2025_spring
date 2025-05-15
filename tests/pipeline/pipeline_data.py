description_text = "Test description"
pipeline_project_name = "First Pipeline Project"
# script = """
# pipeline {
# agent any
# stages {
# stage('Step 1 Test') {
# steps {
# sh 'echo "Step 1"'
# sh 'exit 0'
# }
# }
# stage('Step 2 Message') {
# steps {
# sh 'echo "Step 2"'
# sh 'echo "Success!"'
# }
# }
# }
# }
# """

# script = """ pipeline {
#     agent any
#     stages {
#         stage('Step 1 Test') {
#             steps {
#                 sh 'echo "Success!"; exit 0'
#             }
#         }
#     }
#     post {
#         always {
#             echo 'This will always run'
#         }
#         success {
#             echo 'This will run only if successful'
#         }
#         failure {
#             echo 'This will run only if failed'
#         }
#         unstable {
#             echo 'This will run only if the run was marked as unstable'
#         }
#         changed {
#             echo 'This will run only if the state of the Pipeline has changed'
#             echo 'For example, if the Pipeline was previously failing but is now successful'
#         }
#     }
# }
# """

script = """pipeline {
    agent any
    stages {
        stage('Step 1 Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo Step 1'
                    } else {
                        bat 'echo Step 1'
                    }
                }
            }
        }
        stage('Step 2 Message') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo Step 2'
                        sh 'echo Success!'
                    } else {
                        bat 'echo Step 2'
                        bat 'echo Success!'
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if marked as unstable'
        }
        changed {
            echo 'This will run only if changed'
        }
    }
}
"""