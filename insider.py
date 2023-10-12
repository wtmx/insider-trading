from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import pandas as pd

startTime = datetime.now()

chrome_path = "/Users/wilsonteng/Downloads/chrome-mac-arm64/Google Chrome for Testing.app"
chrome_options = Options()
driver = webdriver.Chrome()
url = "https://www.insidearbitrage.com/insider-sales/?desk=yes"
driver.get(url)

tickerlist = []
relationshiplist = []
datelist = []
costlist = []
shareslist = []
sharesheldlist = []

for i in range(2,101):
    tickerpath = f"""//*[@id="sortTableM"]/tbody/tr[{i}]/td[1]""" 
    ticker = driver.find_element("xpath",tickerpath)
    tickerlist.append(ticker.text)

    relationshippath = f"""//*[@id="sortTableM"]/tbody/tr[{i}]/td[4]""" 
    relationship = driver.find_element("xpath",relationshippath)
    relationshiplist.append(relationship.text)

    datepath = f"""//*[@id="sortTableM"]/tbody/tr[{i}]/td[5]""" 
    date = driver.find_element("xpath",datepath)
    datelist.append(date.text)

    costpath = f"""//*[@id="sortTableM"]/tbody/tr[{i}]/td[6]""" 
    cost = driver.find_element("xpath",costpath)
    costlist.append(cost.text)

    sharespath = f"""//*[@id="sortTableM"]/tbody/tr[{i}]/td[7]""" 
    shares = driver.find_element("xpath",sharespath)
    shareslist.append(shares.text)

    sharesheldpath = f"""//*[@id="sortTableM"]/tbody/tr[{i}]/td[9]""" 
    sharesheld = driver.find_element("xpath",sharesheldpath)
    sharesheldlist.append(sharesheld.text)

allinfo = list(zip(tickerlist,relationshiplist,datelist,costlist,shareslist,sharesheldlist))

df = pd.DataFrame(allinfo, columns = ["Ticker", "Position", "Date", "Share Cost", "Shares Sold", "Shares Held"])

df.to_csv('Insider.csv', index=False)

print(f"""Execution Time: {datetime.now() - startTime}""")

while(True):
    pass

# cmd k+z for zen mode