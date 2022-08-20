from telebot import types


class Keyboard:
    """
    вся работа с виртуальной клавиатурой
    """
    @staticmethod
    def call_keyboard():

        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtn_text = types.KeyboardButton('📝 Оформить текст')
        itembtn_antispam = types.KeyboardButton('🔞 Обход цензуры')
        itembtn1 = types.KeyboardButton('𝕰𝖝𝖆𝖒𝖕𝖑𝖊')
        itembtn2 = types.KeyboardButton('𝔈𝔵𝔞𝔪𝔭𝔩𝔢')
        itembtn3 = types.KeyboardButton('𝓔𝔁𝓪𝓶𝓹𝓵𝓮')
        itembtn4 = types.KeyboardButton('ℰ𝓍𝒶𝓂𝓅𝓁𝑒')
        itembtn5 = types.KeyboardButton('𝗘𝘅𝗮𝗺𝗽𝗹𝗲')
        itembtn6 = types.KeyboardButton('𝖤𝗑𝖺𝗆𝗉𝗅𝖾')
        itembtn7 = types.KeyboardButton('🄴🅇🄰🄼🄿🄻🄴')
        itembtn8 = types.KeyboardButton('Ⓔⓧⓐⓜⓟⓛⓔ')
        markup.row(itembtn_text)
        markup.row(itembtn_antispam)
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)
        return markup

    @staticmethod
    def hide_keyboard():
        """скрывает клаву при сценарии вызова работы с определенным шрифтом"""
        markup = types.ReplyKeyboardRemove(selective=False)
        return markup

    @staticmethod
    def cancel_keyboard():
        """появляется пока активен режим работы с определенным шрифтом"""
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Назад')
        markup.add(itembtn1)
        return markup

    @staticmethod
    def welcome_keyboard():
        markup = types.InlineKeyboardMarkup()
        url = types.InlineKeyboardButton(text='Канал: №1', url='https://t.me/fontbottest')
        check_sub = types.InlineKeyboardButton(text='Проверить', callback_data='is_sub')
        markup.add(url, check_sub)
        return markup


