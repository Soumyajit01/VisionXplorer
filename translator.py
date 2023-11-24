import requests
from urllib.parse import quote

def translateToHindi(text):   
    def encodeURIComponent(url):
        return quote(url)
    encoded_text = encodeURIComponent(text)
    response = requests.get(f"https://t.song.work/api?text={encoded_text}&from=en&to=hi")
    data = response.json()
    return dict(data)["result"]