from app.db.database import SessionLocal
from app.db.seed import seed_database

def main():
    """Main function to seed the database."""
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()

if __name__ == "__main__":
    main() 