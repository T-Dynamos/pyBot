import requests
from flask import Flask, request, Response
from src.pythonREPL import execute_python

TOKEN = "5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0"
app = Flask(__name__)

def parseMessage(msg):
	chatId = msg['message']['chat']['id']
	text = msg['message']['text'].strip('\n').strip()
	return chatId, text

def sendMsg(id, text):
	url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
	payload = {
		'chat_id' : id,
		'text' : text
	}
	r = requests.post(url, json=payload)
	return r

def parseCommand(text):
	if text.startswith('/runpy'):
		code = text.strip('/runpy')
		result = execute_python(code)
		return result

	return text


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		msg = request.get_json()
		chatId, text = parseMessage(msg)
		result = parseCommand(text)
		sendMsg(chatId, result)

		return Response('ok', status=200)
	return "<h1> Hello Bot </h1>"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)

# https://api.telegram.org/bot5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0/setWebhook?url=https://425d-2409-4063-4c07-7d1e-41a8-cc42-8179-be51.in.ngrok.io