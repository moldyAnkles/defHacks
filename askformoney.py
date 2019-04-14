import requests

def ask_for_money():
    headers = {
        "Authorization": "Bearer e7675dd3-ff3b-434b-95aa-70251cc3784b_88140dd4-f13e-4ce3-8322-6eaf2ee9a2d2",
        

    }

    response = requests.post('https://api.evenfinancial.com/leads/rateTables',headers)
    print(response.text)

ask_for_money()
