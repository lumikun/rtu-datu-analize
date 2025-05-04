import requests
import bs4
import pandas as pd


max = int(round(2857/40,0))
all_items = [["name", "price",  "description"]]
for lpp in range(1, 17):
    url = f"https://www.ikea.lv/lv/products/dzivojama-istaba/divani?&product-room=product&page={lpp}&order=RECOMMENDED"
    #url = "https://www.ikea.lv/lv/page/familyItems"
    #url = "https://www.ikea.lv/lv/vairak-neka-tikai-laba-cena"
    print(f"loading in from page {lpp}")

    response = requests.get(url)
    if response.status_code == 200:
        data = bs4.BeautifulSoup(response.text, "html.parser")
        it_block = data.find_all(class_="itemBlock")
        cc = data.find_all(class_="card")

        for info in it_block:
            info = info.find(class_="card-body")
            # Name
            try:
                name = info.find("h3").string
            except:
                continue
            # price
            price = 0
            try:
                price_part = info.find(class_="itemPriceBox")
                price = float(price_part.find("span").attrs["data-price"])
            except:
                price = price_part.find(class_="itemFamilyPrice").find("span")
                price = float(price.attrs["data-pricefamily"])
            # description
            description = info.find(class_="itemFacts").string
            all_items.append([name, price, description])
print("All done!")
items = pd.DataFrame(all_items[1:], columns=all_items[0])
with pd.ExcelWriter("ikea_items_2.xlsx") as file:
    items.to_excel(file, sheet_name="Sheet1", index=False)
print("Written to excel!")