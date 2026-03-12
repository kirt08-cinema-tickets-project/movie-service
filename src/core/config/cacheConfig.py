from pydantic import BaseModel


class CacheConfig(BaseModel):
    ttl: int = 300