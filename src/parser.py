from src.services import *
from src.pythonREPL import *

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
		output = CodeExecuter(code).execute_python()
		result = f"""Execution Results

Execution time : {output[0]}
Return Code : {output[-1]}

Errors:
{output[1][0] if output[1][0] != "" else None}

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
