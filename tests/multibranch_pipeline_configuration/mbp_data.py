from dataclasses import dataclass


@dataclass
class Data:
    PROJECT_NAME = "Multibranch Pipeline Test Project"
    TOGGLE_TOOLTIP_PREFS = (
        "tippy-10",
        "(No new builds within this Multibranch Pipeline will be executed until it is re-enabled)"
    )
    TOGGLE_ENABLED_TEXT = "Enabled"
    TOGGLE_DISABLED_TEXT = "Disabled"
    TOGGLE_ENABLED_ERROR_TEXT = "The toggle switch must be enabled!"