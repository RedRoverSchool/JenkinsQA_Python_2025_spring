description_text = "Test description"
pipeline_project_name = "First Pipeline Project"

class Script:
    script = """pipeline {
        agent any
        stages {
            stage('Stage 1 Test') {
                steps {
                    script {
                        if (isUnix()) {
                            sh 'echo Step 1'
                            sh 'exit 0'
                        } else {
                            bat 'echo Step 1'
                            bat 'exit 0'
                        }
                    }
                }
            }
            stage('Stage 2 Message') {
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

class BuildCounter:
    build_history_limit_30 = 30
    build_history_limit_31 = 31
    build_history_limit_60 = 60
    build_history_limit_61 = 61
    build_history_page_limit = 30
    amount_to_wait = 5