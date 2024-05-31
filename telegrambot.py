import telebot
from telebot import types
from data import *

bot = telebot.TeleBot('7227822094:AAF8d2eKdzzukxxr2z9-zjzRUgPmDX27Ai0')
# t.me/physics1478_bot

all_markups = {}


def reverse_cut(line):
    index = 0
    for i in range(len(line) - 1, 0, -1):
        if line[i] == '.':
            index = i
            break
    return line[:index]
def cut(line):
    index = 0
    for i in range(0, len(line), -1):
        if line[i] == '.':
            index = i
    return line[index+1:]


def traverse_dictionary_immutable(info, dct, suffix=''):
    new_dct = {}
    ans = {}
    for key in dct:
        if isinstance(dct[key], dict):
            new_dct.update(traverse_dictionary_immutable(info, dct[key], suffix + key + '.'))

        else:
            new_dct[suffix + key] = dct[key]

    for key in new_dct:
        ans.update({key: new_dct[key]})
    return ans


def send_message(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    print(callback.data)
    bot.send_message(callback.message.chat.id,'Выбирай', reply_markup=all_markups[callback.data])


def final_send(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    bot.send_document(callback.message.chat.id, callback.data[0], reply_markup=all_markups[callback.data[1]])


all_markups = traverse_dictionary_immutable(info, subjects)

for elm in all_markups:
    markup = types.InlineKeyboardMarkup()
    if all_markups[elm][0] == '+':
        markup.add(types.InlineKeyboardButton('Ютуб леккции', url=info[elm]['lections']))
    if all_markups[elm][1] == '+':
        markup.add(types.InlineKeyboardButton('Учебники', callback_data=info[elm]['textbooks']))
    if all_markups[elm][2] == '+':
        markup.add(types.InlineKeyboardButton('Решебники', callback_data=info[elm]['solvers']))
    all_markups[elm] = markup

for elm1 in subjects:
    if type(subjects[elm1]) != str:
        for elm2 in subjects[elm1]:
            if type(subjects[elm1][elm2]) != str:
                for elm3 in subjects[elm1][elm2]:
                            markup = types.InlineKeyboardMarkup()
                            for elm4 in subjects[elm1][elm2][elm3]:
                                if elm4 !=('-' or '+'):
                                    markup.add(types.InlineKeyboardButton(elm4, callback_data=str(elm1+'.'+elm2+'.'+elm3+'.'+elm4)))
                            all_markups[str(elm1+'.'+elm2+'.'+elm3)] = markup

for elm1 in subjects:
    if type(subjects[elm1]) != str:
        for elm2 in subjects[elm1]:
            if type(subjects[elm1][elm2]) != str:
                markup = types.InlineKeyboardMarkup()
                for elm3 in subjects[elm1][elm2]:
                        markup.add(types.InlineKeyboardButton(elm3, callback_data=str(elm1+'.'+elm2+'.'+elm3)))
                all_markups[str(elm1+'.'+elm2)] = markup


for elm1 in subjects:
    if type(subjects[elm1]) != str:
        markup = types.InlineKeyboardMarkup()
        for elm2 in subjects[elm1]:
                    markup.add(types.InlineKeyboardButton(elm2, callback_data=str(elm1+'.'+elm2)))
        all_markups[str(elm1)] = markup


for elm in all_markups:
    if elm != 'general':
        all_markups[elm].add(types.InlineKeyboardButton('Назад', callback_data=str(reverse_cut(elm)+'.back')))


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Выбери предмет',
                     reply_markup=all_markups['general'])


@bot.callback_query_handler(func=lambda callback: True)
def choose(callback):
    if 'books' in callback.data:
        file = open(callback.data, 'rb')
        bot.send_document(callback.message.chat.id, file)
    elif 'back' in callback.data:
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбирай', reply_markup=all_markups[reverse_cut(callback.data)])
    else:
        send_message(callback)


bot.polling(none_stop=True)
