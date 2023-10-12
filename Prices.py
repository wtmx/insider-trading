# Add the real time stock data and a moving average to each row in the csv file
import Sells
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import datetime,date,timedelta

startTime = datetime.now()

# Sells.getSells() # uncomment to refresh csv file
df = pd.read_csv('Insider2.csv', index_col = 0)

infoDict = {}
numperiods = 180

def getinfo(ticker,n = 180):
    yf.pdr_override()
    try:
        tickerdf = pdr.get_data_yahoo(ticker,start = datetime.today() - timedelta(300), end = datetime.today())
        currentprice = tickerdf.iloc[-1]["Close"]
        MA = pd.Series(tickerdf["Close"].rolling(n,min_periods=0).mean(), name = 'MA')
        currentma = MA[-1]
        return (currentprice, currentma)
    except:
        return('na','na')
    

def getPrice(row):
    ticker = row['Symbol']
    if ticker not in infoDict.keys():
        tickerinfo = getinfo(ticker,numperiods)
        infoDict[ticker] = {}
        infoDict[ticker]["price"] = tickerinfo[0]
        infoDict[ticker]["ma"] = tickerinfo[1]
        return infoDict[ticker]["price"]
    else:
        return infoDict[ticker]["price"]

def getMovingAverage(row):
    ticker = row['Symbol']
    return infoDict[ticker]["ma"]



df['currentprice'] = df.apply (lambda row: getPrice(row), axis = 1)
df['movingaverage'] = df.apply (lambda row: getMovingAverage(row), axis = 1)
df.to_csv('InsiderPrices.csv')
print(f'Prices Gathered - Execution Time: {datetime.now() - startTime}')