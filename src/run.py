import logging
from uvicorn import Config, Server
from src.api import API
from src.config import (
    UVICORN_SSL_CERTFILE,
    UVICORN_SSL_KEYFILE,
    UVICORN_HOST,
    UVICORN_PORT,
)

logger = logging.getLogger(__name__)


async def main():
    cfg = Config(
        app=API,
        host=UVICORN_HOST,
        port=UVICORN_PORT,
        workers=1,
    )

    if UVICORN_SSL_CERTFILE and UVICORN_SSL_KEYFILE:
        cfg.ssl_certfile = UVICORN_SSL_CERTFILE
        cfg.ssl_keyfile = UVICORN_SSL_KEYFILE
        logger.info("SSL configuration loaded successfully")

    server = Server(cfg)
    logger.info(f"Starting server on {UVICORN_HOST}:{UVICORN_PORT}")
    await server.serve()
