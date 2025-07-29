from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import movies, actors, directors, genres

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Movie Explorer API",
    description="A comprehensive API for exploring movies, actors, directors, and genres",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Vue.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(movies.router, prefix="/api")
app.include_router(actors.router, prefix="/api")
app.include_router(directors.router, prefix="/api")
app.include_router(genres.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to Movie Explorer API", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"} 