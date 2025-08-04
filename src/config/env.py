from decouple import config
from dotenv import load_dotenv

load_dotenv(override=True)

### Develop Settings
DEBUG = config("DEBUG", default=False, cast=bool)

### Database Settings
DATABASE_USERNAME = config("DATABASE_USERNAME", default="", cast=str)
DATABASE_PASSWORD = config("DATABASE_PASSWORD", default="", cast=str)
DATABASE_HOST = config("DATABASE_HOST", default="localhost", cast=str)
DATABASE_PORT = config("DATABASE_PORT", default=5432, cast=int)
DATABASE_NAME = config("DATABASE_NAME", default="", cast=str)
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

### API Settings
UVICORN_PORT = config("UVICORN_PORT", default=443, cast=int)
UVICORN_HOST = config("UVICORN_HOST", default="0.0.0.0")
UVICORN_SSL_CERTFILE = config("UVICORN_SSL_CERTFILE", default="")
UVICORN_SSL_KEYFILE = config("UVICORN_SSL_KEYFILE", default="")
DOCS = config("DOCS", default="/docs", cast=str)
