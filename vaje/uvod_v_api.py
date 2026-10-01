import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=46.3026&longitude=14.4222&current=temperature_2m&timezone=Europe%2FBerlin&forecast_days=1"

klic = requests.get(url)

klicJSON = klic.json()

print(klicJSON["current"]["temperature_2m"])
