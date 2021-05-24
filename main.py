import pandas as pd

#Import a CSV File into a Pandas DataFrame
Premier_League_FF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
#print(Premier_League_FF.head())

#Sort DF by Columns - Year and Finishing Position
Premier_League_FF.sort_values(["Year", "Finishing Position"], axis=0,
                 ascending=True, inplace=True)
#print(Premier_League_FF.head())
Premier_League_FF.to_csv('PL_FF1.csv',index=True)

#Index DF to see first 8 columns for all teams in 2017
Indexed = Premier_League_FF.iloc[0:17,0:8]
print(Indexed.head())
