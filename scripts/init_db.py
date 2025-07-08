#!/usr/bin/env python3
import sys
import os

# Add the parent directory to Python path to allow importing app modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from app.db.init_db import init_db

if __name__ == "__main__":
    print("Initializing database...")
    try:
        init_db()
        print("Database initialization completed successfully!")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        sys.exit(1) 