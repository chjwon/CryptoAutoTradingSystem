import telegram
# pip install python-telegram-bot
# @Testbot0000
telegramTokenTXT = open('messenger/telegramToken.txt', 'r')
telegramToken = telegramTokenTXT.read()

telegramChatIdTXT = open('messenger/telegramChatId.txt', 'r')
telegramChatId = telegramChatIdTXT.read()


def sendMessageTelegram(text):
    bot = telegram.Bot(token=telegramToken)
    bot.sendMessage(chat_id=telegramChatId, text=text)
    return True


# sendMessageTelegram('test')
