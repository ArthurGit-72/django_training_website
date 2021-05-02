import requests

token = '1754059008:AAFJoCwsoRcpjOmn3Lq5QwQODlXFeLY7kVY'
chat_id = '-536512127'
text = 'Test_2'



def sendTelegram():
	api = 'https://api.telegram.org/bot'
	method = api + token + '/sendMessage'

	req = requests.post(method, data={
		'chat_id': chat_id,
		'text': text
		})

sendTelegram()