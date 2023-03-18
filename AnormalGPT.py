#Not: Bu kodlar @Mr_Anormal Tarafından yazılmıştır bot daha yapım aşamasında ufak tefek hatalar olabilir güncellenecektir kullanacaksanız Cr vereceksiniz !!!

import telebot

import openai

#Bot Api Token

API_TOKEN = '6265571825:AAGzmoM0K4Q-5_b5XBv5wHwt6T5XVYVRzhg'

#Openai Api Key

openai.api_key="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"

bot = telebot.TeleBot(API_TOKEN)

#Yanıtı Oluşturun

def get_response(msg):

	completion = openai.Completion.create(    engine="text-davinci-003",

    prompt=msg,

    max_tokens=1024,

    n=1,

    stop=None,

    temperature=0.5,

)

	return completion.choices[0].text

# '/start' ve '/help' işlemlerini yapın

@bot.message_handler(commands=['help', 'start'])

def send_welcome(message):

	 # bot.send_message(message.chat.id,message.text)

	   bot.send_message(message.chat.id, """\

Hey, Merhaba. bugün nasıl gidiyor? soru sormak için /sor yazman yeterli sonra sabaha kadar konuşabiliriz :) """)

#'/sor'u İşle

@bot.message_handler(commands=['sor'])

def first_process(message):

	bot.send_message(message.chat.id,"Sor bakayim")

	bot.register_next_step_handler(message,second_process)

def again_send(message):

  bot.register_next_step_handler(message,second_process)

def second_process(message):

  bot.send_message(message.chat.id,get_response(message.text))

  again_send(message)

 

bot.infinity_polling()

#Not: Bu kodlar @Mr_Anormal Tarafından yazılmıştır bot daha yapım aşamasında ufak tefek hatalar olabilir güncellenecektir kullanacaksanız Cr vereceksiniz !!!

import telebot

import openai

#Bot Api Token

API_TOKEN = '6265571825:AAGzmoM0K4Q-5_b5XBv5wHwt6T5XVYVRzhg'

#Openai Api Key

openai.api_key="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"

bot = telebot.TeleBot(API_TOKEN)

#Yanıtı Oluşturun

def get_response(msg):

	completion = openai.Completion.create(

    engine="text-davinci-003",

    prompt=msg,

    max_tokens=1024,

    n=1,

    stop=None,

    temperature=0.5,

)

	return completion.choices[0].text

# '/start' ve '/help' işlemlerini yapın

@bot.message_handler(commands=['help', 'start'])

def send_welcome(message):

	 # bot.send_message(message.chat.id,message.text)

	   bot.send_message(message.chat.id, """\

Hey, Merhaba. bugün nasıl gidiyor? soru sormak için /sor yazman yeterli sonra sabaha kadar konuşabiliriz :) """)

#'/sor'u İşle

@bot.message_handler(commands=['sor'])

def first_process(message):

	bot.send_message(message.chat.id,"Sor bakayim")

	bot.register_next_step_handler(message,second_process)

def again_send(message):

  bot.register_next_step_handler(message,second_process)

def second_process(message):

  bot.send_message(message.chat.id,get_response(message.text))

  again_send(message)

 

bot.infinity_polling()
