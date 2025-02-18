import os
from typing import List
from urllib.parse import quote
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from faststream.rabbit import RabbitBroker
from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMIN_IDS: List[int]
    INIT_DB: bool
    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"
    # DB_URL: str = 'sqlite+aiosqlite:///data/db.sqlite3'
    STORE_URL: str = 'sqlite:///data/jobs.sqlite' # заменить на PostgreSQL !!!
    TABLES_JSON: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dao", "tables.json")
    SLOTS_JSON: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dao", "slots.json")

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    BASE_URL: str
    RABBITMQ_USERNAME: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    VHOST: str

    @property
    def rabbitmq_url(self) -> str:
        return (
            f"amqp://{self.RABBITMQ_USERNAME}:{quote(self.RABBITMQ_PASSWORD)}@"
            f"{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/{self.VHOST}"
        )

    @property
    def hook_url(self) -> str:
        """Возвращает URL вебхука"""
        return f"{self.BASE_URL}/webhook"

    def get_db_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")
    
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    
    )

# Инициализация конфигурации
settings = Settings()

# Настройка логирования
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
logger.add(log_file_path, format=settings.FORMAT_LOG, level="INFO", rotation=settings.LOG_ROTATION)

# Создание брокера сообщений RabbitMQ
broker = RabbitBroker(url=settings.rabbitmq_url)

# Создание планировщика задач
scheduler = AsyncIOScheduler(jobstores={'default': SQLAlchemyJobStore(url=settings.STORE_URL)})