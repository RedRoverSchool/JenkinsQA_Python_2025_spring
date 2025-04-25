from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


# 1. Navigate to the Freestyle project > Configuration (using fixture)
def test_trigger_section(freestyle):
# 2. Verify the "Build Triggers"(Triggers) section is displayed
    title_triggers = freestyle.find_element(By.ID, 'triggers')
    assert title_triggers.is_displayed

def test_enable_trigger_opt(freestyle):
    my_list = []
    bld_remote = 'pseudoRemoteTrigger'
    my_list.append(bld_remote) 
    bld_after_bld = 'jenkins-triggers-ReverseBuildTrigger'
    my_list.append(bld_after_bld) 
    bld_period = 'hudson-triggers-TimerTrigger'
    my_list.append(bld_period) 
    github_hook = 'com-cloudbees-jenkins-GitHubPushTrigger'
    my_list.append(github_hook) 
    poll_scm = 'hudson-triggers-SCMTrigger'
    my_list.append(poll_scm) 

# 3. Select/enable the checkbox for the following options
    for i in my_list:
        result = freestyle.find_element(By.NAME, i)
        result.send_keys(Keys.SPACE)
        assert result.is_enabled(), f"Element {i} should be enabled but it doesn't"

# 4. Select/disable the checkbox for the options mentioned in step 4
    for i in my_list:
        result = freestyle.find_element(By.NAME, i)
        result.send_keys(Keys.SPACE)
        assert result.is_selected() == False, f"Element {i} should be disbale but it doesn't"



