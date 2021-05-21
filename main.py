import pandas as pd

#Import a CSV File into a Pandas DataFrame

nyc_house_prices = pd.read_csv('nyc-rolling-sales.csv')
print(nyc_house_prices.head())
