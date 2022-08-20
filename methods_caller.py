from text_handler import TextEditor
import telebot


class Caller:

    bot = telebot.TeleBot('2018392915:AAFdEpg4G1RXvY8q3B6rBCSaFP-oXLA258s')

    @staticmethod
    def text_edit(message):
        if message.text.lower()[:2] == '..':
            return bot.send_message(message.chat.id, TextEditor.paragraph(message))

        elif message.text.lower()[:2] == ',,':
            return bot.send_message(message.chat.id, TextEditor.center(message))