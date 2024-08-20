# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import MetaTrader5 as mt
import time
from mt5_functions import *
mt.initialize()

#replace the below dummy credentials
login = 65544
password='nnnnn'
server='Exness-Server'
mt.login(login,password,server)



#symbol_info=mt.symbol_info("EURJPY")

#from decimal import Decimal

#lastBuyVolume = 0.01
#lastSellVolume = 0.01
volume = 0.05
dist = 0.0003
while True:
    try:
        if not mt.positions_get():
            
            lot = volume
            buyPos,sellPos = execute(lot,dist)
          
        curPrice = mt.positions_get(symbol='EURUSD')[0].price_current
        PreviousBuys = []
        PreviousSells = []
        allOrders = mt.positions_get()
        for order in allOrders:
            #print(order)
            if order.type == 0:
                PreviousBuys.append(order.ticket)
            else:
                PreviousSells.append(order.ticket)
     
        
        if len(PreviousBuys)>0:
            lastBuyPrice = mt.positions_get(ticket =PreviousBuys[-1])[0].price_open
            #if (lastBuyPrice - curPrice) > 0.0003:     this is also true
            if (curPrice-lastBuyPrice) < -0.0006:
                print('inside buy')
               
                volumes = []
               
                sellTickets = []
                allOrders = mt.positions_get()
                for order in allOrders:
                    #print(order)
                    if order.type == 0:
                        volumes.append(order.volume)
                    else:
                        sellTickets.append(order.ticket)
            
               
                buyTP = mt.symbol_info_tick('EURUSD').bid+dist
                sellTP = mt.symbol_info_tick('EURUSD').ask-dist
                buyVol = volume
                sellVol = volume
                if len(sellTickets) > 0:
                    buyPos = buyOnly(buyVol,buyTP,dist)
                    #lastBuyTicket = buyPos.order
                else:
                    buyPos,sellPos = execute2(buyVol,sellVol,buyTP,sellTP,dist)
                    #print('sell vol',sellVol,'buyvol',buyVol,sellTP,buyTP)
                    #lastBuyTicket = buyPos.order
                    #lastSellTicket = sellPos.order
                
                
        costs = []
        volumes = []
        buyTickets = []
        allOrders = mt.positions_get()
        for order in allOrders:
            if order.type == 0:
                costs.append(order.volume*order.price_open)
                volumes.append(order.volume)
                buyTickets.append(order.ticket)
            
       
        averagePrice = sum(costs)
        totalVol = sum(volumes)
        
        buyTP = (averagePrice / totalVol)+dist
        
        for ticket in buyTickets:
            UpdateTP(ticket,buyTP)
        #SELLS
        if len(PreviousSells)>0:
            lastSellPrice = mt.positions_get(ticket =PreviousSells[-1])[0].price_open
            #if (lastSellPrice - curPrice) < -0.0003:   
            if (curPrice-lastSellPrice) > 0.0006:
                print('inside sell')
                volumes = []
                buyTickets = []
                allOrders = mt.positions_get()
                for order in allOrders:
                    if order.type == 1:
                        volumes.append(order.volume)
                    else:
                        buyTickets.append(order.ticket)
                sellTP = mt.symbol_info_tick('EURUSD').bid-dist
                #print('sellTP',sellTP)
                buyTP = mt.symbol_info_tick('EURUSD').ask+dist
                buyVol = volume
                sellVol = volume
                #print('sell vol',sellVol,'buyvol',buyVol,sellTP,buyTP)
                if len(buyTickets)>0:
                    sellPos = sellOnly(sellVol,sellTP,dist)
                    #lastSellTicket = sellPos.order
                else:
                    buyPos,sellPos = execute2(buyVol,sellVol,buyTP,sellTP,dist)
                    #lastBuyTicket = buyPos.order
                    #lastSellTicket = sellPos.order
        costs = []
        volumes = []
        sellTickets = []
        allOrders = mt.positions_get()
        for order in allOrders:
            if order.type == 1:
                costs.append(order.volume*order.price_open)
                volumes.append(order.volume)
                sellTickets.append(order.ticket)
        averagePrice = sum(costs)
        totalVol = sum(volumes)
        #print('volume',volumes)
        #print('costs',costs)
        #print('average price',averagePrice, 'total volume',totalVol)
        sellTP = (averagePrice / totalVol)-dist
        #print('SELLTP',sellTP)
        for ticket in sellTickets:
            UpdateTP(ticket,sellTP)
    except:
        continue
    time.sleep(1)


#buy is 0
#sell is 1
