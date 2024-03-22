import requests
import pprint

import requests
token ='7126361746:AAG3mWWHmYDUbhaImJ4LqeHulru8H8yQvFk'
main_url = f'https://api.telegram.org/bot{token}'
#url = f'{main_url}/getMe'

#result = requests.get(url)
#print(result.json())

url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())

messages =result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Ваше сообщение было отправленно'
    }
    result = requests.post(url,params=params)