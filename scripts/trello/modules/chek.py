import requests, vars

def Cardid(name):
    query = {"key":vars.Key, "token":vars.Token, "cards":"visible"}
    execute = requests.request("GET", vars.BoardGetUrl, params=query).json()
    for row in execute['cards']:
        if row['name'] == name:
            cardID = 1
            break
        else:
            cardID = 0
    return cardID
