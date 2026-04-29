import pandas as pd
import kagglehub
from main import *

file_download = kagglehub.dataset_download('sidtwr/videogames-sales-dataset')

def open_file(path):
    try:
        file = pd.read_csv(path)
        return file
    except:
        raise FileNotFoundError("Файл не открылся")

df = open_file(r'C:\Users\1\.cache\kagglehub\datasets\sidtwr\videogames-sales-dataset\versions\1\Video_Games_Sales_as_at_22_Dec_2016.csv')

initial = len(df)
df = df.drop_duplicates()
print(f"Удалено дубликатов: {initial - len(df)}")


print(f"{df.isnull().sum()} \n")
df = df.dropna(subset=["Name", "Publisher", "Developer"])
print(df.isnull().sum())



df["Year_of_Release"] = df["Year_of_Release"].astype("Int64")
