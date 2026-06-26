import requests
import json
import csv
import io

# Go to the dataset page, find the JSON/CSV download link, and paste it here:
# url = "https://www.data.gouv.fr/datasets/liste-des-services-de-police-accueillant-du-public-avec-geolocalisation?resource_id=2cb2f356-42b2-4195-a35c-d4e4d986c62b"
url = "https://www.data.gouv.fr/api/1/datasets/r/2cb2f356-42b2-4195-a35c-d4e4d986c62b"

response = requests.get(url)
response.encoding = "utf-8"

csv_file = io.StringIO(response.text)
data = csv.DictReader(csv_file, delimiter=";")

city = input("Quelle ville ?")
jAiTrouve = False
for station in data:
    if(station["commune"] == city):
        print("Trouvé : ",station["service"], "-", station["commune"])
        jAiTrouve = True

if(not jAiTrouve):
    print("je n'ai pas trouvé la station")
