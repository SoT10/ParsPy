# начинаем парсить web страницы

import requests
from bs4 import BeautifulSoup
import json


with open("indexhabr.html") as file: # request_body.py создает файл с кодом на чтение
    src = file.read()

soup = BeautifulSoup(src, "lxml")

text_habr = soup.find("div", class_ = "tm-comment__body-content tm-comment__body-content_muted")
print(text_habr)

# link_dict = {}                                                      ссылки со статьи
# rep = ["\n", " "] 

# for item in text_habr:
#     index_url = item.get("href")
#     name_url = item.text
#     for item in rep:
#         if item in name_url:
#             name_url = name_url.replace(item, "_")
#     try:
#         if index_url[0] == "/":
#             index_url = "https://habr.com" + index_url
#     except TypeError:
#         pass
#     link_dict[name_url] = index_url

# print(link_dict)

# with open("linkhabr.json", "w") as file:
#     json.dump(link_dict, file, indent=4, ensure_ascii=False)