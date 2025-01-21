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
import os
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
while i < len(ticks):
    if len(ticks[i]) > 5 or len(ticks[i]) == 0: # quick and dirty way of filtering out non-tickers
        # print(ticks[i] + " " + str(i))
        del ticks[i]
    else:
        i+=1
ParseListToTxt('./help/ML-Training/tickers.txt', ticks)





