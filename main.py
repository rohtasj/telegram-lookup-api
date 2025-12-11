from fastapi import FastAPI
from telethon import TelegramClient
import os

app = FastAPI()

# ✅ Environment variables (set in Render)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION = "lookup_session"

@app.get("/")
def home():
    return {"status": "API Running"}

@app.get("/lookup")
async def lookup(phone: str):
    try:
        # Create Telegram client
        client = TelegramClient(SESSION, API_ID, API_HASH)
        await client.start()

        # Get Telegram user info
        result = await client.get_entity(phone)

        return {
            "phone": phone,
            "username": result.username,
            "first_name": result.first_name,
            "last_name": result.last_name
        }

    except Exception as e:
        return {"error": str(e)}
