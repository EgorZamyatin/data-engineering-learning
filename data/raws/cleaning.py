import pandas as pd
import kagglehub

file_download = kagglehub.dataset_download('sidtwr/videogames-sales-dataset')

try:
    df = pd.read_csv(r'C:\Users\1\.cache\kagglehub\datasets\sidtwr\videogames-sales-dataset\versions\1\Video_Games_Sales_as_at_22_Dec_2016.csv')
except:
    raise FileNotFoundError("Файл не открылся")

initial = len(df)
df = df.drop_duplicates()
print(f"Удалено дубликатов: {initial - len(df)}")


print(df.isnull().sum())
df = df.dropna(subset=["Name", "Publisher", "Developer"])
print(df.isnull().sum())



df["Year_of_Release"] = df["Year_of_Release"].astype("Int64")
