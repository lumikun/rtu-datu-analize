import requests


url = "https://api.gameofthronesquotes.xyz/v1/random"
# JSON = {} un [] kombinācija
# [] - Indexed 
# {} - key:value
response = requests.get(url)
if response.status_code == 200:
    print(response)
    data = response.json()
    print(data["sentence"])
    print(data["character"]["name"])
    print(data["character"]["house"]["name"])
else:
    print("Something went wrong")