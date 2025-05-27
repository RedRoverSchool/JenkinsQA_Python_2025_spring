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


class Config:
    job_name = pipeline_project_name + " API"
    description = "Created by API"

    @classmethod
    def get_config_xml(cls, token: str = None) -> str:
        return f"""<?xml version='1.1' encoding='UTF-8'?>
    <flow-definition plugin="workflow-job">
      <description>{cls.description}</description>
      <keepDependencies>false</keepDependencies>
      <logRotator class="hudson.tasks.LogRotator">
        <daysToKeep>-1</daysToKeep>
        <numToKeep>50</numToKeep>
        <artifactDaysToKeep>-1</artifactDaysToKeep>
        <artifactNumToKeep>-1</artifactNumToKeep>
      </logRotator>
      <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps">
        <script>{Script.script}</script>
        <sandbox>true</sandbox>
      </definition>
      <authToken>{token}</authToken>
      <disabled>false</disabled>
    </flow-definition>"""
