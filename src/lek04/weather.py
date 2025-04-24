import requests

url = "https://www.7timer.info/bin/astro.php?lon=41.38&lat=2.16&product=astro&output=json"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for i in data["dataseries"]:
        print(f"Direction: {i["wind10m"]["direction"]},\t Speed: {i["wind10m"]["speed"]}m/s,\t Temperature: {i["temp2m"]}C")