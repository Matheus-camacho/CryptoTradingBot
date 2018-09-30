#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 14:19:49 2018

@author: matheus
"""


import gdax
import rollingAverages
import pandas as pd
import listGenerator
import time
import priceGetter

results=[]
asks=[]
money=100000;#USD
wallet=0;#
while True:
    askBidList=([],[]);  
    size1=5;
    size2=50;
    gen=listGenerator.listGenerator();
    roll=rollingAverages.rollingAverages(size1,size2);


    productv="BTC-USD";
    getter=priceGetter.priceGetter();
    lastDifference=0;
    for i in range(10000):
        print(".")
        ask=float(getter.getAsk(product));
        bid=float(getter.getBid(product));
        askBidList=gen.updateLists(askBidList,product);
        
        if (i>size2):
            difference=roll.rollingAverageDifference(askBidList[0],i);
        if (i>size2+2):
            
            if (difference-lastDifference<-5):
                #sell
                if(wallet!=0):
                    money+=wallet*bid
                    wallet=0
                    print("selling")
                    print(money)
                    print("--------")
                
                
            elif(difference-lastDifference>5):
                #buy
                    if(money!=0):
                        wallet+=money/ask
                        money=0;                  
                        print("buying")
                        print(money)
                        print("--------")
            lastDifference=difference
            
            print("Difference:"+str(difference))
            print("Ask:"+str(ask))

        asks.append(ask);
        time.sleep(3)
        print("###########"+str(bid*wallet+money)+"##########");
    results.append(bid*wallet+money)
    