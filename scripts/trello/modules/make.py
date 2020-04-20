import requests, vars

def Checklists(name, idcard):
    card = f"https://api.trello.com/1/cards/{idcard}/checklists"
    Oder = {'key': vars.Key, 'token': vars.Token,
             'name': 'Equipment oder',
             'pos': 'top'}
    Preparation = {'key': vars.Key, 'token': vars.Token,
                   'name': 'Equipment preparation',
                   'pos': 'bottom'}

    requests.request("POST", card, params=Oder)
    requests.request("POST", card, params=Preparation)
