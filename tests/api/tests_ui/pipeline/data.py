import allure
from tests.api.utils.helpers import create_unique_name


class BuildsCounter:
    builds_history_limit_30 = 30
    builds_history_limit_31 = 31
    builds_history_limit_60 = 60
    builds_history_limit_61 = 61
    builds_history_page_limit = 30
    builds_to_keep_70 = 70
    amount_to_wait = 5


class Script:
    two_stages_with_post = """pipeline {
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

    script_default = two_stages_with_post


class Description:
    description = "Created via Jenkins API."
    triggers_default = " Triggers builds remotely."
    builds_to_keep_default = BuildsCounter.builds_to_keep_70

    @classmethod
    def get_pipeline_scripted_keep_70_builds_remotely_description(cls):
        return f"{cls.description} {cls.builds_to_keep_default} builds to keep.{cls.triggers_default}"


class Config:
    @classmethod
    def get_pipeline_scripted_keep_70_builds_remotely_xml(
            cls,
            description: str=Description.description,
            script: str=Script.script_default,
            token: str = None,
            log_rotator: int=BuildsCounter.builds_to_keep_70
    ) -> str:
        return f"""
            <flow-definition plugin="workflow-job">
                <description>{description}</description>
                <keepDependencies>false</keepDependencies>
                <logRotator class="hudson.tasks.LogRotator">
                    <daysToKeep>-1</daysToKeep>
                    <numToKeep>{log_rotator}</numToKeep>
                    <artifactDaysToKeep>-1</artifactDaysToKeep>
                    <artifactNumToKeep>-1</artifactNumToKeep>
                </logRotator>
                <definition class="org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition" plugin="workflow-cps">
                    <script>{script}</script>
                    <sandbox>true</sandbox>
                </definition>
                <triggers/>
                <authToken>{token}</authToken>
                <disabled>false</disabled>
            </flow-definition>
            """


class Data:
    @classmethod
    @allure.step("Create data for Pipeline project")
    def get_pipeline_scripted_keep_70_data(cls, token: str):
        item_name = create_unique_name(prefix="pipeline-api")
        description = Description.get_pipeline_scripted_keep_70_builds_remotely_description()
        log_rotator = BuildsCounter.builds_to_keep_70
        script = Script.two_stages_with_post
        config_xml = Config.get_pipeline_scripted_keep_70_builds_remotely_xml(description, script, token, log_rotator)

        data = (
            f"Pipeline name: {item_name}\n"
            f"Description: {description}\n"
            f"Log rotator: {log_rotator}\n"
        )
        allure.attach(data, name="Pipeline Data", attachment_type=allure.attachment_type.TEXT)

        return item_name, log_rotator, script, config_xml
