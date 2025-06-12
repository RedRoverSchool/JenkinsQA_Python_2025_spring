import uuid
import allure


@allure.step("Create an unique name")
def create_unique_name(prefix="item") -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"
