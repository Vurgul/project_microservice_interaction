from pydantic import BaseSettings


class Settings(BaseSettings):
    IS_DEV_MODE: bool = False
