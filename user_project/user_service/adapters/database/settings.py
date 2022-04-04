from pydantic import BaseSettings
from dotenv import dotenv_values
config = dotenv_values(".env")


class Settings(BaseSettings):
    print(config.get('DB_USER'))
    DB_URL = f"mysql://{config.get('DB_USER')}:{config.get('DB_PASSWORD')}@" \
             f"{config.get('DB_HOST')}:{config.get('DB_PORT')}/{config.get('DB_DATABASE')}"

    LOGGING_LEVEL: str = 'INFO'
    SA_LOGS: bool = False

    @property
    def LOGGING_CONFIG(self):
        config = {
            'loggers': {
                'alembic': {
                    'handlers': ['default'],
                    'level': self.LOGGING_LEVEL,
                    'propagate': False
                }
            }
        }

        if self.SA_LOGS:
            config['loggers']['sqlalchemy'] = {
                'handlers': ['default'],
                'level': self.LOGGING_LEVEL,
                'propagate': False
            }

        return config
