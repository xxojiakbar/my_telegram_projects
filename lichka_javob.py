import os 
from pathlib import Path
from dotenv import load_dotenv
from telethon import TelegramClient, events

path_env = Path(r"C:\Users\User\OneDrive\Desktop\Desktop\MaxfiyMalumotlar\.env")

load_dotenv(path_env)

api_id_path = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

if not api_id_path or not api_hash:
    raise ValueError(f"API_ID yoki API_HASH xatolik bermoqda:{path_env}")

api_id = int(api_id_path)

sessiya_fayl = Path(__file__).parent / "my_sessiya"

client = TelegramClient(str(sessiya_fayl), api_id, api_hash)

salomlashuv = [
    "salom",
    "assalom",
    "solom",
    "ossolom",
    "assalomu aleykum",
    "assalomu oleykum",
    "hi",
    "hello",
]

@client.on(events.NewMessage(incoming=True))
async def javob_ber(event):
    
    if not event.is_private:
        return
    
    matn = event.raw_text.strip().lower()
    
    if any(event.startswith(salom) for salom in salomlashuv):
        await event.reply("Assalom aleykum!")
    
if __file__ == "__main__":
    
    print("Dastur ishka tushmoqda...")
    
    client.start()
    
    print("Dastur muvaffaqiyatli ishga tushdi! ")
    
    client.run_until_disconnected()
    