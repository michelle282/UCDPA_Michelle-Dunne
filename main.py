import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import requests

#Retrieve Data from online APIs
# API Call to Rapid API  and requesting information to be retrieved
response = requests.get("https://live-metal-prices.p.rapidapi.com/v1/latest/XAU,XAG,PA,PL,GBP,EUR/EUR/gram",
 headers={
   "X-RapidAPI-Host": "live-metal-prices.p.rapidapi.com",
   "X-RapidAPI-Key": "4ff3f73e88msh1c3bb96a95c429ep19a33djsn0b0556f92e2a"
   }
)

unit_request = response
unit_data = unit_request.json()

#Retrieving Data from an API that looks at Gold Prices
print(unit_data['baseCurrency'])
print(unit_data['unit'])
print(unit_data['rates'])


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

#Generate Charts using Matplotlib
#Subsetting Rows - Plot Top 5 Teams in 2020 Total Salary Expenditure
PLFF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
DFF3=PLFF[(PLFF.Year>2019) & (PLFF.Points>60)]

DFF3.plot(x ='Team', y='PoundsSpentPerPoint', kind = 'bar', color = 'green')
plt.xlabel("Team", fontsize = 14, color="blue")
plt.xticks(rotation=0)
plt.ylabel("Pounds Spent Per Point to nearest Million", fontsize = 12, color="blue")
plt.title('2020 Top 5 Teams - Expenditure per Point', fontsize = 12, color="blue")
#plt.show()

#Subsetting Rows - Plot Top 5 Teams in 2019 Total Salary Expenditure
PLFF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
DFF4=PLFF[(PLFF.Year==2019) & (PLFF.Points>68)]

DFF4.plot(x ='Team', y='PoundsSpentPerPoint', kind = 'bar', color = 'blue')
plt.xlabel("Team", fontsize = 14, color="blue")
plt.xticks(rotation=0, color="red")
plt.ylabel("Pounds Spent Per Point to nearest Million", fontsize = 12, color="blue")
plt.title('2019 Top 5 Teams - Expenditure per Point', fontsize = 12, color="blue")
#plt.show()

#Group by Year and Suming TotalSalarys
print(PLFF.groupby('Year')['Est. Total Salary'].sum())
df1 = PLFF.groupby('Year')['Est. Total Salary'].sum()
df1.plot(kind='bar',x='Year',y='Est. Total Salary',color='navy')
plt.xticks(rotation=0, color="blue")
plt.xlabel('Season 2017 - 2020', color="purple", fontsize=14)
plt.ylabel('Total Salary Spent per Season to nearest Billion', color="purple")
plt.title('Total Salary Spend Year on Year', fontsize = 14, color="purple")
#plt.show()

PLFF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
DFF5=PLFF[(PLFF.Year>2019) & (PLFF.Points>40)]

DFF5.plot(x ='Team', y='Avg Salary per player', kind = 'bar', color = 'purple', fontsize=8)
plt.xlabel("Team", fontsize = 14, color="blue")
plt.xticks(rotation=90)
plt.ylabel("Avg Salary per player to nearest million", fontsize = 12, color="blue")
plt.title('2020 Avg Salary per Player', fontsize = 14, color="blue")
#plt.show()
