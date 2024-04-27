import telebot
from telebot import types
import time

bot = telebot.TeleBot('6883403900:AAG7mEUX6N4PX6MOjnWzN-1Uf1tvaZCcO70')
queue = {'Versa': 0, 'Infinity': 0, 'Axesse': 0,
         'Halcyon': 0}  # переменная очереди


@bot.message_handler(commands=['start'])
def main(message):
    markup1 = types.ReplyKeyboardMarkup()
    btn_ochered = types.KeyboardButton('Очередь пациентов')  # Создаем кнопки
    btn_set = types.KeyboardButton('Для персонала')  # Создаем кнопки
    btn_set_youtube = types.KeyboardButton(
        'О линейных ускорителях')  # Создаем кнопки
    markup1.row(btn_ochered, btn_set)  # добавляем кнопки на панель
    markup1.row(btn_set_youtube)
    bot.send_message(
        message.chat.id, f'Здравствуйте,{message.from_user.first_name} {message.from_user.last_name} вас приветствует бот отделения дистанционной лучевой терапии \n Здесь вы можете узнать состояние очереди на аппаратах', reply_markup=markup1)
    bot.register_next_step_handler(message, raspred)


def raspred(message):
    if message.text == 'Очередь пациентов':
        a = telebot.types.ReplyKeyboardRemove()
        ochered(message)
    elif message.text == 'Для персонала':
        b = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,
                         'Введите команду ...', reply_markup=b)
        bot.register_next_step_handler(message, password)
    elif message.text == 'О линейных ускорителях':
        markup_btn = types.InlineKeyboardMarkup()
        markup_btn.add(types.InlineKeyboardButton('Перейти на youtube',
                       url='https://www.youtube.com/watch?v=sL2J76dRRbs&ab_channel=bdwind'))
        # ОТВЕТ НА СООБЩЕНИЕ ПОЛЬЗОВАТЕЛЯ ДРУГАЯ ФОРМА!!!!
        bot.reply_to(message, 'Ролик о линейных ускорителя',
                     reply_markup=markup_btn)
        time.sleep(1.5)
        main(message)
    else:
        bot.send_message(
            message.chat.id, 'Я не знаю такой команды попробуйте другую')
        time.sleep(1)  # задержка по времени
        main(message)


def password(message):
    if message.text.lower() == 'setver':
        bot.send_message(message.chat.id, 'Введите число пациентов в очереди')
        bot.register_next_step_handler(message, set_int_versa)
    elif message.text.lower() == 'setaxe':
        bot.send_message(message.chat.id, 'Введите число пациентов в очереди')
        bot.register_next_step_handler(message, set_int_axesse)
    elif message.text.lower() == 'setinf':
        bot.send_message(message.chat.id, 'Введите число пациентов в очередь')
        bot.register_next_step_handler(message, set_int_infinity)
    elif message.text.lower() == 'sethal':
        bot.send_message(message.chat.id, 'Введите число пациентов в очередь')
        bot.register_next_step_handler(message, set_int_halcyon)
    else:
        bot.send_message(message.chat.id, 'Я не знаю такой команды')
        time.sleep(1)  # задержка по времени
        main(message)


def ochered(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Versa')
    btn2 = types.KeyboardButton('Infinity')
    markup.row(btn1, btn2)
    btn3 = types.KeyboardButton('Axesse')
    btn4 = types.KeyboardButton('Halcyon')
    markup.row(btn3, btn4)
    bot.send_message(message.from_user.id,
                     'Выберите нужный аппарат', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):  # Получение количества пациентов    #РАБОТАЕТ НЕ ТРОГАТЬ (Sl0uKA)
    if message.text == 'Versa':
        bot.send_message(message.chat.id, queue['Versa'])
    elif message.text == 'Infinity':
        bot.send_message(message.chat.id, queue['Infinity'])
    elif message.text == 'Axesse':
        bot.send_message(message.chat.id, queue['Axesse'])
    elif message.text == 'Halcyon':
        bot.send_message(message.chat.id, queue['Halcyon'])
    else:
        bot.send_message(
            message.chat.id, 'Я не знаю такой команды,попробуйте еще раз')
    time.sleep(1)
    main(message)


def set_int_versa(message):  # VERSA
    ver_int = message.text
    queue['Versa'] = ver_int
    bot.send_message(message.from_user.id, 'Очередь записана!')
    main(message)


def set_int_axesse(message):  # AXESSE
    axe_int = message.text
    queue['Axesse'] = axe_int
    bot.send_message(message.from_user.id, 'Очередь записана!')
    main(message)


def set_int_infinity(message):  # INFINITY
    inf_int = message.text
    queue['Infinity'] = inf_int
    bot.send_message(message.from_user.id, 'Очередь записана!')
    main(message)


def set_int_halcyon(message):  # HALCYON
    halc_int = message.text
    queue['Halcyon'] = halc_int
    bot.send_message(message.from_user.id, 'Очередь записана!')
    main(message)

# @bot.message_handler(commands=['help'])
# def help(message):
    # bot.send_message(message.chat.id, 'Нажмите на кнопку интересующего вас аппарата и вам будет направленна информация о текущей очереди, обратите внимание что возможно задержки в обновлении количества пациентов')


bot.polling(none_stop=True)  # Бот работает бесконечно
