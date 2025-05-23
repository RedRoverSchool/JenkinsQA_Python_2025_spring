from tests.new_item.data import new_pipeline_name


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

    DEFAULT_PROJECT_DATA = {
        "status": "Not built",
        "weather": "100%",
        "name": new_pipeline_name,
        "last_success": "N/A",
        "last_failure": "N/A",
        "duration": "N/A",
        "schedule": ""
    }
