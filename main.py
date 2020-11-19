from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram import Bot
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext

button_plus = "+"
button_minus = "-"
button_self = "C"
button_close = "END"


def messege_handler(update: Update, contex: CallbackContext):
    file_name = str(update.message.from_user.name)
    reply_markup = ReplyKeyboardMarkup(

        keyboard=[[KeyboardButton(text=button_self),
                   ], [KeyboardButton(text=button_plus), KeyboardButton(text=button_minus),
                       ], [KeyboardButton(text=button_close), ],
                  ],
        resize_keyboard=True,
    )
    text = update.message.text
    try:
        if (text == button_close):
            create_write_to_file(file_name,text)
            update.message.reply_text(
                text="Свято си скінчило на жуй файл",
                reply_markup=reply_markup

            )
        elif (text == button_plus):
            create_write_to_file(file_name,text)
            update.message.reply_text(
                text="Ого ти нажав '+';",
                reply_markup=reply_markup

            )
        elif (text == button_self):
            create_write_to_file(file_name,text)
            update.message.reply_text(
                text="Ого ти нажав 'C';",
                reply_markup=reply_markup

            )
        elif (text == button_minus):
            create_write_to_file(file_name,text)
            update.message.reply_text(
                text="Ого ти нажав '-';",
                reply_markup=reply_markup

            )
        elif (int(text)):

            test = int(text) * int(text)
            update.message.reply_text(
                text="Єба то буде в квадраті: " + str(test) + ";",
                reply_markup=reply_markup

            )
    except ValueError:

        update.message.reply_text(
            text='йобаний шашлик то якась хуйня',

            reply_markup=reply_markup

        )


#
# def do_echo(update: Update, bot: Bot):
#     text = update.message.text
#     bot.send_message(
#         chat_id=update.message.chat_id,
#         text=text
#     )
#     print(text)
def create_write_to_file(file_name,result):

    f = open(file_name+"_terapia.csv", 'a')

    f.write(str(result))

    f.close()


def start_bot(TOKEN):
    print("Start this piece of shit")

    updater = Updater(

        token=TOKEN,
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=messege_handler))
    # messege_echo = MessageHandler(Filters.text, do_echo)
    #
    # updater.dispatcher.add_handler(messege_echo)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    TOKEN = '1483412678:AAFNfs6V_PlZABFMAZUf712_-xHzuZQ662o'

    start_bot(TOKEN)
