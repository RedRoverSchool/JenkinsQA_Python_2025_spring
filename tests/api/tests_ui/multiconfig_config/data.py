project_name = "MyProject"

class GitHubConnection:
    INVALID_GITHUB_LINK = "https://github.com/RedRoverSchool/JenkinsQA_Python_2025_spring.git"+"1"
    FAILED_CONNECTION_ERROR_MESSAGE = f"Failed to connect to repository : Command \"git ls-remote -h -- {INVALID_GITHUB_LINK} HEAD\" returned status code 128:"

class Config:
    config_base_xml = """
    <matrix-project plugin="matrix-project@847.v88a_f90ff9f20">
        <keepDependencies>false</keepDependencies>
        <properties/>
        <scm class="hudson.scm.NullSCM"/>
        <canRoam>false</canRoam>
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

    config_with_environment_options_xml = """
    <matrix-project plugin="matrix-project@847.v88a_f90ff9f20">
      <description></description>
      <keepDependencies>false</keepDependencies>
      <properties/>
      <scm class="hudson.scm.NullSCM"/>
      <canRoam>true</canRoam>
      <disabled>false</disabled>
      <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
      <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
      <triggers/>
      <concurrentBuild>false</concurrentBuild>
      <axes/>
      <builders/>
      <publishers/>
      <buildWrappers>
        <hudson.plugins.ws__cleanup.PreBuildCleanup plugin="ws-cleanup@0.45"/>
        <org.jenkinsci.plugins.credentialsbinding.impl.SecretBuildWrapper plugin="credentials-binding@603.vd951319b_1c03"/>
        <hudson.plugins.timestamper.TimestamperBuildWrapper plugin="timestamper@1.26"/>
        <hudson.plugins.build__timeout.BuildTimeoutWrapper plugin="build-timeout@1.32">
          <strategy class="hudson.plugins.build_timeout.impl.AbsoluteTimeOutStrategy">
            <timeoutMinutes>60</timeoutMinutes>
          </strategy>
          <operationList>
            <hudson.plugins.build__timeout.operations.AbortOperation/>
          </operationList>
        </hudson.plugins.build__timeout.BuildTimeoutWrapper>
        <hudson.plugins.gradle.buildscan.BuildScanPublisher plugin="gradle@2.8"/>
      </buildWrappers>
      <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
        <runSequentially>false</runSequentially>
      </executionStrategy>
    </matrix-project>
    """

    config_delete_workspace_xml = """
    <matrix-project plugin="matrix-project@845.vffd7fa_f27555">
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <axes/>
    <builders/>
    <publishers/>
    <buildWrappers>
    <hudson.plugins.ws__cleanup.PreBuildCleanup plugin="ws-cleanup@0.48">
    <deleteDirs>false</deleteDirs>
    <cleanupParameter/>
    <externalDelete/>
    <disableDeferredWipeout>false</disableDeferredWipeout>
    </hudson.plugins.ws__cleanup.PreBuildCleanup>
    </buildWrappers>
    <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
    <runSequentially>false</runSequentially>
    </executionStrategy>
    </matrix-project>
    """

    config_test_use_secrets_xml = """
    <matrix-project plugin="matrix-project@845.vffd7fa_f27555">
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <axes/>
    <builders/>
    <publishers/>
    <buildWrappers>
    <org.jenkinsci.plugins.credentialsbinding.impl.SecretBuildWrapper plugin="credentials-binding@687.v619cb_15e923f">
    <bindings class="empty-list"/>
    </org.jenkinsci.plugins.credentialsbinding.impl.SecretBuildWrapper>
    </buildWrappers>
    <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
    <runSequentially>false</runSequentially>
    </executionStrategy>
    </matrix-project>
    """

    config_add_timestamps_xml = """
    <matrix-project plugin="matrix-project@845.vffd7fa_f27555">
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <axes/>
    <builders/>
    <publishers/>
    <buildWrappers>
    <hudson.plugins.timestamper.TimestamperBuildWrapper plugin="timestamper@1.28"/>
    </buildWrappers>
    <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
    <runSequentially>false</runSequentially>
    </executionStrategy>
    </matrix-project>
    """

    config_Inspect_build_log_xml = """
    <matrix-project plugin="matrix-project@845.vffd7fa_f27555">
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <axes/>
    <builders/>
    <publishers/>
    <buildWrappers>
    <hudson.plugins.gradle.BuildScanBuildWrapper plugin="gradle@2.14.1"/>
    </buildWrappers>
    <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
    <runSequentially>false</runSequentially>
    </executionStrategy>
    </matrix-project>
    """

    config_terminate_build_xml = """
    <matrix-project plugin="matrix-project@845.vffd7fa_f27555">
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <axes/>
    <builders/>
    <publishers/>
    <buildWrappers>
    <hudson.plugins.build__timeout.BuildTimeoutWrapper plugin="build-timeout@1.36">
    <strategy class="hudson.plugins.build_timeout.impl.AbsoluteTimeOutStrategy">
    <timeoutMinutes>3</timeoutMinutes>
    </strategy>
    <operationList/>
    </hudson.plugins.build__timeout.BuildTimeoutWrapper>
    </buildWrappers>
    <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
    <runSequentially>false</runSequentially>
    </executionStrategy>
    </matrix-project>
    """