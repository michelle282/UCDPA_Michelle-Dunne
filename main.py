import pandas as pd

# Import a CSV File into a Pandas DataFrame
Premier_League_FF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
# print(Premier_League_FF.head())

# Sort DF by Columns - Year and Finishing Position
Premier_League_FF.sort_values(["Year", "Finishing Position"],
                              ascending=[False, True], inplace=True)
print(Premier_League_FF.head())
Premier_League_FF.to_csv('PL_Sorted.csv',index=True)

# Index DF to see first 8 columns for all teams in
Premier_League_FF = pd.read_csv("Premier League - Football and Financial Performance - 2017 - 2020.csv")
Indexed = Premier_League_FF.iloc[:, :8]
print(Indexed)
Indexed.to_csv('IndexedPLFF.csv')

# Get the last entry for each team
Grouped = Premier_League_FF.groupby('Team').last()
# print(Grouped)
# Grouped.to_csv(r'Grouped_PLFF.csv')

# Drop Duplicates on Teams Column
Drop_Duplicates = Premier_League_FF.drop_duplicates(subset=['Team'])
# print(Drop_Duplicates)


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