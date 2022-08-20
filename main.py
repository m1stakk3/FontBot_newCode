import telebot
from keyboard_actions import Keyboard
from methods_caller import Caller
from text_handler import TextEditor

bot = telebot.TeleBot('2018392915:AAFdEpg4G1RXvY8q3B6rBCSaFP-oXLA258s')


@bot.message_handler(commands=['start'])
def welcome_message(message):
    if message.text == '/start':
        markup = Keyboard.welcome_keyboard()
        global st
        st = bot.send_message(message.chat.id, '🔥 Чтобы продолжить, пожалуйста подпишитесь на каналы 👇🏻',
                              reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):

    if message.text in ['𝕰𝖝𝖆𝖒𝖕𝖑𝖊', '𝔈𝔵𝔞𝔪𝔭𝔩𝔢', '𝓔𝔁𝓪𝓶𝓹𝓵𝓮', 'ℰ𝓍𝒶𝓂𝓅𝓁𝑒', '𝗘𝘅𝗮𝗺𝗽𝗹𝗲',
                        '𝖤𝗑𝖺𝗆𝗉𝗅𝖾', '🄴🅇🄰🄼🄿🄻🄴', 'Ⓔⓧⓐⓜⓟⓛⓔ']:
        global current_text_mode
        current_text_mode = message.text
        markup = Keyboard.cancel_keyboard()
        bot.send_message(message.chat.id, 'Пришлите текст для конвертации в выбранный шрифт', reply_markup=markup)
        bot.register_next_step_handler(message, font_editor)

    elif message.text.lower()[2:] == 'оформить текст':
        markup = Keyboard.cancel_keyboard()
        bot.send_message(message.chat.id, 'Пришлите текст для обработки:\n\n'
                                          '— Для *разделения на абзацы* пришлите текст, скопируйте ответ бота и '
                                          'вставьте в Инстаграм\n'
                                          '— Для написания текста *с красной строки* поставьте две точки '
                                          'перед текстом\n'
                                          '— Для создания текста *по центру* поставьте две запятые перед текстом\n\n'
                                          'Например:\n\n'
                                          '..Красная строка\n,,Текст по центру\n\n'
                                          '*P.S.* Если точка или запятая находится не в конце слова, то она *удалится'
                                          ' при конвертации*',
                         reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(message, edit_text_mode)

    elif message.text.lower()[2:] == 'обход цензуры':
        markup = Keyboard.cancel_keyboard()
        bot.send_message(message.chat.id, 'Пришлите текст для обхода цензуры', reply_markup=markup)
        bot.register_next_step_handler(message, antispam_mode)

    elif message.text.lower() == 'назад':
        markup = Keyboard.call_keyboard()
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)


def edit_text_mode(message):
    """
    используется для работы с режимом "Оформить текст"
    пока не прислан текст "назад" функция перезапускается рекурсивно
    с передачей обработчка на саму себя
    """
    if message.text.lower() != 'назад':

        bot.send_message(message.chat.id, TextEditor.editor(message))

        bot.register_next_step_handler(message, edit_text_mode)

    else:
        markup = Keyboard.call_keyboard()
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)


def antispam_mode(message):
    """
    функция работает с режимом "Антиспам", пока не прислали "отмена" перезапускается рекурсивно
    """
    if message.text.lower() != 'назад':
        change_dict = {'е': 'e', 'Е': 'E', 'а': 'a', 'А': 'A', 'у': 'y', 'о': 'o', 'О': 'O'}
        result = [change_dict[i] if i in change_dict.keys() else i for i in message.text]
        bot.send_message(message.chat.id, ''.join(result))
        bot.register_next_step_handler(message, antispam_mode)

    else:
        markup = Keyboard.call_keyboard()
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)


def font_editor(message):

    if message.text.lower() != 'назад':
        font_set = {'𝕰𝖝𝖆𝖒𝖕𝖑𝖊': 'f1', '𝔈𝔵𝔞𝔪𝔭𝔩𝔢': 'f2', '𝓔𝔁𝓪𝓶𝓹𝓵𝓮': 'f3', 'ℰ𝓍𝒶𝓂𝓅𝓁𝑒': 'f4', '𝗘𝘅𝗮𝗺𝗽𝗹𝗲': 'f5',
                    '𝖤𝗑𝖺𝗆𝗉𝗅𝖾': 'f6', '🄴🅇🄰🄼🄿🄻🄴': 'f7', 'Ⓔⓧⓐⓜⓟⓛⓔ': 'f8'}
        bot.send_message(message.chat.id, TextEditor.converter(message, font_set[current_text_mode]))
        bot.register_next_step_handler(message, font_editor)

    else:
        markup = Keyboard.call_keyboard()
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if bot.get_chat_member(chat_id='-1001725631650', user_id=call.from_user.id).status in ['creator',
                                                                                           'administrator',
                                                                                           'member']:
        markup = Keyboard.call_keyboard()
        bot.send_message(call.from_user.id, '🤖 Привет! Это — самый полезный бот, когда нужен *классный* '
                                            'и *красивый* шрифт для соцсетей.\n\nТакже бот очень полезен '
                                            'для Инстаграма:\n\n'
                                            '*• «Оформить текст»* — разделить текст на абзацы, сделать красную строку '
                                            'или центрировать.\n'
                                            '*• «Обход цензуры»* — обойти цензуру в Инстаграме и не получить бан.\n'
                                            '*• Всё, что ниже верхних двух кнопок* — это сами шрифты.',
                         reply_markup=markup, parse_mode="Markdown")
        bot.delete_message(st.chat.id, st.message_id)


bot.infinity_polling()
