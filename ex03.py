import json 
from urllib.request import urlopen

obj = json.load(urlopen('http://air4thai.pcd.go.th/services/getNewAQI_JSON.php?stationID=70t'))

print('Station: ' + obj['stationID'])
print('Name: ' + obj['nameTH'] + ' (' + obj['nameEN'] + ')')
print('Address: ' + obj['areaTH'] + ' (' + obj['areaEN'] + ')')
print('Lattitude & Longtitude: ' + obj['lat'] + ', ' + obj['long'])
print('')

for k, v in obj['AQILast'].items():
  if k != 'date': 
    if k != 'time':
      if k == 'AQI':
        print(k)
        print(f" Param: {v['param']}")
        print(f" AQI: {v['aqi']}")
      else:
        print(k)
        print(f" AQI: {v['aqi']}")
        print(f" value: {v['value']}")