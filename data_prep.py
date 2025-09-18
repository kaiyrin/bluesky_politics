from atproto import Client
import os
from dotenv import load_dotenv

client = Client()
load_dotenv()
username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

client.login(username, password)
