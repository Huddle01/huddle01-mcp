from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
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