from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


class BrowserConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="BROWSER_")

    NAME: str = "chrome"
    OPTIONS_CHROME: str = "--window-size=1920,1080; --incognito"
    OPTIONS_EDGE: str = "--window-size=1920,1080; --incognito"


class Config(BaseSettings):
    browser: BrowserConfig = Field(default_factory=BrowserConfig)

    @classmethod
    def load(cls) -> "Config":
        return cls()