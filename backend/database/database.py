from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.core.config import settings


engine = create_engine(settings.DATABASE_URL,echo=False)
Base = declarative_base()
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    database = session()
    try:
        yield database
    
    finally:
        database.close()


