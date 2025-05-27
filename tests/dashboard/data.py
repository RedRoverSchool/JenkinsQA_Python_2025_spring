class DashboardTable:
    HEADERS_MAP = {
        "Status of the last build": "S",
        "Weather report": "W",
        "Name": "Name",
        "Last Success": "Last Success",
        "Last Failure": "Last Failure",
        "Last Duration": "Last Duration",
        "Schedule": ""
    }

    PROJECT_NAMES = {
        "Freestyle project": "Star-Lord-The-Charming-Freestyle",
        "Pipeline": "Gamora_The_Fierce_Pipeline",
        "Multi-configuration project": "Drax_The_Destroyer_MultiConfig",
        "Folder": "Rocket The Clever Folder",
        "Multibranch Pipeline": "Groot_The_Mighty_Multibranch",
        "Organization Folder": "Nebula_The_Ruthless_OrgFolder",
    }

    DEFAULT_PROJECT_DATA_MAP = {
        "Freestyle project": {
            "status": "Not built",
            "weather": "100%",
            "name": PROJECT_NAMES["Freestyle project"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Pipeline": {
            "status": "Not built",
            "weather": "100%",
            "name": PROJECT_NAMES["Pipeline"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Multi-configuration project": {
            "status": "Not built",
            "weather": "100%",
            "name": PROJECT_NAMES["Multi-configuration project"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Folder": {
            "status": "Folder",
            "weather": "100%",
            "name": PROJECT_NAMES["Folder"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Multibranch Pipeline": {
            "status": "Multibranch Pipeline",
            "weather": "100%",
            "name": PROJECT_NAMES["Multibranch Pipeline"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Organization Folder": {
            "status": "Organization Folder",
            "weather": "100%",
            "name": PROJECT_NAMES["Organization Folder"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        }
    }
