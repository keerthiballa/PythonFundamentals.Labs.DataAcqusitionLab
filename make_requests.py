import urllib.request
import json
import requests

#response = urllib.request.urlopen(url)
#data = json.loads(response.read().decode())
#print(data)

j=1

for i in range(39):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset="+str(j)+"&limit=1000"
    my_headers = {'Accept':'*/*', 'Accept-Encoding':'gzip,deflate,br', 'Connection':'keep-alive', 'Content-Type': 'application/json','token': 'azIHEAtmyoUhqJMPraoaafDZPfZmXPSF'}

    response = requests.get(url, headers=my_headers)

    data = response.json()
    jsonFile = open("./NOAA_results/locations_"+str(i)+".json","w")
    json.dump(data, jsonFile)
    jsonFile.close()
    j+=1000