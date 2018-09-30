#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 13:06:45 2018

@author: matheus
"""
import priceGetter

class listGenerator(object):
    
    def __init__(self):
        super(listGenerator, self).__init__();

        self.getter=priceGetter.priceGetter()
        
    def updateLists(self,priceList,product):   
        askList=priceList[0];
        bidList=priceList[1];
        askList.append(float(self.getter.getAsk(product)));
        bidList.append(float(self.getter.getBid(product)));
        
        return (askList,bidList)
        