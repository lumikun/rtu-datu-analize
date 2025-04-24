import requests
import bs4

url = "https://en.wikipedia.org/wiki/Siberian_Husky"
response = requests.get(url)
if response.status_code == 200:
    print("200: Good!")
    page_content = bs4.BeautifulSoup(response.text, "html.parser")
else:
    print("Something went wrong!")

ret = page_content.find("h2")
print(ret.contents) # All Contents
print(ret.string)   # string only if it's a string
ret = page_content.find_all("h2")
for i in ret:
    print(i)

print("----")
ret = page_content.find(id="History")
print(ret)
print("----")
ret = page_content.find_all(class_="mw-heading")
print(ret)
print(len(ret))
print("----")
#ret = page_content.find_all("li", class_="interlanguage-link")
ret = page_content.find_all("a", class_="interlanguage-link-target")
print(len(ret))


for link in ret:
    #print(link.prettify())
    if link.attrs["lang"] in ["lv", "de", "en-simple"]:
        print(f"{link.attrs['lang']}\t{link.attrs['data-title']}\n{link.attrs["href"]}")
    #print(link.attrs['data-title'])