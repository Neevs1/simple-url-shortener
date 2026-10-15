import os
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, inspect, text



def connect_to_db():
    postgres_user = os.getenv("DB_USERNAME")
    postgres_password = os.getenv("DB_PASSWORD")
    engine = create_engine(f"postgresql+psycopg://{postgres_user}:{postgres_password}@postgres:5432/urlshortener")
    return engine

def test_connection():
    engine = connect_to_db()
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)
    conn = engine.connect()
    result = conn.execute(text("""
        SELECT current_database(),
               current_schema(),
               current_user,
               inet_server_addr(),
               inet_server_port()
    """))
    print(result.fetchone())
