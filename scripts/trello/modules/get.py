import requests, vars


def Members():
    querystring = {"key":vars.Key,"token":vars.Token,
                   'members': 'all'}
    execute = requests.request("GET", vars.BoardGetUrl, params=querystring).json()
    return execute
#r = get.Members()
#for f in r['members']:
#    print(f'{f["fullName"]} => {f["id"]}')


def Cardid(name):
    query = {"key":vars.Key, "token":vars.Token, "cards":"visible"}
    execute = requests.request("GET", vars.BoardGetUrl, params=query).json()
    for row in execute['cards']:
        if row['name'] == name:
            cardID = row['id']
    return cardID


def Checklists(name, idcard):
    card = f"https://api.trello.com/1/cards/{idcard}/idChecklists"
    Oder = {'key': vars.Key, 'token': vars.Token}
    execute = requests.request("GET", card, params=Oder).json()
    return execute
