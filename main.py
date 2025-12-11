from fastapi import FastAPI
from telethon import TelegramClient
import os

app = FastAPI()

API_ID = int(os.getenv("32244403"))
API_HASH = os.getenv("c63b95f0a3c363dc09ee594a2de16106"))
SESSION = "lookup_session"

@app.get("/")
def home():
    return {"status": "API Running"}

@app.get("/lookup")
async def lookup(phone: str):
    try:
        client = TelegramClient(SESSION, API_ID, API_HASH)
        await client.start()
        result = await client.get_entity(phone)

        return {
            "phone": phone,
            "username": result.username,
            "first_name": result.first_name,
            "last_name": result.last_name
        }

    except Exception as e:
        return {"error": str(e)}
