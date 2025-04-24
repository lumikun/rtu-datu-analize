import requests
import bs4



def main():
    url = "https://www.ss.lv/lv/transport/cars/bmw"
    response = requests.get(url)
    if response.status_code == 200:
        print("200: OK!")
        data = bs4.BeautifulSoup(response.text, "html.parser")
        data = data.find(class_="body")
        print(data.prettify())
    else:
        print(f"Status: {response.status_code} Failed.")
        
if __name__ == "__main__":
    main()