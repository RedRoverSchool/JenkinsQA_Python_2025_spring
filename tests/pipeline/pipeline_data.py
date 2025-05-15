description_text = "Test description"
pipeline_project_name = "First Pipeline Project"
script = [
    "pipeline {\n",
    # "agent any\n",
    # "stages {\n",
    # "stage('Test') {\n",
    # "steps {\n",
    # "sh 'echo \"Step 1\"'\n",
    # "sh 'exit 0'",
    # "steps {\n",
    # "sh 'echo \"Step 1\"'\n",
    # "sh 'exit 0'",
    # "}\n",
    # "}\n",
    # "stage('Step 2 Message') {\n",
    # "steps {\n",
    # "sh 'echo \"Step 1\"'\n",
    # "sh 'exit 0'\n",
    # "}\n",
    # "}\n",
]

script1 = """
pipeline {
    agent any
    stages {
        stage('Step 1 Test') {
            steps {
                sh 'echo "Step 1"'
                sh 'exit 0'
            }
        }
        stage('Step 2 Message') {
            steps {
                sh 'echo "Step 2"'
                sh 'echo "Success!"'
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
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the Pipeline was previously failing but is now successful'
        }
    }
}
"""
