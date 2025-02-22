from dotenv import load_dotenv
import os
from db_connector import DatabaseConnector as database

# Load environment variables from a .env file
load_dotenv()

DATABASE = os.getenv("DATABASE_PATH")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
TOKEN = os.getenv("TOKEN")
print(DATABASE)
db = database(DATABASE) 
