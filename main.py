from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '1483412678:AAFNfs6V_PlZABFMAZUf712_-xHzuZQ662o'

button_plus = KeyboardButton('+')
button_minus = KeyboardButton('-')
button_self = KeyboardButton('Self')
button_close = KeyboardButton('/send_file')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button_plus, button_minus, button_self
)
markup_big.row(
    button_close
)


# bot.py
@dp.message_handler(commands=['test'])
async def process_hi7_command(message: types.Message):
    await message.reply("Починаєм відмічати таски)", reply_markup=markup_big)


@dp.message_handler(commands=['send_file'])
async def process_file_command(message: types.Message):
    with open(message.from_user.first_name + "_" + str(message.from_user.id) + ".csv") as file:
        await message.reply("Ось твій файлик", reply_markup=markup_big)
        await message.answer_document(file)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привітик!\nНапиши мені якщо тобі скучно)")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    print(msg.text)
    print(msg.from_user.first_name + "_" + str(msg.from_user.id) + ".csv")
    if (msg.text == "+"):
        print("plus")
        print(msg.text)
        create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)


    elif (msg.text == "-"):
        print("minus")
        print(msg.text)
        create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)

    elif (msg.text == "Self"):
        print("Self")
        print(msg.text)
        create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)


def create_write_to_file(file_name, result):
    f = open(file_name + ".csv", 'a', newline='')

    f.write(str(result))
    f.write('\n')
    f.close()


if __name__ == '__main__':
    executor.start_polling(dp)
