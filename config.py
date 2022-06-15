from pydantic import BaseSettings
import os

ROOT_DIR = os.path.join("..")


class MlApiSettings(BaseSettings):
    ML_API_USERNAME: str = ''
    ML_API_PASSWORD: str = ''
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'logs/cfy_ner.log',
                'level': 'DEBUG',
                'formatter': 'simple',
                'when': 'midnight',
                'interval': 1,
                'backupCount': 7
            },
        },
        'loggers': {
            '1': {
                'handlers': ['file_handler'],
                'level': 'DEBUG',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
        },
    }

    class Config:
        env_file = ".env"
