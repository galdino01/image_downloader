import requests
import pandas as pd

usecols = ['Slug', 'Image Filename', 'Image URL']

data = pd.read_csv("data/images.csv", index_col="Slug", usecols=usecols)

list_dicts = []
dict_links = {}

for index, row in data.iterrows():
    img_data = requests.get(row["Image URL"]).content
    with open('data/images/'+row["Image Filename"], 'wb') as handler:
        handler.write(img_data)