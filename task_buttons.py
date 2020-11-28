from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb_full = InlineKeyboardMarkup(row_width=2)
check_plus_btn = InlineKeyboardButton('+', callback_data='btn1')
check_minus_btn = InlineKeyboardButton('-', callback_data='btn2')
check_self_btn = InlineKeyboardButton('С', callback_data='btn3')
simplify_task_btn = InlineKeyboardButton('Спростити', callback_data='btn4')
complicate_task_btn = InlineKeyboardButton('Ускладнити', callback_data='btn5')
inline_kb_full.row(check_plus_btn, check_minus_btn, check_self_btn).row(simplify_task_btn, complicate_task_btn)
