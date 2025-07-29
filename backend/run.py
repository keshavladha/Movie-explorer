import uvicorn
from app.seed_data import seed_database

if __name__ == "__main__":
    # Seed database on startup
    print("Seeding database...")
    seed_database()
    
    # Start the server
    print("Starting Movie Explorer API server...")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 