import requests
import bs4

url = "https://www.ikea.lv/lv/products/dzivojama-istaba/divani?&product-room=product&page=2&order=RECOMMENDED"

response = requests.get(url)
if response.status_code == 200:
    data = bs4.BeautifulSoup(response.text, "html.parser")
it_block = data.find_all(class_="itemBlock")
cc = data.find_all(class_="card")
print(len(it_block))
print(len(cc))

all_items = [["name", "price",  "description"]]

for info in it_block:
    info = info.find(class_="card-body")
    print()
    print(info.find(class_="price__integer"))