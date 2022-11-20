from src.services import *
from src.pythonREPL import execute_python

def parseMessage(msg):
	print(msg)
	message = msg.get("message", None)
	if message:
		if 'chat' in message.keys() and 'text' in message.keys():
			chatId = message['chat']['id']
			text = message['text'].strip('\n').strip()
			return chatId, text
	return None, None

def parseCommand(text):
	if text.startswith('/runpy'):
		code = text.strip('/runpy')
		result = execute_python(code).rstrip('\n')
		return f"Result: \n{result}"
	elif text.startswith('/date'):
		return get_date()
	elif text.startswith('/time'):
		return get_time()
	elif text.startswith('/quote'):
		return get_quote()
	elif text.startswith('/about'):
		return """This bot is written by Prajjwal Pathak.
		Repo : https://github.com/pyGuru123/pyBot"""
	elif text.startswith('/youtube'):
		return "https://www.youtube.com/c/pyGuru"

	return text