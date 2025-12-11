from fastapi import FastAPI
from telethon.sync import TelegramClient
import os

app = FastAPI()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = "lookup_session"

@app.get("/")
def home():
    return {"status": "API Running"}

@app.get("/lookup")
def lookup(phone: str):
    try:
        client = TelegramClient(SESSION, API_ID, API_HASH)
        client.start()
        result = client.get_entity(phone)
        client.disconnect()

        return {
            "phone": phone,
            "username": result.username,
            "first_name": result.first_name,
            "last_name": result.last_name
        }

    except Exception as e:
        return {"error": str(e)}
