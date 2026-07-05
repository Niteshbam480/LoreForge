from backend.core.config import settings
from fastapi import FastAPI
from backend.auth.router import router as auth_router


app = FastAPI(title=settings.APP_NAME,version=settings.APP_VERSION)


@app.get("/health")
def health():
    status = {
        "APP_NAME":settings.APP_NAME,
        "APP_VERSION":settings.APP_VERSION,
        "status": "OK"
    }
    return status


app.include_router(auth_router,prefix="/auth",tags=["auth"])

