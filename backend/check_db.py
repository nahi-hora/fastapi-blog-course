import os
import sys
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect

load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_server = os.getenv("POSTGRES_SERVER", "localhost")
postgres_port = os.getenv("POSTGRES_PORT", 5432)
postgres_db = os.getenv("POSTGRES_DB")

db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
print("Connecting to:", db_url)

try:
    engine = create_engine(db_url)
    inspector = inspect(engine)
    print("Connection successful!")
    print("Tables in DB:", inspector.get_table_names())
except Exception as e:
    print("Error connecting to database:")
    print(e)
    sys.exit(1)
