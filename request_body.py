import requests

url = "https://habr.com/ru/company/tssolution/blog/495280/" # url страницы, на которой мы будем парсить 

headers = {
    "Accept":"*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36" 
} # в этом блоке далее идут хедеры для того, чтобы зайти на сайт

req = requests.get(url, headers=headers)
src = req.text

with open("indexhabr.html", "w") as file:
    file.write(src)