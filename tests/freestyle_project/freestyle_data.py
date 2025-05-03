class Freestyle:
    project_name = "New Freestyle Project"
    encoded_project_name = project_name.replace(" ", "%20")
    tooltip_disable = "Enable or disable the current project"
    warning_message = "This project is currently disabled"
    description_text = "Jenkins freestyle project is the general purpose job that will clone the projects from the Source Code Management (SCM) like Github, Gitlab, and Bit Bucket."
    tooltip_scm_link = (
        '//a[@tooltip="Help for feature: Git"]',
        '//a[@tooltip="Help for feature: Repositories"]',
        '//a[@tooltip="Help for feature: Repository URL"]',
        '//a[@tooltip="Help for feature: Credentials"]',
        '//a[@tooltip="Help for feature: Name"]',
        '//a[@tooltip="Help for feature: Refspec"]',
        '//a[@tooltip="Help for feature: Branches to build"]',
        "//a[@tooltip=\"Help for feature: Branch Specifier (blank for 'any')\"]",
        '//a[@tooltip="Help for feature: Repository browser"]',
    )
    tooltip_scm_link_wait = (
        '//a[@aria-describedby="tippy-34"]',
        '//a[@aria-describedby="tippy-35"]',
        '//a[@aria-describedby="tippy-36"]',
        '//a[@aria-describedby="tippy-37"]',
        '//a[@aria-describedby="tippy-39"]',
        '//a[@aria-describedby="tippy-40"]',
        '//a[@aria-describedby="tippy-42"]',
        '//a[@aria-describedby="tippy-43"]',
        '//a[@aria-describedby="tippy-45"]',
    )
    tooltip_scm_expected_text = (
        "Help for feature: Git",
        "Help for feature: Repositories",
        "Help for feature: Repository URL",
        "Help for feature: Credentials",
        "Help for feature: Name",
        "Help for feature: Refspec",
        "Help for feature: Branches to build",
        "Help for feature: Branch Specifier (blank for 'any')",
        "Help for feature: Repository browser",
    )
    tooltip_environment_link = (
        '//a[@tooltip="Help for feature: Use secret text(s) or file(s)"]',
        '//a[@tooltip="Help for feature: With Ant"]',
    )
    tooltip_environment_link_wait = (
        '//a[@aria-describedby="tippy-62"]',
        '//a[@aria-describedby="tippy-65"]',
    )
    tooltip_environment_expected_text = (
        "Help for feature: Use secret text(s) or file(s)",
        "Help for feature: With Ant",
    )
