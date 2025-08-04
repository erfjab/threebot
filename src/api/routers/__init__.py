from fastapi import APIRouter
from . import base


def setup_api_routers() -> APIRouter:
    router = APIRouter()
    router.include_router(base.router)
    return router


__all__ = ["setup_api_routers"]
