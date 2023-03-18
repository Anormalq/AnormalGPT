#Not: Bu kodlar @Mr_Anormal Tarafından yazılmıştır bot daha yapım aşamasında ufak tefek hatalar olabilir güncellenecektir kullanacaksanız Cr vereceksiniz !!!

import telebot

import openai

#Bot Api Token

API_TOKEN = 'Enter your telegram bot api token here '

#Openai Api Key

openai.api_key="Enter your openai api token here"

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









 

