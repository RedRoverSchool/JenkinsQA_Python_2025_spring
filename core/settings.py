from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


class BrowserConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="BROWSER_")

    NAME: str = "chrome"
    OPTIONS_CHROME: str = "--window-size=1920,1080"
    OPTIONS_EDGE: str = "--window-size=1920,1080"


class JenkinsConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="JENKINS_")

    HOST: str
    PORT: str
    USERNAME: str
    PASSWORD: str
    base_url: str = ""
    login_url: str = ""
    login_data: dict = {}
    crumb: str = ""
    current_username: str = ""

    def model_post_init(self, context: Any, /) -> None:
        self.base_url = f"http://{self.HOST}:{self.PORT}"
        self.login_url = f"{self.base_url}/j_spring_security_check"
        self.login_data = {"j_username": self.USERNAME, "j_password": self.PASSWORD}

    def update_crumb(self, crumb):
        self.crumb = crumb

    def get_url_with_credentials(self):
        return f"http://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}"


class Config(BaseSettings):
    browser: BrowserConfig = Field(default_factory=BrowserConfig)
    jenkins: JenkinsConfig = Field(default_factory=JenkinsConfig)

    @classmethod
    def load(cls) -> "Config":
        return cls()