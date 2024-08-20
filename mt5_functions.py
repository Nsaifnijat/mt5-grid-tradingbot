# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:51:24 2022

@author: Nazar PC
"""

import MetaTrader5 as mt
def execute(lot,dist):

    request={
        'action':mt.TRADE_ACTION_DEAL,
        'symbol':'EURUSD',
        'volume':lot,
        'type':mt.ORDER_TYPE_BUY,#or mt.ORDER_TYPE_BUY, for buy
        'price':mt.symbol_info_tick('EURUSD').bid,
        'sl':0.0,#float
        'tp':mt.symbol_info_tick('EURUSD').bid+dist,#float
        'deviation':0,#integer, slippage
        'magic':7629765,#integer, ticket no, or id
        'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
        'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
        
        }
    
    buyOrder=mt.order_send(request)
    
    request={
        'action':mt.TRADE_ACTION_DEAL,
        'symbol':'EURUSD',
        'volume':lot,
        'type':mt.ORDER_TYPE_SELL,#or mt.ORDER_TYPE_BUY, for buy
        'price':mt.symbol_info_tick('EURUSD').ask,
        'sl':0.0,#float
        'tp':mt.symbol_info_tick('EURUSD').ask-dist,#float
        'deviation':0,#integer, slippage
        'magic':7629765,#integer, ticket no, or id
        'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
        'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
        }
    
    sellOrder=mt.order_send(request)

    return buyOrder,sellOrder

def execute2(buyVol,sellVol,buyTP,sellTP,dist):

    request={
        'action':mt.TRADE_ACTION_DEAL,
        'symbol':'EURUSD',
        'volume':buyVol,
        'type':mt.ORDER_TYPE_BUY,#or mt.ORDER_TYPE_BUY, for buy
        'price':mt.symbol_info_tick('EURUSD').bid+dist,
        'sl':0.0,#float
        'tp':buyTP,#float
        'deviation':0,#integer, slippage
        'magic':7629765,#integer, ticket no, or id
        'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
        'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
        
        }
    
    buyOrder=mt.order_send(request)

    request={
        'action':mt.TRADE_ACTION_DEAL,
        'symbol':'EURUSD',
        'volume':sellVol,
        'type':mt.ORDER_TYPE_SELL,#or mt.ORDER_TYPE_BUY, for buy
        'price':mt.symbol_info_tick('EURUSD').ask-dist,
        'sl':0.0,#float
        'tp':sellTP,#float
        'deviation':0,#integer, slippage
        'magic':7629765,#integer, ticket no, or id
        'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
        'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
        }
    
    sellOrder=mt.order_send(request)

    return buyOrder,sellOrder

def buyOnly(buyVol,buyTP,dist):

    request={
        'action':mt.TRADE_ACTION_DEAL,
        'symbol':'EURUSD',
        'volume':buyVol,
        'type':mt.ORDER_TYPE_BUY,#or mt.ORDER_TYPE_BUY, for buy
        'price':mt.symbol_info_tick('EURUSD').bid+dist,
        'sl':0.0,#float
        'tp':buyTP,#float
        'deviation':0,#integer, slippage
        'magic':7629765,#integer, ticket no, or id
        'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
        'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
        
        }
    
    buyOrder=mt.order_send(request)
    return buyOrder

def sellOnly(sellVol,sellTP,dist):

    request={
        'action':mt.TRADE_ACTION_DEAL,
        'symbol':'EURUSD',
        'volume':sellVol,
        'type':mt.ORDER_TYPE_SELL,#or mt.ORDER_TYPE_BUY, for buy
        'price':mt.symbol_info_tick('EURUSD').ask-dist,
        'sl':0.0,#float
        'tp':sellTP,#float
        'deviation':0,#integer, slippage
        'magic':7629765,#integer, ticket no, or id
        'type_time':mt.ORDER_TIME_GTC,#valid until you cancel it
        'type_filling':mt.ORDER_FILLING_IOC,#the max size will be taken if the volume is big
        }
    
    sellOrder=mt.order_send(request)

    return sellOrder


def UpdateTP(ticket,TP):
    request={
        'action':mt.TRADE_ACTION_SLTP,
        'position':ticket,
        'sl':0.0,#float
        'tp':TP,#float
    
        }
    order=mt.order_send(request)
    return order




