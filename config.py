from dotenv import load_dotenv
import os
from user_db import UserDB 
from openai import OpenAI
from truck_db import TruckDB
from order_db import OrderDB

# Load environment variables from a .env file
load_dotenv()

DATABASE = os.getenv("DATABASE_PATH")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")
TOKEN = os.getenv("TOKEN")
DATA=os.getenv("DATA")
user_db = UserDB(DATABASE) 
truck_db = TruckDB(DATABASE)
order_db = OrderDB(DATABASE) 

API_CLIENT = OpenAI(
    api_key=os.getenv("AI_API_KEY")
)