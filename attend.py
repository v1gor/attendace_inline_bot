import telebot
from telebot import types
# TODO LIST
#Make db
#Make register
#Make admin


token = ''
bot = telebot.TeleBot(token)

home = { 'lon' : 76.913358, 'lat' : 43.229191 }


@bot.inline_handler(lambda query: query.query == 'тут')
def query_text(inline_query):
	lon = inline_query.location.longitude
	lat = inline_query.location.latitude

	mx = abs(home.get('lon') - lon)
	my = abs(home.get('lat') - lat)

	dist = ((mx**2 + my**2) ** 0.5 ) * 100
	min_dist = 0.2

	if dist<=min_dist:
		print('Nice')
	else:
		print('Ты находишься в ' +str(dist)[0:4]+ ' от места работы')

def registerUser(message):
	pass

@bot.message_handler(content_types = ['text'])
def handle_text(message):
	text = message.text
	text = text.lower()

	if text == 'ахтунг':
		registerUser(message)

bot.polling()
