import requests

urls = ["https://api.gameofthronesquotes.xyz/v1/random/2", "https://api.gameofthronesquotes.xyz/v1/author/tyrion/3", "https://api.gameofthronesquotes.xyz/v1/author/cersei/2"]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(f"\n'{i["sentence"]}'\n\t -- {i["character"]["name"]}\n\t\t({i["character"]["house"]["name"]})")
        print("-----")
    else:
        print("Something went wrong!")
