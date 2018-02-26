# -*- coding: utf-8 -*-
"""############################################################################
###
### ClassTest
### This file is part of Snippets
### This file was created by Dr Daniel Parker on Sat Feb 24 16:24:46 2018 
###    Twitter: @DrDanParker     GitHub:https://github.com/DrDanParker 
###     
### Copyright (C) Daniel Parker - All Rights Reserved
### You may use, distribute and modify this code under the terms of MIT Licence
### See LICENSE or go to https://goo.gl/ZFmCuw for full licence details
###
### Based on the following:
###     
###     https://www.youtube.com/watch?v=LwOg0b0ZwCM
###
###     Worked example of a class assigned dataand used in function
###
############################################################################"""

from lse_scraper import LSE

class Stock:
    def __init__(self,ticker):
        self.ticker = ticker
        self.url = self.findUrl('Link')
        
    def findUrl(self,utype):
        df = LSE.buildDatabase()
        od = df.loc[self.ticker,utype]
        print(od)
        return od
    


a1 = Stock('SCPA')
