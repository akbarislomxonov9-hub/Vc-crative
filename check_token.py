import asyncio
from dotenv import dotenv_values
from aiogram import Bot

token = (dotenv_values(".env").get("BOT_TOKEN") or "").strip()
print("Token topildi:", bool(token))
print("Token uzunligi:", len(token))

async def main():
    if not token:
        print(".env faylida BOT_TOKEN topilmadi!")
        return

    bot = Bot(token=token)
    try:
        user = await bot.get_me()
        print("TOKEN ISHLAYDI!")
        print("Bot username:", user.username)
        print("Bot ID:", user.id)
    except Exception as e:
        print("XATO:", type(e).__name__)
        print("Tafsilot:", str(e))
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
