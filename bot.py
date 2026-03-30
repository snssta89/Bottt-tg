import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from config import TELEGRAM_TOKEN, ADMIN_ID

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="🔐 VPN Subscription")], [types.KeyboardButton(text="🎰 Lottery")], [types.KeyboardButton(text="👤 Profile")], [types.KeyboardButton(text="💰 Referral")]], resize_keyboard=True)
    await message.answer(f"👋 Welcome, {message.from_user.first_name}!
\nThis is a Monetization Bot.
\nChoose an option:", reply_markup=keyboard)

@dp.message(Command("vpn"))
async def vpn_menu(message: Message):
    await message.answer("🔐 VPN Service - Coming Soon!")

@dp.message(Command("lottery"))
async def lottery_menu(message: Message):
    await message.answer("🎰 Lottery - Coming Soon!")

@dp.message(Command("profile"))
async def profile_command(message: Message):
    await message.answer(f"👤 Profile of {message.from_user.first_name}")

@dp.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Access Denied!")
        return
    await message.answer("🛠️ Admin Panel - Active")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Available Commands:\n/start\n/vpn\n/lottery\n/profile\n/help")

@dp.message()
async def handle_text(message: Message):
    await message.answer("Use /help for commands")

async def main():
    logger.info("Bot starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
