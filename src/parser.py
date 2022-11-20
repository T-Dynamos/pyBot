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
		output = execute_python(code)
		result = f"""Execution Results 

Execution time : {output[0]}
Return Code : {output[-1]}

Errors:
{output[1][0]}

Output:
{output[1][-1]}"""
		return result
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