from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import WebAppInfo

# ---- Новый токен Telegram ----
BOT_TOKEN = "8560279215:AAFUL0g6bfqYYdEqf95Hi7p6iA-C5zS4ACU"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_button = types.KeyboardButton(
        text="Открыть мини-приложение 📚",
        web_app=WebAppInfo(url="http://127.0.0.1:8080/index.html")
    )
    keyboard.add(webapp_button)
    await message.answer("Нажми кнопку, чтобы открыть мини-приложение 👇", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
