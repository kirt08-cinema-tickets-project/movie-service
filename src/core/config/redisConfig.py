from pydantic import BaseModel, SecretStr


class RedisConfig(BaseModel):
    host: str = ""
    port: int = 0
    password: SecretStr = ""
    db: int = 0

    @property
    def url(self):
        return f"redis://:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db}"

    