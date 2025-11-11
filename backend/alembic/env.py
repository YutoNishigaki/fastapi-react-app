import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app.db.database import Base
from app.models import item  # models を import して metadata を登録

config = context.config
fileConfig(config.config_file_name)

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@db:5432/app")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_online():
    """Run migrations in 'online' mode."""
    engine = engine_from_config(config.get_section(config.config_file_name), 
                                prefix="sqlalchemy.", 
                                poolclass=pool.NullPool)
    with engine.connect() as conn:
        context.configure(connection=conn, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_independent():
    """Run migrations in 'independent' mode."""
    engine = engine_from_config(config.get_section(config.config_file_name), 
                                prefix="sqlalchemy.", 
                                poolclass=pool.NullPool)
    with engine.connect() as conn:
        context.configure(connection=conn, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if __name__ == "__main__":
    run_migrations_online()