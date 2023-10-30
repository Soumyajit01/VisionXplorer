import requests
def simplify(question):
    url="https://newton.vercel.app/api/v2/simplify/"+str(question).replace("/","(over)")
    response = requests.get(url).json()
    return response.get("result")

def derive(question:str):
    url="https://newton.vercel.app/api/v2/derive/"+str(question).replace("/","(over)")
    response = requests.get(url).json()
    return response.get("result")

def integrate(question:str):
    url="https://newton.vercel.app/api/v2/integrate/"+str(question).replace("/","(over)")
    response = requests.get(url).json()
    return response.get("result")