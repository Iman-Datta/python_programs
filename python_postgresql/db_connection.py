from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_dbconnection():
    database_url = "postgresql://testuser:testpassword@127.0.0.1:5432/testdb"

    try:
        engine = create_engine(database_url)
        print("Successfully connected to database")
        Session = sessionmaker(engine)
        session = Session()
        return session, engine
    except Exception as e:
        print(f"Exception occur {e}")
        return None, None
    
session, engine = create_dbconnection()

if engine:
    print("You can perform CRUD operation")
else:
    print("Failed to established database connection")