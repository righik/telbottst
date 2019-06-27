#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pprint import pprint #нахне нужен, удобно чекать джисон
import requests
import json
import cherrypy


WEBHOOK_HOST = 'you_ip'
WEBHOOK_PORT = 8443  #все остальные из под рута
WEBHOOK_LISTEN = 'you_ip'

url1 = 'https://edge.qiwi.com/payment-notifier/v1/hooks?hookType=1&param=http%3A%2F%2Fecho.fjfalcon.ru%2F&txnType=2'

headers1 = {
	 'accept' : '*/*',
	 'authorization' : 'Bearer you_token'
}

r = requests.put(url1, headers = headers1)
data = r.json() 
data2 = json.dumps(data)
hkId = data['hookId']
print (hkId)
url2 = 'https://edge.qiwi.com/payment-notifier/v1/hooks/' + hkId + '/key'

kl = requests.get(url2, headers = headers1)
print (kl)
data = kl.json()
kb = data['key']
print (kb)

class Root(object):
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def index(self):
        data = cherrypy.request.json

pprint (data)

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
})

cherrypy.quickstart(Root())




