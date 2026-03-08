import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.config.grpcConfig import GrpcConfig
from src.core.config.loggerConfig import LoggerConfig
from src.core.config.databaseConfig import DatabaseConfig

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
env_name = os.getenv("ENVIRONMENT", "development").lower()
env_file = BASE_DIR / f".env.{env_name}.local"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive = False,
        env_file = env_file,
        env_prefix = "MOVIE_SERVICE__",
        env_nested_delimiter="__"
    )
    logger: LoggerConfig = LoggerConfig()
    grpc: GrpcConfig = GrpcConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()