import allure

from tests.api.utils.helpers import create_unique_name


class CronTimer:
    every_minute: dict[str, str | int] = {
        "timer": "*/1 * * * *",
        "schedule": "1 min",
        "timeout": 60
    }
    every_two_minutes: dict[str, str | int] = {
        "timer": "H/2 * * * *",
        "schedule": "2 min",
        "timeout": 120
    }


class Config:
    @classmethod
    def get_freestyle_scheduled_xml(cls, description: str, timer: str) -> str:
        return f"""
            <project>
                <actions/>
                <description>{description}</description>
                <keepDependencies>false</keepDependencies>
                <properties/>
                <scm class="hudson.scm.NullSCM"/>
                <canRoam>true</canRoam>
                <disabled>false</disabled>
                <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
                <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
                <triggers>
                    <hudson.triggers.TimerTrigger>
                    <spec>{timer}</spec>
                    </hudson.triggers.TimerTrigger>
                </triggers>
                <concurrentBuild>false</concurrentBuild>
                <builders/>
                <publishers/>
                <buildWrappers/>
            </project>
            """

    @classmethod
    def get_empty_job_xml(cls) -> str:
        return """
            <project>
                <keepDependencies>false</keepDependencies>
                <properties/>
                <scm class="hudson.scm.NullSCM"/>
                <canRoam>false</canRoam>
                <disabled>false</disabled>
                <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
                <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
                <triggers/>
                <concurrentBuild>false</concurrentBuild>
                <builders/>
                <publishers/>
                <buildWrappers/>
            </project>
            """


class Description:
    description = "Created via Jenkins API."

    @classmethod
    def get_freestyle_scheduled_description(cls, schedule: str, timer: str):
        return f"{cls.description} Builds every {schedule} ({timer})."


class Data:
    @classmethod
    def get_freestyle_scheduled_every_minute_data(cls):
        item_name = create_unique_name(prefix="freestyle-api")
        schedule = CronTimer.every_minute["schedule"]
        timer = CronTimer.every_minute["timer"]
        timeout = CronTimer.every_minute["timeout"]
        description = Description.get_freestyle_scheduled_description(schedule, timer)
        config_xml = Config.get_freestyle_scheduled_xml(description, timer)

        with allure.step(f"Create data for Freestyle project \"{item_name}\" scheduled every {schedule}"):
            return item_name, timer, timeout, config_xml
