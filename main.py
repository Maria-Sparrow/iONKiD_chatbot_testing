#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import csv
from collections import defaultdict

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor, markdown

from task_buttons import inline_kb_full
from therapy_buttons import markup_launch, markup_main, markup_finish

TOKEN = '1475672387:AAGkNWnDIh8rBt0eclIaEfKkaNqKF1CEiGQ'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
user_dict = defaultdict(list)

list_task = []
with open('therapy_tasks.txt', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='%')
    line_count = 0
    for row in csv_reader:
        protocol = [row[0], row[1], row[2]]
        list_task.append(protocol)
        line_count = line_count + 1
    print(line_count)
    list_task.append(('FINISH', 0))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        'Вітаю, ' + message.from_user.full_name + '!\n Натисніть на ' + markdown.bold('"Почати терапію"') +
        ', коли будете готові.',
        reply_markup=markup_launch,
        parse_mode=ParseMode.MARKDOWN
    )


@dp.message_handler(text=['Почати терапію'])
async def process_start_command(message: types.Message):
    await message.reply('Терапія почалася.', reply_markup=markup_main)


@dp.message_handler(text=['Завершити терапію'])
async def process_help_command(message: types.Message):
    await message.reply('Будь ласка, підтвердіть дію.', reply_markup=markup_finish)


@dp.message_handler(text=['Повернутися назад'])
async def process_help_command(message: types.Message):
    await message.reply('Повертаємось...', reply_markup=markup_main)


@dp.message_handler(text=['Згенерувати файл з результатами'])
async def process_file_command(message: types.Message):
    user_dict_complex_task[message.from_user.first_name] = 0
    user_dict_protocol_number[message.from_user.first_name] = -1

    write_to_file(message.from_user.first_name)
    with open(message.from_user.first_name + ".csv", encoding='utf8') as file:
        await message.reply('Генерую файл з результатами...', reply_markup=markup_launch)
        await message.answer_document(file)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply('Ви берете участь у закритому тестуванні бота, якого розробляють студенти-другокурсники ' +
                        markdown.bold('Львівської політехніки') + ', спеціальності ' +
                        markdown.bold('"Інтернет речей"') +
                        '. Я створений, щоб допомагати вам проводити терапії:\n\n'
                        '– буду почергово виводити короткий зміст вправ, які потрібно виконати з дитиною сьогодні;\n\n'
                        '– дозволю вам швидше переключатися між різними рівнями складності;\n\n'
                        '– запам\'ятовуватиму результати кожної ітерації.\n\n'
                        'Для того, щоб розпочати терапію, просто натисніть на кнопку.',
                        parse_mode=ParseMode.MARKDOWN
                        )


###########################################################


user_dict_complex_task = defaultdict(int)
user_dict_flag_task = defaultdict(int)
user_dict_protocol_number = defaultdict(int)


@dp.callback_query_handler()
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    print(user_dict_flag_task)
    code = callback_query.data[-1]

    print(str(user_dict_complex_task[callback_query.from_user.first_name]) + ' fuck')

    try:
        # обмеження к-ті тасок

        print(str(user_dict_complex_task[callback_query.from_user.first_name]) + ' test')
        print(user_dict_complex_task)

        print(str(len(user_dict[callback_query.from_user.first_name])) + ' чорт')

        if code.isdigit():
            code = int(code)

        # code = 1, 2, 3
        if code < 4:

            print(user_dict)
            complex_empty = user_dict_complex_task[callback_query.from_user.first_name] + 1
            print(str(complex_empty) + ' пропуски')
            if complex_empty == 1:
                user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                    user_dict_complex_task[callback_query.from_user.first_name] + 2)].append("  ")
                user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                    user_dict_complex_task[callback_query.from_user.first_name] + 3)].append("  ")

            if complex_empty == 2:
                user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                    user_dict_complex_task[callback_query.from_user.first_name])].append("  ")
                user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                    user_dict_complex_task[callback_query.from_user.first_name] + 2)].append("  ")

            if complex_empty == 3:
                user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                    user_dict_complex_task[callback_query.from_user.first_name] - 1)].append("  ")
                user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                    user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                    user_dict_complex_task[callback_query.from_user.first_name])].append("  ")
            await send_task(callback_query)

            current_protocol_complex = user_dict[str(callback_query.from_user.first_name) + "Протокол:" + str(
                user_dict_protocol_number[callback_query.from_user.first_name] + 1) + "Складність:" + str(
                user_dict_complex_task[callback_query.from_user.first_name] + 1)]

            if code == 1:
                current_protocol_complex.append('+')
            elif code == 2:
                current_protocol_complex.append('-')
            elif code == 3:
                current_protocol_complex.append('C')

            print(user_dict)
            print(user_dict_complex_task[callback_query.from_user.first_name])

        elif code == 4:
            if user_dict_complex_task[callback_query.from_user.first_name] == 0:
                await bot.send_message(callback_query.from_user.id, 'Спрощення цієї вправи неможливе.')

            else:
                user_dict_complex_task[callback_query.from_user.first_name] -= 1
                print(str(user_dict_complex_task[callback_query.from_user.first_name]) + ' спростити')
                await send_task(callback_query)

        elif code == 5:

            try:
                if user_dict_complex_task[callback_query.from_user.first_name] < 2:
                    user_dict_complex_task[callback_query.from_user.first_name] += 1
                    print(str(user_dict_complex_task[callback_query.from_user.first_name]) + ' ускладнити')
                    print(user_dict_complex_task[callback_query.from_user.first_name])
                    await send_task(callback_query)

                else:
                    await bot.send_message(callback_query.from_user.id, f'Ускладнення цієї вправи неможливе.')
                    print('ніхуя собі а всьо нізя')
            except IndexError:

                await bot.send_message(callback_query.from_user.id, f'Ускладнення цієї вправи неможливе.')
                print('да бляяяяяяяяяять')

    except IndexError:
        await bot.send_message(callback_query.from_user.id, f'Ви виконали максимально можливу кількість вправ.')
        print(str(user_dict) + ' zbhjh')


# bot should reply to types.CallbackQuery with a new message, and reply to types.Message with 'reply'
async def send_task(message_source):
    message = markdown.bold('Протокол: ') + str(user_dict_protocol_number[message_source.from_user.first_name] + 1) + \
              '\n' + \
              markdown.bold('Складність: ') + str(user_dict_complex_task[message_source.from_user.first_name] + 1) + \
              '\n\n' + \
              list_task[user_dict_protocol_number[message_source.from_user.first_name]][
                  user_dict_complex_task[message_source.from_user.first_name]]
    if isinstance(message_source, types.CallbackQuery):
        await bot.send_message(message_source.from_user.id,
                               message,
                               reply_markup=inline_kb_full,
                               parse_mode=ParseMode.MARKDOWN)
    elif isinstance(message_source, types.Message):
        user_dict_flag_task[message_source.from_user.first_name] = 1
        await message_source.reply(message,
                                   reply_markup=inline_kb_full,
                                   parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(text=['Наступна вправа'])
async def process_hi7_command(message: types.Message):
    try:
        print(user_dict_flag_task[message.from_user.first_name])
        if user_dict_flag_task[message.from_user.first_name] != 0:
            print('e?')
            user_dict_complex_task[message.from_user.first_name] = 0
            user_dict_protocol_number[message.from_user.first_name] += 1
        # щоб не дійти до #16-заглушки
        if user_dict_protocol_number[message.from_user.first_name] >= len(list_task) - 1:
            user_dict_protocol_number[message.from_user.first_name] = len(list_task) - 2
            await message.reply('На сьогодні вправи закінчилися.')
        else:
            await send_task(message)

        print('eeeeeeeeeeeeeeeeeeeeee?')

    except IndexError:

        print(IndexError)
        print('Чорт')


@dp.message_handler(text=['Попередня вправа'])
async def process_hi7_command(message: types.Message):
    try:
        print(user_dict_flag_task[message.from_user.first_name])
        if user_dict_flag_task[message.from_user.first_name] != 0:
            print('e?')
            user_dict_complex_task[message.from_user.first_name] = 0
            user_dict_protocol_number[message.from_user.first_name] -= 1
        if user_dict_protocol_number[message.from_user.first_name] < 0:
            user_dict_protocol_number[message.from_user.first_name] = -1
            await message.reply('Попередніх вправ немає.')
        else:
            await send_task(message)
        print('ПРОТОКОЛ НОМЕР ' + str(user_dict_protocol_number[message.from_user.first_name]))

        print('eeeeeeeeeeeeeeeeeeeeee?')

    except IndexError:

        print(IndexError)
        print('Чорт')


def write_to_file(file_name):
    with codecs.open(file_name + '.csv', "a", encoding='utf-8-sig') as f:
        f.write('\n')
        for protocol_number in range(1, 16):
            f.write("Протокол #" + str(protocol_number))
            f.write('\n')
            f.write("Ітерація")
            f.write(',')
            for iteration in range(1, 41):
                f.write(str(iteration) + ',')
            f.write('\n')
            for sub_protocol_number in range(1, 4):
                f.write('\n')
                f.write(u"Етап " + str(sub_protocol_number) + ',')
                for k in user_dict[str(file_name) + 'Протокол:' + str(protocol_number) + 'Складність:'
                                   + str(sub_protocol_number)]:
                    f.write(str(k) + ',')
                f.write('\n')
            f.write('\n')


if __name__ == '__main__':
    executor.start_polling(dp)
