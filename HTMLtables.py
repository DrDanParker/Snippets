# -*- coding: utf-8 -*-
"""############################################################################
###
### HTMLtables
### This file is part of Snippets
### This file was created by Dr Daniel Parker on Sat Feb 24 23:58:07 2018 
###    Twitter: @DrDanParker     GitHub:https://github.com/DrDanParker 
###     
### Copyright (C) 2018 Daniel Parker - All Rights Reserved
### You may use, distribute and modify this code under the terms of MIT Licence
### See LICENSE or go to https://goo.gl/ZFmCuw for full licence details
###
### Based on the following:
###     http://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/
###     
###
############################################################################"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


class HTMLTableParser:
       
        def parse_url(self, url):
            response = requests.get(url)
            tabs = self.parse_html_tables(response.text)
            return tabs 

        
        def parse_page(self,page):
            soup = BeautifulSoup(page, 'html.parser')
            return soup

        
        def parse_html_tables(self, page):
            soup = self.parse_page(page)
            tables = soup.find_all('table')
            tabs = []
            for i in range(0,len(tables)):
                tabs.append(self.parse_html_table(tables[i]))
            return tabs
            
            
        def parse_html_table(self, table):
            ttab = []
            ind = []
            #### Build Table 
            for row in table.find_all('tr'):
                dat = []
                for cell in row.find_all('td'):
                    dat.append(cell.text.strip())
                if len(dat) > 1:
                    ind.append(dat[0])
                    ttab.append(dat[1:])
            
            #col = []
            '''
             # Handle column names if we find them
                th_tags = row.find_all('th') 
                if len(th_tags) > 0 and len(column_names) == 0:
                    for th in th_tags:
                        column_names.append(th.get_text())
            '''
            
            
            #tab = pd.DataFrame(ttab, index=ind, columns=col)
            tab = pd.DataFrame(ttab, index=ind)
            
            return tab
