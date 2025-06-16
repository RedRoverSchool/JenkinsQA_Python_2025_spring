description_text = "Test description"
pipeline_project_name = "First Pipeline Project"


class BuildTriggers:
    PROJECT_NAME = "Pipeline project"
    TITLE = "Triggers"
    DESCRIPTION = ("Set up automated actions that start your build based on specific events, "
                   "like code changes or scheduled times.")
    TRIGGER_LABELS = ["Build after other projects are built",
                      "Build periodically",
                      "GitHub hook trigger for GITScm polling",
                      "Poll SCM",
                      "Trigger builds remotely (e.g., from scripts)"]
    TRIGGER_CHECKBOXES_IDS = ["cb8", "cb9", "cb10", "cb11", "cb12"]
    TRIGGER_HELPER_TOOLTIPS = ["Help for feature: Build after other projects are built",
                               "Help for feature: Build periodically",
                               "Help for feature: GitHub hook trigger for GITScm polling",
                               "Help for feature: Poll SCM",
                               "Help for feature: Trigger builds remotely (e.g., from scripts)"]
    PIPELINE_PAGE_TITLE = f"{PROJECT_NAME} [Jenkins]"
    PIPELINE_PAGE_HEADER = f"{PROJECT_NAME}"
    PROJECTS_INPUT_LABEL = "Projects to watch"
    EMPTY_PROJECTS_VALUE = ""
    EMPTY_PROJECTS_ERROR = "No project specified"
    RADIO_BUTTON_LABELS = ["Trigger only if build is stable",
                           "Trigger even if the build is unstable",
                           "Trigger even if the build fails",
                           "Always trigger, even if the build is aborted"]
    RADIO_BUTTON_VALUE = ["SUCCESS", "UNSTABLE", "FAILURE", "ABORTED"]
