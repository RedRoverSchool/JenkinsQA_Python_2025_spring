from selenium.webdriver.common.by import By


class Freestyle:
    project_name = "New Freestyle Project"
    tooltip_disable = "Enable or disable the current project"
    warning_message = "This project is currently disabled"
    description_text = "Jenkins freestyle project is the general purpose job that will clone the projects from the Source Code Management (SCM) like Github, Gitlab, and Bit Bucket."
    tooltip_enable = (By.XPATH, '//span[@tooltip="Enable or disable the current project"]')
    environmet_options = ([
        ("Delete workspace before build starts", "cb18"),
        ("Use secret text(s) or file(s)", "cb19"),
        ("Add timestamps to the Console Output", "cb20"),
        ("Inspect build log for published build scans", "cb21"),
        ("Terminate a build if it's stuck", "cb22"),
        ("With Ant", "cb23")
    ])
    tooltip_scm = [
        ((By.XPATH, '//a[@tooltip="Help for feature: Git"]'), 'Help for feature: Git', 0),
        ((By.XPATH, '//a[@tooltip="Help for feature: Repositories"]'), 'Help for feature: Repositories', 1),
        ((By.XPATH, '//a[@tooltip="Help for feature: Repository URL"]'), 'Help for feature: Repository URL', 2),
        ((By.XPATH, '//a[@tooltip="Help for feature: Credentials"]'), 'Help for feature: Credentials', 3),
        ((By.XPATH, '//a[@tooltip="Help for feature: Name"]'), 'Help for feature: Name', 4),
        ((By.XPATH, '//a[@tooltip="Help for feature: Refspec"]'), 'Help for feature: Refspec', 4),
        ((By.XPATH, '//a[@tooltip="Help for feature: Branches to build"]'), 'Help for feature: Branches to build', 6),
        ((By.XPATH, '//a[@tooltip="Help for feature: Branch Specifier (blank for \'any\')"]'), 'Help for feature: Branch Specifier (blank for \'any\')', 6),
        ((By.XPATH, '//a[@tooltip="Help for feature: Repository browser"]'), 'Help for feature: Repository browser', 7)
    ]
    tooltip_environment = [
        ((By.XPATH, '//a[@tooltip="Help for feature: Use secret text(s) or file(s)"]'), 'Help for feature: Use secret text(s) or file(s)'),
        ((By.XPATH, '//a[@tooltip="Help for feature: With Ant"]'), 'Help for feature: With Ant')
    ]
    cron_schedule_every_minute = "*/1 * * * *"
    cron_schedule_every_two_minutes = "H/2 * * * *"
    timeout = {
        "*/1 * * * *": 60,
        "H/2 * * * *": 120
    }