from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    DATABASE_USERNAME : str = 'postgres'
    DATABASE_PASSWORD : str = '123123'
    DATABASE_HOST : str = 'localhost'
    DATABASE_PORT : str = '5432'
    DATABASE_NAME : str = 'mydb'

    DATABASE_URI : str = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 60 * 24 * 5  # 60 * 24 * 5 = 5 days
    SECRET_KEY : str = '5ZhRhFEwqLrIwGdc11bpzWPlP24Xwc6n'
    ALGORITHM : str = "HS512"
    
    model_config = {
        'case_sensitive': True
    }

@lru_cache
def get_Settings() -> Settings:
    return Settings()


settings = get_Settings()