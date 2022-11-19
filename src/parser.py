from src.services import *
from src.pythonREPL import execute_python

def parseMessage(msg):
	chatId = msg['message']['chat']['id']
	text = msg['message']['text'].strip('\n').strip()
	return chatId, text

def parseCommand(text):
	if text.startswith('/runpy'):
		code = text.strip('/runpy')
		result = execute_python(code)
		return result
	elif text.startswith('/date'):
		return get_date()
	elif text.startswith('/time'):
		return get_time()
	elif text.startswith('/quote'):
		return get_quote()

	return text