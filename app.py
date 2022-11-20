import requests
from flask import Flask, request, Response
from src.parser import parseMessage, parseCommand
from src.pythonREPL import execute_python

TOKEN = "5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0"
BOTID = "-1001439604894"
app = Flask(__name__)

def sendMsg(id, text):
	url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
	if text:
		payload = {
			'chat_id' : id,
			'text' : text
		}
		response = requests.post(url, json=payload)
		return response

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		msg = request.get_json()
		chatId, text = parseMessage(msg)
		if chatId:
			result = parseCommand(text)
			sendMsg(chatId, result)

		return Response('ok', status=200)
	return "<h1> Hello Bot </h1>"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)

# https://api.telegram.org/bot5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0/setWebhook?url=https://ba79-2409-4063-4c07-7d1e-41a8-cc42-8179-be51.in.ngrok.io