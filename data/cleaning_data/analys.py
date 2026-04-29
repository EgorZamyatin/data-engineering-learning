from cleaning import open_file


df = open_file(r'C:\Users\1\.cache\kagglehub\datasets\sidtwr\videogames-sales-dataset\versions\1\Video_Games_Sales_as_at_22_Dec_2016.csv')

print(df.info())
print(df.isnull().sum())
print(df.describe())




