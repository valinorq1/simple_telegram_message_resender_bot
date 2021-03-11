import configparser
config = configparser.ConfigParser()
config['TELEGRAM'] = {'api_id': 'you_api_id',
                    'api_hash': 'you_api_hash',
                      'username': 'you_username',
                      'resend_from_chat': 'telebot,botfather'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)