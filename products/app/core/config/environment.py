import os
from dotenv import load_dotenv
load_dotenv()

POSTGRES_DB_URL = os.getenv("POSTGRES_DB_URL")

