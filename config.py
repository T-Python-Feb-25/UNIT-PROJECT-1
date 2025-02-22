from dotenv import load_dotenv
import os
from truck_db import TruckDB
from user_db import UserDB 

# Load environment variables from a .env file
load_dotenv()

DATABASE = os.getenv("DATABASE_PATH")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
TOKEN = os.getenv("TOKEN")
PROVINCE=os.getenv("PROVINCE_PATH")
user_db = UserDB(DATABASE) 
truck_db = TruckDB(DATABASE) 
