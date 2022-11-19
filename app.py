from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		msg = request.get_json()
		print(msg)

		return Response('ok', status=200)
	return "<h1> Hello Bot </h1>"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)

# https://api.telegram.org/bot5830914299:AAEyaoz_yGrTzVi2cLMeC6B91QWQho3fUp0/setWebhook?url=https://abb1-47-9-105-149.in.ngrok.io