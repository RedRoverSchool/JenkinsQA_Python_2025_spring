project_name = "Organization Folder Project Name"
display_name = "Organization Folder Display Name API"
description = "Created By API"


class Config:
    @classmethod
    def get_organization_folder_xml(cls, display_name: str, description: str) -> str:
        return f"""
                <jenkins.branch.OrganizationFolder plugin="branch-api@2.1214.v3f652804588d">
                  <actions/>
                  <description>{description}</description>
                  <displayName>{display_name}</displayName>
                  <properties>
                    <jenkins.branch.OrganizationChildHealthMetricsProperty>
                      <templates>
                        <com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric plugin="cloudbees-folder@6.985.va_f1635030cc5">
                          <nonRecursive>false</nonRecursive>
                        </com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric>
                      </templates>
                    </jenkins.branch.OrganizationChildHealthMetricsProperty>
                    <jenkins.branch.OrganizationChildOrphanedItemsProperty>
                      <strategy class="jenkins.branch.OrganizationChildOrphanedItemsProperty$Inherit"/>
                    </jenkins.branch.OrganizationChildOrphanedItemsProperty>
                    <jenkins.branch.OrganizationChildTriggersProperty>
                      <templates>
                        <com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger plugin="cloudbees-folder@6.985.va_f1635030cc5">
                          <spec>H H/4 * * *</spec>
                          <interval>86400000</interval>
                        </com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger>
                      </templates>
                    </jenkins.branch.OrganizationChildTriggersProperty>
                    <jenkins.branch.NoTriggerOrganizationFolderProperty>
                      <branches>.*</branches>
                      <strategy>NONE</strategy>
                    </jenkins.branch.NoTriggerOrganizationFolderProperty>
                  </properties>
                  <folderViews class="jenkins.branch.OrganizationFolderViewHolder">
                    <owner reference="../.."/>
                  </folderViews>
                  <healthMetrics/>
                  <icon class="jenkins.branch.MetadataActionFolderIcon">
                    <owner class="jenkins.branch.OrganizationFolder" reference="../.."/>
                  </icon>
                  <orphanedItemStrategy class="com.cloudbees.hudson.plugins.folder.computed.DefaultOrphanedItemStrategy" plugin="cloudbees-folder@6.985.va_f1635030cc5">
                    <pruneDeadBranches>true</pruneDeadBranches>
                    <daysToKeep>2</daysToKeep>
                    <numToKeep>2</numToKeep>
                    <abortBuilds>false</abortBuilds>
                  </orphanedItemStrategy>
                  <triggers>
                    <com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger plugin="cloudbees-folder@6.985.va_f1635030cc5">
                      <spec>H H/4 * * *</spec>
                      <interval>43200000</interval>
                    </com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger>
                  </triggers>
                  <disabled>false</disabled>
                  <navigators/>
                  <projectFactories>
                    <org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProjectFactory plugin="workflow-multibranch@803.v08103b_87c280">
                      <scriptPath>Jenkinsfile</scriptPath>
                    </org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProjectFactory>
                  </projectFactories>
                  <buildStrategies/>
                  <strategy class="jenkins.branch.DefaultBranchPropertyStrategy">
                    <properties class="empty-list"/>
                  </strategy>
                </jenkins.branch.OrganizationFolder>
                """
