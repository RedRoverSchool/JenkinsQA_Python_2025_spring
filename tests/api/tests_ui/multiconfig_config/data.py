project_name = "MyProject"

class GitHubConnection:
    INVALID_GITHUB_LINK = "https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring.git"+"1"
    FAILED_CONNECTION_ERROR_MESSAGE = f"Failed to connect to repository : Command \"git.exe ls-remote -h -- {INVALID_GITHUB_LINK} HEAD\" returned status code 128:"

class Config:
    @classmethod
    def get_multiconfig_github_link_xml(cls, github_link: str, branch_name: str = "*/main") -> str:
        return f"""
            <matrix-project plugin="matrix-project@847.v88a_f90ff9f20">
                <actions/>
                <description/>
                <keepDependencies>false</keepDependencies>
                <properties/>
                <scm class="hudson.plugins.git.GitSCM" plugin="git@5.7.0">
                    <configVersion>2</configVersion>
                    <userRemoteConfigs>
                        <hudson.plugins.git.UserRemoteConfig>
                            <url>{github_link}</url>     
                        </hudson.plugins.git.UserRemoteConfig>
                    </userRemoteConfigs>
                    <branches>
                        <hudson.plugins.git.BranchSpec>
                            <name>{branch_name}</name>
                        </hudson.plugins.git.BranchSpec>
                    </branches>
                    <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
                    <submoduleCfg class="empty-list"/>
                    <extensions/>
                </scm>
                <canRoam>true</canRoam>
                <disabled>false</disabled>
                <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
                <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
                <triggers/>
                <concurrentBuild>false</concurrentBuild>
                <axes/>
                <builders/>
                <publishers/>
                <buildWrappers/>
                <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
                    <runSequentially>false</runSequentially>
                </executionStrategy>
            </matrix-project>
            """