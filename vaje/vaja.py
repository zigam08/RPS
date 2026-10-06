# avto = {
#     "znamka" : "Fiat",
#     "model" : "Grande Punto",
#     "letnik" : "2008"
# }

# print(avto["model"])
# avto["barva"] = "Bela"

# for kljuc, vrednost in avto.items():
#    print(kljuc, "->", vrednost)


# -----------------------------------------------------------


# sola = {
#     "ime": "ŠC Kranj",
#     "naslov": {
#         "ulica": "Kidričeva cesta 55",
#         "posta": 4000,
#         "kraj": "Kranj"
#     },
#     "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
# }

# print(sola["naslov"]["kraj"])   # Kranj
# print(sola["smeri"][0])         # računalništvo
# print(len(sola["smeri"]))       # 3

# #Naloga
# print(sola["naslov"]["posta"])
# print(sola["smeri"][2])

# for vrednost in sola["smeri"]:
#     print(vrednost)


# ----------------------------------------------------------


# import requests

# url = "https://api.open-meteo.com/v1/forecast"
# parametri = {
#     "latitude": 46.29329867361963,
#     "longitude": 14.395127817501294,
#     "current": "temperature_2m,wind_speed_10m"
# }

# odgovor = requests.get(url, params=parametri)

# print(odgovor.status_code)   # 200 pomeni, da je vse v redu
# podatki = odgovor.json()     # JSON pretvorimo v slovar
# print(podatki)


# temperatura = podatki["current"]["temperature_2m"]
# enota = podatki["current_units"]["temperature_2m"]
# print(f"V Preddvoru je trenutno {temperatura} {enota}.")


# veter = podatki["current"]["wind_speed_10m"]
# enota_veter = podatki["current_units"]["wind_speed_10m"]
# print(f"V Preddvoru je trenutno {veter} {enota_veter}.")


# -------------------------------------------------------


# import requests

# def trenutna_temperatura(lat, lon):
#     url = "https://api.open-meteo.com/v1/forecast"
#     parametri = {
#         "latitude": lat,
#         "longitude": lon,
#         "current": "temperature_2m"
#     }
#     odgovor = requests.get(url, params=parametri)
#     podatki = odgovor.json()
#     return podatki["current"]["temperature_2m"]


# kraji = {
#     "Ljubljana": (46.0569, 14.5058),
#     "Maribor": (46.5547, 15.6459),
#     "Mirna Peč": (45.85982945346324, 15.082563472718329)
# }

# temperature = {}

# for ime, (lat, lon) in kraji.items():
#     t = trenutna_temperatura(lat, lon)
#     temperature[ime] = t

# print(temperature)


# ----------------------------------------


temperature = {
    "Ljubljana": 14.2,
    "Maribor": 15.1,
    "Koper": 18.4,
    "Kamnik": 12.9,
    "Kranj": 10.2,
    "Preddvor": 16.3
}

najtoplejse = "Ljubljana"
najvisja = temperature["Ljubljana"]
najnizja = temperature["Ljubljana"]

for mesto, t in temperature.items():
    if t > najvisja:
        najvisja = t
        najtoplejse = mesto

print(f"Najtoplejše: {najtoplejse} ({najvisja} °C)")


vsota = 0
for t in temperature.values():
    vsota = vsota + t

povprecje = vsota / len(temperature)
print(f"Povprečje: {round(povprecje, 1)} °C")

for mesto, t in temperature.items():
    if t < najnizja:
        najnizja = t
        najhladnejse = mesto

print(f"Najhladnejše: {najhladnejse} ({najnizja} °C)")
