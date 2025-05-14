description_text = "Test description"
pipeline_project_name = "First Pipeline Project"
script = """
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
}
"""