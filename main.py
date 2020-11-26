import csv

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from collections import defaultdict

TOKEN = **********************************

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
user_dict = defaultdict(list)

list_task = []
with open('therapy_tasks.txt', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='%')
    line_count = 0
    for row in csv_reader:
        protocol = [row[0], row[1], row[2]]
        list_task.append(protocol)
        line_count = line_count + 1
    print(line_count)

# ------------- Buttons -------------
inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_btn_1 = InlineKeyboardButton('+', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('-', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('Self', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('Спростити', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('Ускладнити', callback_data='btn5')
inline_kb_full.row(inline_btn_1, inline_btn_2, inline_btn_3).row(inline_btn_4, inline_btn_5)


###########################################################
# ---------- Кнопки ----------

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привітик!\nНапиши мені якщо тобі скучно)", reply_markup=markup_main)


# * Launch
button_launch = KeyboardButton('Почати терапію')
markup_launch = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup_launch.add(button_launch)


@dp.message_handler(text=['Почати терапію'])
async def process_start_command(message: types.Message):
    await message.reply("Терапія почалася", reply_markup=markup_main)


button_next_exercise = KeyboardButton('Наступна вправа')
button_previous_exercise = KeyboardButton('Попередня вправа')
button_end_therapy = KeyboardButton('Завершити терапію')
markup_main = ReplyKeyboardMarkup(resize_keyboard=True)
markup_main.row(button_previous_exercise, button_next_exercise).add(button_end_therapy)


#
# @dp.message_handler(text=['Наступна вправа'])
# async def process_help_command(message: types.Message):
#     await message.reply("Переходимо до наступної вправи", reply_markup=markup_main)


@dp.message_handler(text=['Завершити терапію'])
async def process_help_command(message: types.Message):
    await message.reply("Підтвердіть дію", reply_markup=markup_finish)


button_go_back = KeyboardButton('Повернутися назад')
button_generate_file = KeyboardButton('Згенерувати файл')
markup_finish = ReplyKeyboardMarkup(resize_keyboard=True)
markup_finish.add(button_go_back).add(button_generate_file)


@dp.message_handler(text=['Повернутися назад'])
async def process_help_command(message: types.Message):
    await message.reply("ok", reply_markup=markup_main)


@dp.message_handler(text=['Згенерувати файл'])
async def process_file_command(message: types.Message):
    # write_to_file(message.from_user.first_name + "_" + str(message.from_user.id))
    user_dict_complex_task[message.from_user.first_name] = 0
    user_dict_protocol_number[message.from_user.first_name] = -1
    create_write_to_file(message.from_user.first_name)
    with open(message.from_user.first_name + ".csv") as file:
        await message.reply("Ось твій файлик", reply_markup=markup_launch)
        await message.answer_document(file)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши щось...")


###########################################################


user_dict_complex_task = defaultdict(int)
user_dict_flag_task = defaultdict(int)
user_dict_protocol_number = defaultdict(int)


@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    print(user_dict_flag_task)
    code = callback_query.data[-1]

    print(str(user_dict_complex_task[callback_query.from_user.first_name]) + " fuck")

    try:
        # обмеження к-ті тасок

        print(str(user_dict_complex_task[callback_query.from_user.first_name]) + " test")
        print(user_dict_complex_task)

        print(str(len(user_dict[callback_query.from_user.first_name])) + " чорт")

        if code.isdigit():
            code = int(code)

        if code == 1:

            user_dict[callback_query.from_user.first_name].append("+")

            await bot.send_message(callback_query.from_user.id, "Протокол: " + str(
                user_dict_protocol_number[callback_query.from_user.first_name] + 1) + '\n' +
                                   "Складність: " + str(
                user_dict_complex_task[callback_query.from_user.first_name] + 1) + "\n" +
                                   list_task[user_dict_protocol_number[callback_query.from_user.first_name]][
                                       user_dict_complex_task[callback_query.from_user.first_name]],
                                   reply_markup=inline_kb_full)
            # await bot.send_message(callback_query.from_user.id, f'Ти нажав +')

        elif code == 2:
            await bot.send_message(callback_query.from_user.id, "Протокол: " + str(
                user_dict_protocol_number[callback_query.from_user.first_name] + 1) + '\n' + "Складність: " + str(
                user_dict_complex_task[callback_query.from_user.first_name] + 1) + "\n" +
                                   list_task[user_dict_protocol_number[callback_query.from_user.first_name]][
                                       user_dict_complex_task[callback_query.from_user.first_name]],
                                   reply_markup=inline_kb_full)
            user_dict[callback_query.from_user.first_name].append("-")
            # await bot.send_message(callback_query.from_user.id, f'Ти нажав -')

        elif code == 3:
            await bot.send_message(callback_query.from_user.id, "Протокол: " + str(
                user_dict_protocol_number[callback_query.from_user.first_name] + 1) + '\n' + "Складність: " + str(
                user_dict_complex_task[callback_query.from_user.first_name] + 1) + "\n" +
                                   list_task[user_dict_protocol_number[callback_query.from_user.first_name]][
                                       user_dict_complex_task[callback_query.from_user.first_name]],
                                   reply_markup=inline_kb_full)
            user_dict[callback_query.from_user.first_name].append("Self")
            print(user_dict_complex_task[callback_query.from_user.first_name])

            # await bot.send_message(callback_query.from_user.id, f'Ти нажав Self')

        elif code == 4:
            if user_dict_complex_task[callback_query.from_user.first_name] == 0:
                await bot.send_message(callback_query.from_user.id, "нiзя")
                # await bot.answer_callback_query(callback_query.id)

            else:
                user_dict_complex_task[callback_query.from_user.first_name] -= 1
                print(str(user_dict_complex_task[callback_query.from_user.first_name]) + "спростити")
                await bot.send_message(callback_query.from_user.id, "Протокол: " + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + '\n' + "Складність: " + str(
                    user_dict_complex_task[callback_query.from_user.first_name] + 1) + "\n" +
                                       list_task[user_dict_protocol_number[callback_query.from_user.first_name]][
                                           user_dict_complex_task[callback_query.from_user.first_name]],
                                       reply_markup=inline_kb_full)
                # await bot.answer_callback_query(callback_query.id)

        elif code == 5:

            try:
                if user_dict_complex_task[callback_query.from_user.first_name] < 2:
                    user_dict_complex_task[callback_query.from_user.first_name] += 1
                    print(str(user_dict_complex_task[callback_query.from_user.first_name]) + "ускладнити")
                    print(user_dict_complex_task[callback_query.from_user.first_name])
                    await bot.send_message(callback_query.from_user.id, "Протокол: " + str(user_dict_protocol_number[
                                                                                               callback_query.from_user.first_name] + 1) + '\n' + "Складність: " + str(
                        user_dict_complex_task[callback_query.from_user.first_name] + 1) + "\n" +
                                           list_task[user_dict_protocol_number[callback_query.from_user.first_name]][
                                               user_dict_complex_task[callback_query.from_user.first_name]],
                                           reply_markup=inline_kb_full)

                else:
                    await bot.send_message(callback_query.from_user.id, f'ускладнення неможливе')
                    print("ніхуя собі а всьо нізя")
            except IndexError:

                await bot.send_message(callback_query.from_user.id, f'ускладнення неможливе')
                print("да бляяяяяяяяяять")

    except IndexError:
        await bot.send_message(callback_query.from_user.id, f'Достаааааааа')
        print(str(user_dict) + " zbhjh")


# bot.py


@dp.message_handler(text=['Наступна вправа'])
async def process_hi7_command(message: types.Message):
    try:
        print(user_dict_flag_task[message.from_user.first_name])
        if user_dict_flag_task[message.from_user.first_name] != 0:
            print("e?")
            user_dict_complex_task[message.from_user.first_name] = 0
            user_dict_protocol_number[message.from_user.first_name] += 1
        if user_dict_protocol_number[message.from_user.first_name] > len(list_task):
            await message.reply("На сьогодні вправи закінчилися")
        user_dict_flag_task[message.from_user.first_name] = 1
        await message.reply("Протокол: " + str(user_dict_protocol_number[message.from_user.first_name] + 1) + '\n' +
                            "Складність: " + str(user_dict_complex_task[message.from_user.first_name] + 1) + "\n" +
                            list_task[user_dict_protocol_number[message.from_user.first_name]][
                                user_dict_complex_task[message.from_user.first_name]], reply_markup=inline_kb_full)
        # await message.reply("Терапія почалася", reply_markup=markup_main)

        print("eeeeeeeeeeeeeeeeeeeeee?")

    except IndexError:

        print(IndexError)
        print("Чорт")


@dp.message_handler(text=['Попередня вправа'])
async def process_hi7_command(message: types.Message):
    try:
        print(user_dict_flag_task[message.from_user.first_name])
        if user_dict_flag_task[message.from_user.first_name] != 0:
            print("e?")
            user_dict_complex_task[message.from_user.first_name] = 0
            user_dict_protocol_number[message.from_user.first_name] -= 1
        if user_dict_protocol_number[message.from_user.first_name] < 0:
            user_dict_protocol_number[message.from_user.first_name] = -1
            await message.reply("Попередніх вправ немає")

        else:
            user_dict_flag_task[message.from_user.first_name] = 1
            await message.reply("Протокол: " + str(user_dict_protocol_number[message.from_user.first_name] + 1) + '\n' +
                                "Складність: " + str(user_dict_complex_task[message.from_user.first_name] + 1) + "\n" +
                                list_task[user_dict_protocol_number[message.from_user.first_name]][
                                    user_dict_complex_task[message.from_user.first_name]], reply_markup=inline_kb_full)
        print("ПРОТОКОЛ НОМЕР " + str(user_dict_protocol_number[message.from_user.first_name]))
        # await message.reply("Терапія почалася", reply_markup=markup_main)

        print("eeeeeeeeeeeeeeeeeeeeee?")

    except IndexError:

        print(IndexError)
        print("Чорт")


def create_write_to_file(file_name):
    f = open(file_name + ".csv", 'a+', newline='')
    f.write("Iteration")
    f.write('\n')
    for i in range(1, len(user_dict[file_name]) + 1):
        f.write(str(i) + ",")
    f.write('\n')
    for i in user_dict[file_name]:
        f.write(str(i) + ",")
    f.close()


if __name__ == '__main__':
    executor.start_polling(dp)
