import pandas as pd
import kagglehub as kh

patch = kh.dataset_download("mohamedhanyyy/video-games")

try:
    file = pd.read_csv(r'C:\Users\1\.cache\kagglehub\datasets\mohamedhanyyy\video-games\versions\1\games.csv')
except:
    raise FileNotFoundError("Файл не открылся")




