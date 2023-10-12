import pandas as pd
from datetime import datetime
import requests

def getSells():
    startTime = datetime.now()

    base_site = 'https://www.insidearbitrage.com/insider-sales/?desk=yes'
    r = requests.get(base_site)

    df = pd.read_html(r.text) # right now it's just a single dataframe trapped in a list
    df = df[0]
    # columns = df.iloc[0] # set the first row as our dataframe columns
    # df.columns = columns
    # df.drop(df.columns[0], axis = 1, inplace = True) # drop the very first index (ie. column) in our columns
    #  inplace true means we don't need to assign dataframe to the same dataframe to overwrite it

    df.to_csv('Insider2.csv')

    print(df)

    print(f'CSV File Created - Execution Time: {datetime.now() - startTime}')