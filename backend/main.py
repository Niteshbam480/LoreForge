from backend.core.config import settings
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from backend.auth.router import router as auth_router
from backend.universes.router import router as universe_router
from backend.nodes.router import router as node_router
from backend.relationships.router import router as relationship_router
from backend.search.router import router as search_router
from backend.nodes.models import Node
from backend.relationships.models import Relationship
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title=settings.APP_NAME,version=settings.APP_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    status = {
        "APP_NAME":settings.APP_NAME,
        "APP_VERSION":settings.APP_VERSION,
        "status": "OK"
    }
    return status


app.include_router(auth_router,prefix="/auth",tags=["auth"])
app.include_router(universe_router,prefix="/universes",tags=["universes"])
app.include_router(node_router,prefix="/nodes",tags=["nodes"])
app.include_router(relationship_router,prefix="/relationships",tags=["relationships"])
app.include_router(search_router,prefix="/search",tags=["search"])

@app.exception_handler(RequestValidationError)
def request_validation_error_handler(request:Request,exc: RequestValidationError):
    return JSONResponse(status_code=422,content={"detail":"Invalid request data","errors":exc.errors()})

@app.exception_handler(Exception)
def request_validation_error_handler(request:Request,exc:Exception):
    return JSONResponse(status_code=500,content={"detail":"Internal server error"})