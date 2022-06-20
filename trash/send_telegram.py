import telebot
import bot_config
from params import path_to_waiting_screenshot
from params import path_to_acceptance_screenshot

bot=telebot.TeleBot(bot_config.TOKEN)


def send_photo_Waiting(chat_id):
    waiting_png = open(path_to_waiting_screenshot, 'rb')
    bot.send_photo(chat_id, waiting_png)
def send_photo_Acceptance(chat_id):
    acceptance_png = open(path_to_acceptance_screenshot, 'rb')
    bot.send_photo(chat_id, acceptance_png)

# if __name__ == '__main__':
#     send_photo_Waiting(chat_id=BotConfig.chat_id)
#     send_photo_Acceptance(chat_id=BotConfig.chat_id)