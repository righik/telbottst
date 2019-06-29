#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telebot
import config
import requests
import json
import random
from telebot import types
bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def cmd_start(message):
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('мак')
        itembtn2 = types.KeyboardButton('кино')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "выбери:", reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def vbr(message):
        global cost 
        if message.text == 'мак':
            mkcost = 1
            cost = mkcost
            markup = types.ReplyKeyboardMarkup()
            itembtn1 = types.KeyboardButton('оплатил')
            markup.add(itembtn1)
            koment = 'rekvizity_qiwi: +7(123)4567890' + ' / koment_zakaza: ' + message.text + '_' + str(message.message_id)
            global komgl
            komgl = message.text + '_' + str(message.message_id)
            bot.send_message(message.chat.id, koment, reply_markup=markup)            
        elif message.text == 'кино':
            markup = types.ReplyKeyboardMarkup()
            itembtn1 = types.KeyboardButton('оплатил')
            markup.add(itembtn1)
            kncost = 2
            cost = kncost
            koment = 'rekvizity_qiwi: +7(123)4567890' + ' / koment_zakaza: ' + message.text + '_' + str(message.message_id)
            komgl = message.text + '_' + str(message.message_id)
            bot.send_message(message.chat.id, koment, reply_markup=markup)
        elif message.text == 'оплатил':
            url = 'https://edge.qiwi.com/payment-history/v2/persons/79688569979/payments?rows=1'
            headers = {
                    'Accept' : 'application/json',
                    'Content-Type' : 'application/json',
                    'Authorization' : 'Bearer b7d35b2d6f69cba9e806d22e1a2aa87a'
            }
            r = requests.get(url, headers = headers)
            r.raise_for_status() # do not create the result file until json is parsed
            data = r.json()
            sm = int(data['data'][0]['sum']['amount'])
            kom = data['data'][0]['comment']
            k = message.message_id
            if (sm == cost and kom == komgl):
                bot.send_message(message.chat.id, 'красава держи ништяк')
            print(komgl)
            print(k)
            print(kom)
            print(sm)
                        


bot.polling(none_stop=True, interval=0)
