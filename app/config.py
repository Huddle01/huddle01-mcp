from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # --- Run Time ---
    environment: str = Field(default="development", alias="ENVIRONMENT")
    log_level: str = Field(default="info", alias="LOG_LEVEL")
    host: str = Field(default="127.0.0.1", alias="HOST")
    port: int = Field(default=8080, alias="PORT")
    workers: int = Field(default=1, alias="WORKERS", ge=1)

    # --- Huddle01 ENV Vars ---
    huddle01_api_key: str = Field(description="API Key to Interact with Huddle01 Services", alias="Huddle01_API_KEY")
    huddle01_project_id: str = Field(description="Project Id to distinguish unique projects", alias="Huddle01_PROJECT_ID")

    model_config = SettingsConfigDict(
        env_file='.env',        
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'         
    )

settings = Settings() # type: ignore[call-arg]