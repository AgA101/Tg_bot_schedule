import telebot
from telebot import types
from keys import Token
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button_student = types.KeyboardButton(text='Студент')
    button_teacher = types.KeyboardButton(text='Преподаватель')
    markup.row(button_student, button_teacher)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}, кем вы являетесь ?', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def student(message):
    if message.text == 'Студент':
        bot.send_message(message.chat.id, f'Введите название группы', reply_markup=telebot.types.ReplyKeyboardRemove())
        file_group = open('./name_groups.txt', 'rb')
        bot.send_document(message.chat.id, file_group)


bot.polling(none_stop=True)