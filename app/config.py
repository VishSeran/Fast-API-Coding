from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseSettings (BaseSettings):
    
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    
    # default variable in base setting class
    model_config = SettingsConfigDict(
        env_file= "./.env",
        env_ignore_empty=True,
        extra="ignore",
    )
    
settings = DatabaseSettings()

print(settings.POSTGRES_DB)
print(settings.POSTGRES_USERNAME)
print(settings.POSTGRES_PASSWORD)
print(settings.POSTGRES_PORT)
    