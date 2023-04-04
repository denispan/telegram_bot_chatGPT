import logging
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pprint
import json

file = open('config.json', 'r')
config = json.load(file)

openai.api_key = config['openai']
bot = Bot(config['token'])
dp = Dispatcher(bot)

BOT_NAME = config['bot_name']
ADMIN_ID = config['admin_id']

messages = [
    {"role": "system", "content": "You are a Telegram bot based on the AI GPT-3.5 Turbo. You answer user's questions and maintain a conversation."},
    {"role": "user", "content": "I am a conversationalist. I can ask about anything."},
]

async def on_startup_notify(dp: Dispatcher):
    try:
        text = f'Запущен бот: <b>{BOT_NAME}</b> 😍'
        await dp.bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode='HTML')
        print('Бот успешно запущен')
    except Exception as err:
        logging.exception(err)


async def on_shutdown_notify(dp: Dispatcher):
    try:
        text = f'Остановлен бот: <b>{BOT_NAME}</b> ☠️'
        await dp.bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode='HTML')
        print('Бот остановлен')
    except Exception as err:
        logging.exception(err)


async def send_admin_message(message):
    text = f'From: <b>{message.from_user.username}</b>(id:{message.from_id})\n'\
           f'Text: {message.text}'

    await dp.bot.send_message(
        chat_id=config['admin_group_id'],
        text=text,
        parse_mode='HTML')

def update(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


@dp.message_handler()
async def send(message: types.Message):
    await send_admin_message(message)
    update(messages, "user", message.text)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    await message.answer(response['choices'][0]['message']['content'])

executor.start_polling(dp, skip_updates=True, on_startup=on_startup_notify, on_shutdown=on_shutdown_notify)
