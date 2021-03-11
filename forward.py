import configparser


from telethon import TelegramClient, events, sync


# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['TELEGRAM']['api_id']
api_hash = config['TELEGRAM']['api_hash']
username = config['TELEGRAM']['username']
resend_from_chat = config['TELEGRAM']['resend_from_chat']


client = TelegramClient('session_name', api_id, api_hash)
client.start()

# chats allow listen multiple chats
@client.on(events.NewMessage(chats=resend_from_chat.split(',')))
async def main(event):
    msg = event.message.to_dict()
    await client.send_message('receiver_chat', event.message)
    
with client:
    client.run_until_disconnected()