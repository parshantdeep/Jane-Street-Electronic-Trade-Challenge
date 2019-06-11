#!/usr/bin/python

# ~~~~~==============   HOW TO RUN   ==============~~~~~
# 1) Configure things in CONFIGURATION section
# 2) Change permissions: chmod +x bot.py
# 3) Run in loop: while true; do ./bot.py; sleep 1; done

from __future__ import print_function

import sys
import socket
import json
import time

# ~~~~~============== CONFIGURATION  ==============~~~~~
# replace REPLACEME with your team name!
team_name="FLASHBOYS"
# This variable dictates whether or not the bot is connecting to the prod
# or test exchange. Be careful with this switch!
test_mode = False

# This setting changes which test exchange is connected to.
# 0 is prod-like
# 1 is slower
# 2 is empty
test_exchange_index=0
prod_exchange_hostname="production"

port=25000 + (test_exchange_index if test_mode else 0)
exchange_hostname = "test-exch-" + team_name if test_mode else prod_exchange_hostname
# ~~~~~============== NETWORKING CODE ==============~~~~~
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((exchange_hostname, port))
    return s.makefile('rw', 1)

def write_to_exchange(exchange, obj):
    json.dump(obj, exchange)
    exchange.write("\n")

def read_from_exchange(exchange):
    return json.loads(exchange.readline())


# ~~~~~============== MAIN LOOP ==============~~~~~
exchange = connect()
     
def main():
    while True:
        x = read_from_exchange(exchange)
        print(x)

def max_demanded_commodity(x, max_demand_sofar, stock_to_sell):
        stock_to_sell = []
        total_demand = 0
        for dictionary in x:
                if 'book' in dictionary:
                        for each_entry in dictionary['buy']:
                                total_demand = total_demand + each_entry[1]
         if total_demand > max_demand_sofar:
           max_demand_sofar = total_demand      
           stock_to_sell.append(dictionary['symbol'])
 return(stock_to_sell)

def max_supply_commodity(x, max_supply_sofar, stock_to_buy):
        stock_to_buy = []
        total_supply = 0
        for dictionary in x:
                if 'book' in dictionary:
                        for each_entry in dictionary['sell']:
                                total_supply = total_supply + each_entry[1]
         if total_suppy > max_supply_sofar:
           max_supply_sofar = total_demand      
           stock_to_buy.append(dictionary['symbol'])
 return(stock_to_buy)
                                        
                                        


if __name__ == "__main__":
  main()
