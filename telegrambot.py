import telebot
from telebot import types
bot = telebot.TeleBot('7181725455:AAF990YHlxJyuEAdqGRyK76jKrcLBlFOev4')

markup01 = types.InlineKeyboardMarkup()
markup02 = types.InlineKeyboardMarkup()
markup03 = types.InlineKeyboardMarkup()
markup04 = types.InlineKeyboardMarkup()
markup05 = types.InlineKeyboardMarkup()
markup06 = types.InlineKeyboardMarkup()
list_markups = [markup02, markup03, markup04, markup05, markup06]

D1 = {}
list1 = ['⛹️ Физкультура', '👅 Языки', '🇷🇺 История России', '⛺️ Безопасность жизнедеятельности', '🧐 Философия', '🧮 Математика', '🧲 Физика', '💻 Программирование']
for i in range(len(list1)):
    D1.update({list1[i]:i})

for i in D1:
    markup01.add(types.InlineKeyboardButton(i, callback_data=str(D1.get(i))))

D2 = {}
list2 = ['🌏 Общая физика', '⚡️ Электродинамика', '⚙️ Теоретическая механика', '✅ Математическая физика', '🧪 Физическая химия', '⚛️ Квантовая механика', '⚽️ Теория упругости', '💯 Численные методы', '🔩 Лабораторные работы']
for i in range(len(list2)):
    D2.update({list2[i]:i})

for i in D2:
    markup02.add(types.InlineKeyboardButton(i, callback_data=str(D2.get(i)).rjust(2, '0')))

D3 = {}
list3 = ['🍪 Дифференциальные уравнения', '📈 Математический анализ', '🎲 Теор. вероятности и мат. статистика', '📐 Линейная алгебра', '🔓 Функции комплексного переменного', '🔢 Теория групп', '➿ Топология']
for i in range(len(list3)):
    D3.update({list3[i]:i})

for i in D3:
    markup03.add(types.InlineKeyboardButton(i, callback_data=str(D3.get(i)).rjust(3, '0')))

D4 = {}
list4 = ['🇨🇳 Китайский', '🇩🇪 Немецкий', '🇪🇸 Испанский', '🇬🇧 Английский']
for i in range(len(list4)):
    D4.update({list4[i]:i})

for i in D4:
    markup04.add(types.InlineKeyboardButton(i, callback_data=str(D4.get(i)).rjust(4, '0')))

D5 = {}
list5 = ['🪆 Русская культура', '📻 Российская наука и техника', '📊 Социальная история России', '💸 Россия и мир в ХХ веке', '⚔️ Россия в международных отношениях', '📝 Реформы и реформаторы в России']
for i in range(len(list5)):
    D5.update({list5[i]:i})

for i in D5:
    markup05.add(types.InlineKeyboardButton(i, callback_data=str(D5.get(i)).rjust(5, '0')))

D6 = {}
list6 = ['📃 Лекции по программированию', '🔁 Алгоритмы', '🖥 Физическое моделирование', '💾 Хранение и обработка данных', '🤖 Машинное обучение']
for i in range(len(list6)):
    D6.update({list6[i]:i})

for i in D6:
    markup06.add(types.InlineKeyboardButton(i, callback_data=str(D6.get(i)).rjust(6, '0')))


for n in list_markups:
    n.add(types.InlineKeyboardButton('Назад', callback_data='back'))
@bot.message_handler(commands=['start'])
def main_choose(message):
    bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=markup01)

@bot.callback_query_handler(func=lambda callback: True)
def second_choose(callback):
    if callback.data == str(D1.get('🧲 Физика')):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбери тему', reply_markup=markup02)
    elif callback.data == str(D1.get('🧮 Математика')):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбери тему', reply_markup=markup03)
    elif callback.data == str(D1.get('👅 Языки')):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбери тему', reply_markup=markup04)
    elif callback.data == str(D1.get('🇷🇺 История России')):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбери тему', reply_markup=markup05)
    elif callback.data == str(D1.get('💻 Программирование')):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбери тему', reply_markup=markup06)
    elif callback.data == 'back':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id, 'Выбери предмет', reply_markup=markup01)

bot.polling(none_stop=True)