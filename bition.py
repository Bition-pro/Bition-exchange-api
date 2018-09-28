#!-*-coding:utf-8 -*-
import requests
import json
import time
import hashlib

api_key = 'xxxxxxx'
secret_key = 'xxxxxxx'
symbol = 'ethbtc'
period = '30'  #k-line period

def GetSign(sign_str):
	sign = hashlib.md5()
	sign.update(sign_str.encode("utf-8"))
	return sign.hexdigest()	

def GetRecords(period):
	payload = {'symbol':symbol,'period':period}
	return requests.get('https://openapi.bition.pro/exchange-open-api/open/api/get_records',params=payload).json()['data']

def GetTicker():
	payload = {'symbol':symbol}
	return requests.get('https://openapi.bition.pro/exchange-open-api/open/api/get_ticker',params=payload).json()['data']

def GetDepth():
	payload = {'symbol':symbol,'type':'step0'}
	return requests.get('https://openapi.bition.pro/exchange-open-api/open/api/market_dept',params=payload).json()['data']

def GetAccount():
	timestamp = str(int(time.time()))
	sign_str = 'api_key'+api_key+'time'+timestamp+secret_key
	signed = GetSign(sign_str)
	payload = {'api_key':api_key,'time':timestamp,'sign':signed}
	return requests.get('https://openapi.bition.pro/exchange-open-api/open/api/user/account',params=payload).json()['data']

def GetOrders():
	timestamp = str(int(time.time()))
	sign_str = 'api_key'+api_key+'pageSize'+'100'+'symbol'+symbol+'time'+timestamp+secret_key
	signed = GetSign(sign_str)	
	payload = {'symbol':symbol,'pageSize':100,'api_key':api_key,'time':timestamp,'sign':signed}
	return requests.get('https://openapi.bition.pro/exchange-open-api/open/api/new_order',params=payload).json()['data']

def GetMarket():
	return requests.get('https://openapi.bition.pro/exchange-open-api/open/api/market').json()['data']

#---post-------------------------------------------------

def CreateOrder(side,price,amount):
	timestamp = str(int(time.time()))
	price = str(price)
	amount = str(amount)
	sign_str = 'api_key'+api_key+'price'+price+'side'+side+'symbol'+symbol+'time'+timestamp+'type'+'1'+'volume'+amount+secret_key
	signed = GetSign(sign_str)	
	payload = {'side':side,'type':1,'volume':amount,'price':price,'symbol':symbol,'api_key':api_key,'time':timestamp,'sign':signed}
	return requests.post('https://openapi.bition.pro/exchange-open-api/open/api/create_order',params=payload).json()['data']

def CancelOrder(order_id):
	timestamp = str(int(time.time()))
	order_id = str(order_id)
	sign_str = 'api_key'+api_key+'order_id'+order_id+'symbol'+symbol+'time'+timestamp+secret_key
	signed = GetSign(sign_str)	
	payload = {'order_id':order_id,'symbol':symbol,'api_key':api_key,'time':timestamp,'sign':signed}
	return requests.post('https://openapi.bition.pro/exchange-open-api/open/api/cancel_order',params=payload).json()['data']


