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
