import os
from dotenv import load_dotenv

load_dotenv("witkey.env")

WITKEY = os.getenv('WITKEY')
