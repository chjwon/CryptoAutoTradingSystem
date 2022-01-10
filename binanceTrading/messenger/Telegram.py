import telegram
# pip install python-telegram-bot
telegramTokenTXT = open('telegramToken.txt', 'r')
telegramToken = telegramTokenTXT.read()

telegramChatIdTXT = open('telegramChatId.txt', 'r')
telegramChatId = telegramChatIdTXT.read()


def sendMessageTelegram(text):
    bot = telegram.Bot(token=telegramToken)
    bot.sendMessage(chat_id=telegramChatId, text=text)
    return True


# sendMessageTelegram('test')
