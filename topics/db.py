import os
from dotenv import load_dotenv
load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

connection_string = f"mysql+pymysql://{user}:{password}@{host}:3306/{db}"