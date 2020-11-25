from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from collections import defaultdict

user_dict = defaultdict(list)

TOKEN = '1483412678:AAFNfs6V_PlZABFMAZUf712_-xHzuZQ662o'
bot = Bot(token=TOKEN)

# ------------- Buttons -------------
inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_btn_1 = InlineKeyboardButton('+', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('-', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('Self', callback_data='btn3')
inline_kb_full.row(inline_btn_1, inline_btn_2, inline_btn_3)
button_plus = KeyboardButton('/terapia')

button_close = KeyboardButton('/send_file')

text_test = "ckndvondvodovndovn"
protocol_1 = ("test1", "test1.2", "test1.3")
protocol_2 = ("test2", "test2.2", "test2.3")
protocol_3 = ("test3", "test3.2", "test3.3")
list_task = [protocol_1, protocol_2, protocol_3,
             ("FINISH", 0)]
dp = Dispatcher(bot)
list_test = ["Test protocol"]
markup_big = ReplyKeyboardMarkup(resize_keyboard=True)

markup_big.add(
    button_plus
)
markup_big.row(
    button_close
)


@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    test = len(list_task)

    test_2 = len(user_dict[callback_query.from_user.first_name]) + 1
    print(test_2)
    try:
        # обмеження к-ті тасок
        if len(user_dict[callback_query.from_user.first_name]) < test:
            print(test_2)
            dif = 0
            await bot.send_message(callback_query.from_user.id,
                                   list_task[test_2][dif],
                                   reply_markup=inline_kb_full)
            print(len(user_dict[callback_query.from_user.first_name]))

            if code.isdigit():
                code = int(code)
            if code == 1:
                user_dict[callback_query.from_user.first_name].append("+")

                await bot.answer_callback_query(callback_query.id)

                # await bot.send_message(callback_query.from_user.id, f'Ти нажав +')

            elif code == 2:

                list_test.append("-")
                await bot.answer_callback_query(callback_query.id)
                user_dict[callback_query.from_user.first_name].append("-")
                # await bot.send_message(callback_query.from_user.id, f'Ти нажав -')
            elif code == 3:
                list_test.append("Self")
                await bot.answer_callback_query(callback_query.id)

                user_dict[callback_query.from_user.first_name].append("Self")
                # await bot.send_message(callback_query.from_user.id, f'Ти нажав Self')
            elif code == 4:
                await bot.answer_callback_query(callback_query.id)

    except IndexError:

        await bot.send_message(callback_query.from_user.id, f'Достаааааааа')
        print(user_dict)


# bot.py
@dp.message_handler(commands=['terapia'])
async def process_hi7_command(message: types.Message):
    await message.reply(list_task[len(user_dict[message.from_user.first_name])][0], reply_markup=inline_kb_full)


@dp.message_handler(commands=['send_file'])
async def process_file_command(message: types.Message):
    # write_to_file(message.from_user.first_name + "_" + str(message.from_user.id))
    create_write_to_file(message.from_user.first_name)
    with open(message.from_user.first_name + ".csv") as file:
        await message.reply("Ось твій файлик", reply_markup=markup_big)
        await message.answer_document(file)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привітик!\nНапиши мені якщо тобі скучно)", reply_markup=markup_big)



@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    print(msg.text)
    print(msg.from_user.first_name + "_" + str(msg.from_user.id) + ".csv")
    if (msg.text == "+"):
        print("plus")
        print(msg.text)

        list_test.append(msg.text)
        # create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)


    elif (msg.text == "-"):
        list_test.append(msg.text)
        print("minus")
        print(msg.text)
        user_dict[msg.from_user.first_name].append(msg.text)
        print(user_dict)
        # create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)

    elif (msg.text == "Self"):
        list_test.append(msg.text)
        print("Self")
        print(msg.text)
    # create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)
#

def create_write_to_file(file_name):
    f = open(file_name + ".csv", 'a+', newline='')
    f.write("Iteration")
    f.write('\n')
    for i in user_dict[file_name]:
        f.write(str(i) + ",")
    f.close()


if __name__ == '__main__':

    executor.start_polling(dp)
