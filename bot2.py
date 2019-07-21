#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telebot
import config
import requests
import json
import sqlite3

from telebot import types
bot = telebot.TeleBot(config.token)

#conn = sqlite3.connect('db2')
#c = conn.cursor()
#c.execute('SELECT * FROM mac')
#rows = c.fetchall()
idmac = 0
idkino = 0               
cost = 0
komzkz = 0     
@bot.message_handler(commands=['start'])
def cmd_start(message):
        markup = types.ReplyKeyboardMarkup()
        itembtn1 = types.KeyboardButton('мак')
        itembtn2 = types.KeyboardButton('кино')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "выбери:", reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def vbr(message):
        def mak():
            conn = sqlite3.connect('db2')
            c = conn.cursor()
            c.execute('SELECT * FROM mac')
            rows = c.fetchall()
            cost = rows[1][2]
            komzkz = rows[idmac][1]
            c.close()
            print(cost)
            print(komzkz) 
            markup = types.ReplyKeyboardMarkup() 
            itembtn1 = types.KeyboardButton('оплатил')
            markup.add(itembtn1)
            koment = 'rekvizity_qiwi: +7(123)4567890' + ' koment_zakaza: ' + komzkz  
            bot.send_message(message.chat.id, koment, reply_markup=markup)
        def kino():
            conn = sqlite3.connect('db2')
            c = conn.cursor()
            c.execute('SELECT * FROM kino')
            rows = c.fetchall()
            cost = rows[1][2]
            komzkz = rows[idkino][1]
            print(cost)
            print(komzkz)
            markup = types.ReplyKeyboardMarkup() 
            itembtn1 = types.KeyboardButton('оплатил')
            markup.add(itembtn1)
            koment = 'rekvizity_qiwi: +7(123)4567890' + ' koment_zakaza: ' + komzkz  
            bot.send_message(message.chat.id, koment, reply_markup=markup) 
        def oplata():
            url = 'https://edge.qiwi.com/payment-history/v2/persons/nomer/payments?rows=1'
            headers = {
                    'Accept' : 'application/json',
                    'Content-Type' : 'application/json',
                    'Authorization' : 'Bearer id'
            }
            r = requests.get(url, headers = headers)
            r.raise_for_status() # do not create the result file until json is parsed
            data = r.json()
            sm = int(data['data'][0]['sum']['amount'])
            kom = data['data'][0]['comment']
            k = message.message_id
            if (sm == cost and kom == komzkz):
                
                bot.send_message(message.chat.id, 'красава держи ништяк')
                 
        if message.text == 'мак':
            global idmac
            idmac = idmac + 1
            mak()
        elif message.text == 'кино':
            global idkino
            idkino = idkino + 1
            kino()
        elif message.text == 'оплатил':
            oplata()

bot.polling(none_stop=True, interval=0)
        
        

