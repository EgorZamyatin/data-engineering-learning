import pandas as pd
import oc
import kagglehub

file_download = kagglehub.dataset_download('sidtwr/videogames-sales-dataset')

try:
    df = pd.read_csv(r'C:\Users\1\.cache\kagglehub\datasets\sidtwr\videogames-sales-dataset\versions\1\Video_Games_Sales_as_at_22_Dec_2016.csv')
except:
    raise FileNotFoundError("Файл не открылся")

print(df.info())
print(df.isnull().sum())
print(df.describe())




