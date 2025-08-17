import os

from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = os.getenv('BOT_USERNAME')
TOKEN = os.getenv('TOKEN')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')