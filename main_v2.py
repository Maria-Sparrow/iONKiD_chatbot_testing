import csv

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from collections import defaultdict

user_dict = defaultdict(list)

list_task = []
with open('therapy_tasks.txt', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='%')
    line_count = 0
    for row in csv_reader:
        protocol = [row[0], row[1], row[2]]
        list_task.append(protocol)
        line_count = line_count+1
    print(line_count)
    list_task.append(("FINISH", 0))

TOKEN = '1413602973:AAH_6QtvLAj53H3Ri29ln1Vhr9kgRHkFpEQ'
bot = Bot(token=TOKEN)

# ------------- Buttons -------------
inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_btn_1 = InlineKeyboardButton('+', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('-', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('Self', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('Спростити', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('Ускладнити', callback_data='btn5')
inline_kb_full.row(inline_btn_1, inline_btn_2, inline_btn_3).row(inline_btn_4, inline_btn_5)
button_plus = KeyboardButton('/terapia')

button_close = KeyboardButton('/send_file')

text_test = "ckndvondvodovndovn"
protocol_1 = ("test1.1", "test1.2", "test1.3")
protocol_2 = ("test2.1", "test2.2", "test2.3")
protocol_3 = ("test3.1", "test3.2", "test3.3")

dp = Dispatcher(bot)
list_test = ["Test protocol"]
markup_big = ReplyKeyboardMarkup(resize_keyboard=True)

markup_big.add(
    button_plus
)
markup_big.row(
    button_close
)

protocol_1 = ("test1.1", "test1.2", "test1.3")
protocol_2 = ("test2.1", "test2.2", "test2.3")
protocol_3 = ("test3.1", "test3.2", "test3.3")

iter_num = []
user_dict_complex_task = defaultdict(int)

user_dict_flag_task = defaultdict(int)


@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    print(user_dict_flag_task)
    code = callback_query.data[-1]
    # print("==", callback_query.data)
    len_list_task = len(list_task)
    # it = len(iter_num)
    test_2 = len(user_dict[callback_query.from_user.first_name])
    print(str(user_dict_complex_task[callback_query.from_user.first_name]) + " fuck")

    # print("oo", test_2)
    try:
        # обмеження к-ті тасок

        print(str(user_dict_complex_task[callback_query.from_user.first_name]) + " test")
        print(user_dict_complex_task)

        print(str(len(user_dict[callback_query.from_user.first_name])) + " чорт")

        if code.isdigit():
            code = int(code)

        if code == 1:

            user_dict[callback_query.from_user.first_name].append("+")
            await bot.send_message(callback_query.from_user.id,
                                   "Складність: "+str(user_dict_complex_task[callback_query.from_user.first_name]+1)+"\n"+
                                   list_task[0][user_dict_complex_task[callback_query.from_user.first_name]],
                                   reply_markup=inline_kb_full)
            # await bot.send_message(callback_query.from_user.id, f'Ти нажав +')


        elif code == 2:
            await bot.send_message(callback_query.from_user.id,"Складність: "+str(user_dict_complex_task[callback_query.from_user.first_name]+1)+"\n"+
                                   list_task[0][user_dict_complex_task[callback_query.from_user.first_name]],
                                   reply_markup=inline_kb_full)
            user_dict[callback_query.from_user.first_name].append("-")
            # await bot.send_message(callback_query.from_user.id, f'Ти нажав -')


        elif code == 3:
            await bot.send_message(callback_query.from_user.id,"Складність: "+str(user_dict_complex_task[callback_query.from_user.first_name]+1)+"\n"+
                                   list_task[0][user_dict_complex_task[callback_query.from_user.first_name]],
                                   reply_markup=inline_kb_full)
            user_dict[callback_query.from_user.first_name].append("Self")
            print(user_dict_complex_task[callback_query.from_user.first_name])

            # await bot.send_message(callback_query.from_user.id, f'Ти нажав Self')

        elif code == 4:

            if user_dict_complex_task[callback_query.from_user.first_name] == 0:
                await bot.send_message(callback_query.from_user.id, "нiзя")
                # await bot.answer_callback_query(callback_query.id)
                print(len_list_task)
            else:
                user_dict_complex_task[callback_query.from_user.first_name] -= 1
                print(str(user_dict_complex_task[callback_query.from_user.first_name]) + "спростити")
                await bot.send_message(callback_query.from_user.id,"Складність: "+str(user_dict_complex_task[callback_query.from_user.first_name]+1)+"\n"+
                                       list_task[0][user_dict_complex_task[callback_query.from_user.first_name]],
                                       reply_markup=inline_kb_full)
                # await bot.answer_callback_query(callback_query.id)


        elif code == 5:

            try:
                if user_dict_complex_task[callback_query.from_user.first_name] < 2:
                    user_dict_complex_task[callback_query.from_user.first_name] += 1
                    it = user_dict_complex_task[callback_query.from_user.first_name]
                    print(str(user_dict_complex_task[callback_query.from_user.first_name]) + "ускладнити")
                    print(user_dict_complex_task[callback_query.from_user.first_name])
                    await bot.send_message(callback_query.from_user.id,"Складність: "+str(user_dict_complex_task[callback_query.from_user.first_name]+1)+"\n"+
                                           list_task[0][user_dict_complex_task[callback_query.from_user.first_name]],
                                           reply_markup=inline_kb_full)


                else:
                    await bot.send_message(callback_query.from_user.id, f'ускладнення неможливе')
                    print("ніхуя собі а всьо нізя")
            except IndexError:

                await bot.send_message(callback_query.from_user.id, f'ускладнення неможливе')
                print("да бляяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяять")



    except IndexError:
        await bot.send_message(callback_query.from_user.id, f'Достаааааааа')
        print(str(user_dict) + " zbhjh")


# bot.py
@dp.message_handler(commands=['terapia'])
async def process_hi7_command(message: types.Message):
    try:
        print(user_dict_flag_task[message.from_user.first_name])
        await message.reply("Складність: "+str(user_dict_complex_task[message.from_user.first_name]+1)+"\n"+list_task[0][
                                user_dict_complex_task[message.from_user.first_name]], reply_markup=inline_kb_full)

        print("eeeeeeeeeeeeeeeeeeeeee?")
        if user_dict_flag_task[message.from_user.first_name] == 0:
            user_dict_flag_task[message.from_user.first_name] = 1
    except IndexError:

        user_dict[message.from_user.first_name] = 0
        print(IndexError)
        print("Чорт")


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


#
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
#     print(msg.text)
#     print(msg.from_user.first_name + "_" + str(msg.from_user.id) + ".csv")
#     if (msg.text == "+"):
#         print("plus")
#         print(msg.text)
#
#         list_test.append(msg.text)
#         # create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)
#
#
#     elif (msg.text == "-"):
#         list_test.append(msg.text)
#         print("minus")
#         print(msg.text)
#         user_dict[msg.from_user.first_name].append(msg.text)
#         print(user_dict)
#         # create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)
#
#     elif (msg.text == "Self"):
#         list_test.append(msg.text)
#         print("Self")
#         print(msg.text)
#     # create_write_to_file(msg.from_user.first_name + "_" + str(msg.from_user.id), msg.text)
#
#
# #

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
