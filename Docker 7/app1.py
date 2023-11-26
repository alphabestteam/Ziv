import os
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)
APP_PORT = 5000
RESPONE_FORMAT = '<body style="background:{color};color:white"><b style="font-family:comic-sans;font-size:60px">{text}</b></div>'


@app.route('/')
def hello_world():
	log_file_path = f'/app/logs/{request.remote_addr}.log'
	if os.path.exists(log_file_path):
		with open(log_file_path) as buff:
			name = buff.read()
			return RESPONE_FORMAT.format(color='green', text=f'Welcome back, {name.capitalize()}! I recognized you.')

	return RESPONE_FORMAT.format(color='red', text=f'Enter your name under http://thisapp:{APP_PORT}/{{name}} so I can get to know you!')

@app.route('/<name>')
def logger(name):
	if name.startswith('favicon'):
		return ''

	if not os.path.exists('/app/logs'):
		os.mkdir('/app/logs')

	log_file_path = f'/app/logs/{request.remote_addr}.log'
	with open(log_file_path, 'w') as buff:
		buff.write(name)

	return RESPONE_FORMAT.format(color='blue', text=f'Hello, {name.capitalize()}! Now I know you.')


if __name__ == '__main__':
	app.run('0.0.0.0', APP_PORT)