from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# * Launch
button_launch = KeyboardButton('Почати терапію')
markup_launch = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup_launch.add(button_launch)

markup_main = ReplyKeyboardMarkup(resize_keyboard=True)
next_task_btn = KeyboardButton('Наступна вправа')
prev_task_btn = KeyboardButton('Попередня вправа')
end_therapy_btn = KeyboardButton('Завершити терапію')
markup_main.row(prev_task_btn, next_task_btn).add(end_therapy_btn)

button_go_back = KeyboardButton('Повернутися назад')
button_generate_file = KeyboardButton('Згенерувати файл з результатами')
markup_finish = ReplyKeyboardMarkup(resize_keyboard=True)
markup_finish.add(button_go_back).add(button_generate_file)
