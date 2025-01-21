import yfinance as yf
import pandas as pd
import csv
stock = yf.Ticker('SIRI')
dict = stock.info
tempDf = pd.DataFrame.from_dict(dict,orient='index')
tempDf = tempDf.reset_index()
pd.set_option("display.max_rows", None)


def ParseListToTxt(fileName, data):
    with open(fileName, "w+") as f:
        for item in data:
            f.write(item + "\n")


def ParseListToCsv(fileName, data):
    with open(fileName, "w+") as f:
        writer = csv.writer(f)
        writer.writerow(data)
