import requests

slackTokenTXT = open('slackToken.txt', 'r')
slackToken = slackTokenTXT.read()


def sendMessageSlack(channel, text):
    """send Slack message"""
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + slackToken},
                             data={"channel": channel, "text": text}
                             )
    print(response)
