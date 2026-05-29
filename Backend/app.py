from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import employee_routes
from db.config import engine, Base
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create database tables
logger.info("Creating database tables...")
Base.metadata.create_all(bind=engine)
logger.info("Database tables created successfully")

# Initialize FastAPI app
app = FastAPI(
    title="Employee Management System API",
    description="REST API for managing employees",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(employee_routes.router)

@app.get("/")
def root():
    return {
        "message": "Employee Management System API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "GET /api/employees": "Get all employees",
            "POST /api/employees": "Add new employee",
            "DELETE /api/employees/{id}": "Delete employee"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "connected"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )