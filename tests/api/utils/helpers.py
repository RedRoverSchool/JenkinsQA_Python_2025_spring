import uuid
import allure
import randomname
from datetime import datetime


@allure.step("Create unique name")
def create_unique_name(prefix="item") -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


@allure.step("Create unique name with words and time")
def create_unique_word_name(prefix="item") -> str:
    time = datetime.now().isoformat().replace(":", ".")[:18]
    return f"{prefix}-{randomname.get_name()}-{time}-{uuid.uuid4().hex[:8]}"
