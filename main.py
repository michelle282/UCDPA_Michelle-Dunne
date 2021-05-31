import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

# Import a CSV File into a Pandas DataFrame
Premier_League_FF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
# print(Premier_League_FF.head())

# Sort DF by Columns - Year and Finishing Position
#Premier_League_FF.sort_values(["Year", "Finishing Position"],
                              #ascending=[False, True], inplace=True)
#print(Premier_League_FF.head())
#Premier_League_FF.to_csv('PL_Sorted.csv',index=True)


# Indexing a Dataframe using Indexing Operator
#Indexed_df2 = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv", index_col="Team")
#Salary = Indexed_df2["Est. Total Salary"]
#print(Salary)

# Indexing - retrieving row by loc method
#first = data.loc["Liverpool"]
#second = data.loc["Manchester United"]

#print(first, "\n\n\n", second)

# Get the last entry for each team
Grouped = Premier_League_FF.groupby('Team').last()
# print(Grouped)
# Grouped.to_csv(r'Grouped_PLFF.csv')

# Drop Duplicates on Teams Column
#Dropped_Dup = Premier_League_FF.drop_duplicates(subset=['Team'])
#print(Dropped_Dup)
#Dropped_Dup.to_csv(r'Dropped_PLFF.csv')

#Itterows
#for index, row in Premier_League_FF.iterrows():
    #print(row)

#create dataframe
df_points = pd.DataFrame({
    'Team': ['Arsenal', 'Chelsea', 'Liverpool', 'Manchester City', 'Manchester United'],
	'Points': [75, 93, 76, 78, 69]})

#iterate through each row of dataframe
#for index, row in df_points.iterrows():
    #print(index, ': ', row['Team'], 'has', row['Points'], 'Points.')

#Merge Dataframes - Create 2 DataFrame and Merge
df2020 = {'Team':['Liverpool', 'Manchester City', 'Chelsea', 'Manchester United', 'Leicester City'], 'Year':['2020', '2020', '2020', '2020', '2020'], 'Points':['99', '81', '66', '66', '62'], 'Est Total Salary':['118m', '135m', '138m', '183m', '79m'], 'PoundsSpentPerPoint':['1.19m', '1.69m', '2.1m', '2.77m', '1.28m']}
df1=pd.DataFrame(df2020, columns=['Team', 'Year', 'Points', 'Est Total Salary', 'PoundsSpentPerPoint'])
#print(df1.head())

df2019 = {'Team':['Manchester City', 'Liverpool', 'Chelsea', 'Manchester United', 'Leicester City'], 'Year':['2019', '2019', '2019', '2019', '2019'], 'Points':['98', '97', '72', '66', '52'], 'Est Total Salary':['146m', '115m', '121m', '158m', '75m'], 'PoundsSpentPerPoint':['1.49m', '1.19m', '1.68m', '2.38m', '1.45m']}
df2=pd.DataFrame(df2019, columns=['Team', 'Year', 'Points', 'Est Total Salary', 'PoundsSpentPerPoint'])
#print(df2.head())
Team_Performance=df1.merge(df2, on='Team')
#print(Team_Performance)
#Team_Performance.to_csv(r'Merged_PLFF3.csv')

#Create reusable code using Python Functions


#Create a Numpy Array based on DF Last Entry for Each Team
#Grouped = pd.read_csv("Grouped_PLFF.csv")
#df = pd.DataFrame(Grouped, columns = ['Team','Year','Est. Total Salary'])

#print(df)
#print(type(df))
#my_array = df.to_numpy()

#print(my_array)
#print(type(my_array))
#print(my_array.dtype)
#Access my_array using index value
#data=my_array
#x = data[0,2]
#y = data[5,2]
#print(x,y)


#Creating a Dictionary from Pandas Dataframe in Python for all clubs with over 40 points in 2020
PLFF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
PLFF2=PLFF[(PLFF.Year>2019) & (PLFF.Points>40)]
#print(PLFF2)
my_dictionary=PLFF2.to_dict(orient = 'list')
#print(my_dictionary)


