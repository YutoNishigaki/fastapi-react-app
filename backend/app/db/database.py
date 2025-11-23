from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:postgres@db:5432/app"

Engine = create_engine(  
    DATABASE_URL,
    echo=True
)

# Sessionの作成
SessionLocal = scoped_session(
    sessionmaker(
        autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)

# modelで使用する
Base = declarative_base()
Base.query = SessionLocal.query_property()