import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import datetime
from Helper import *
import yfinance as yf
import re
from WebScraper import *
'''
Scripts to help with setup, testing, and stuff. I will comment these out as I go
'''
url = 'https://stockanalysis.com/stocks/sector/technology/'
attr = 'href'
filter = '/stocks/'


ws = WebScraper(url,attr,filter)
ticks = []
ws.scrapeToList(ticks)
i = 0
end = len(ticks)
while i < end :
    stock = yf.Ticker(ticks[i])
    try:
        tmp = stock.info
    except:
        del ticks[i]
        end-=1
        continue
    i+=1
print(ticks)
#clean these tickers and helper file




