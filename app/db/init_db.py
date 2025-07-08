from sqlalchemy.orm import Session
from app.db.base import Base
from app.db.seed import seed_database
from app.db.database import engine, SessionLocal
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def reset_database():
    """Drop all tables and recreate them."""
    # Remove the SQLite database file if it exists
    db_file = "./fodmap.db"
    if os.path.exists(db_file):
        os.remove(db_file)
        logger.info("Removed existing database file.")

def init_db(force_reset: bool = False):
    """Initialize the database with tables and seed data.
    
    Args:
        force_reset: If True, will drop and recreate all tables before seeding.
    """
    if force_reset:
        logger.info("Forcing database reset...")
        reset_database()
    
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    # Create a new session using SessionLocal
    db = SessionLocal()
    try:
        # Seed the database
        seed_database(db, force_reset)
        logger.info("Database initialization completed successfully.")
    except Exception as e:
        logger.error(f"Error during database initialization: {str(e)}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    # When run directly, force a reset
    init_db(force_reset=True) 