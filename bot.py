import typing
import os
import parse_rate
import parse_weather
import sentence_generator as gen
from config import TOKEN
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.callback_data import CallbackData
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! 👋\nНапиши /help чтобы узнать что я могу!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    commands = 'Доступные команды:\n\n'
    commands += '/start - Начало общения\n'
    commands += '/help - Вывод доступных команд\n'
    commands += '/weather - Погода\n'
    commands += '/rate - Курс выбранной валюты\n'
    commands += '/rand - Случайная фраза'
    await message.reply(commands)


data_cb = CallbackData('id', 'name', 'action')


@dp.message_handler(commands=['weather'])
async def process_weather_command(message: types.message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    moscow = types.InlineKeyboardButton(
        'Москва', callback_data=data_cb.new('moscow', 'temp'))
    peter = types.InlineKeyboardButton(
        'Санкт-Петербург', callback_data=data_cb.new('peter', 'temp'))

    markup.add(moscow, peter)
    await bot.send_message(chat_id=message.chat.id, text="Выберите город!", reply_markup=markup)


@dp.message_handler(commands=['rate'])
async def process_rate_command(message: types.message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    dollar = types.InlineKeyboardButton(
        'Доллар США', callback_data=data_cb.new('dollar', 'plot'))
    euro = types.InlineKeyboardButton(
        'Евро', callback_data=data_cb.new('euro', 'plot'))
    pound = types.InlineKeyboardButton(
        'Фунт стерлингов', callback_data=data_cb.new('pound', 'plot'))
    frank = types.InlineKeyboardButton(
        'Швейцарский франк', callback_data=data_cb.new('frank', 'plot'))
    cron = types.InlineKeyboardButton(
        'Шведская крона', callback_data=data_cb.new('cron', 'plot'))
    yena = types.InlineKeyboardButton(
        'Японская Йена', callback_data=data_cb.new('yena', 'plot'))

    markup.add(dollar, euro, pound, frank, cron, yena)
    await bot.send_message(chat_id=message.chat.id, text="Выберите валюту!", reply_markup=markup)


@dp.callback_query_handler(data_cb.filter(action='temp'))
async def process_chosen_city_command(call: CallbackQuery, callback_data: typing.Dict[str, str]):
    name = callback_data['name']
    await call.message.edit_text('Сейчас сделаю!')
    await process_temp_command(call.message, name)


@dp.callback_query_handler(data_cb.filter(action='plot'))
async def process_chosen_rate_command(call: CallbackQuery, callback_data: typing.Dict[str, str]):
    name = callback_data['name']
    await call.message.edit_text('Сейчас сделаю!')
    await process_plot_command(call.message, name)


@dp.message_handler(commands=['rand'])
async def process_generator_command(message: types.Message):
    sentence = gen.generate_sentence()
    await message.reply(sentence)


async def process_temp_command(message: types.Message, name):
    Dict = {"moscow": "Москве", "peter": "Санкт-Петербурге"}
    data = parse_weather.temperature(name)
    await bot.send_message(chat_id=message.chat.id, text='Ну и погодка в ' + Dict[name] + '!' + data)


async def process_plot_command(message: types.Message, name):

    img, cap = parse_rate.make_plot(name)
    img.savefig('fig.png')
    await bot.send_photo(chat_id=message.chat.id, photo=open('fig.png', 'rb'), caption=cap)
    if os.path.exists("fig.png"):
        os.remove("fig.png")


@ dp.message_handler()
async def echo_message(message: types.Message):
    await message.reply('Что это? Я так не умею 😪')


if __name__ == '__main__':
    executor.start_polling(dp)
