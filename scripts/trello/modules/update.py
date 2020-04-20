import requests, vars, get

def Checklists(name, type, idcard):
    Clist = get.Checklists(name, idcard)
    Equipment = {
'Oder': ({"name":"Budget preparation.","pos":"top","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Budget approval.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Bill invoice.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Bill for approval.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Bill payment.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Delivery of equipment to the department.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token}),
'esxi': ({"name":"Configure Edge Router","pos":"top","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Ubiquiti AP setup","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Switch configuration","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Configure VMware Server","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Configure Backup Server","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Workstation preparation","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Delivery of equipment to the warehouse.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token}),
'proxmox': ({"name":"Configure Edge Router","pos":"top",   "checked":"false","key":vars.Key,"token":vars.Token},
            {"name":"Ubiquiti AP setup","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
            {"name":"Configure Proxmox Server","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
            {"name":"Workstation preparation","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
            {"name":"Delivery of equipment to the warehouse.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token}),
'none': ({"name":"Configure Edge Router","pos":"top",   "checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Ubiquiti AP setup","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Workstation preparation","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token},
         {"name":"Delivery of equipment to the warehouse.","pos":"bottom","checked":"false","key":vars.Key,"token":vars.Token})}
    OderUrl = f"https://api.trello.com/1/checklists/{Clist[0]}/checkItems"
    PreparationSBurl = f"https://api.trello.com/1/checklists/{Clist[1]}/checkItems"
    for row in Equipment['Oder']:
        requests.request("POST", OderUrl, params=row)
    if type == 'esxi':
        for row in Equipment['esxi']:
            requests.request("POST", PreparationSBurl, params=row)
    elif type == 'proxmox':
        for row in Equipment['proxmox']:
            requests.request("POST", PreparationSBurl, params=row)
    elif type == 'none':
        for row in Equipment['none']:
            requests.request("POST", PreparationSBurl, params=row)


def Members(idcard):
    url = f"https://api.trello.com/1/cards/{idcard}/idMembers"
    members = (vars.user0, vars.user1, vars.user2)
    for member in members:
        query = {"key":vars.Key,"token":vars.Token,
                 'value': member}
        requests.request("POST", url, params=query)
