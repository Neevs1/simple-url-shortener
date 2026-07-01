from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
import dotenv
dotenv.load_dotenv()
engine = create_engine("postgresql://user:password@localhost/dbname")