import json 
from urllib.request import urlopen

based = "http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&type=hr"

def check(inp):
  if inp == '':
    return 'y'
  else:
    return inp.lower()

params = '&param='

based_obj = ['PM25', 'PM10', 'O3', 'CO', 'NO2', 'SO2', 'WS', 'WD', 'TEMP', 'RH', 'BP', 'RAIN']

for param in range(len(based_obj)): 
  ask = input(f'Do you want to see {based_obj[param]}? (Y/n): ')
  ask = check(ask)

  if (ask == 'y'):
    if (params == '&param='):
      params = params + based_obj[param]
    else:
      params = params + ',' + based_obj[param]

print('')

started_date = ''
started_time = ''
ended_date = ''
ended_time = ''

while (started_date == ''):
  started_date = input('Enter started date (format YYYY-MM-DD): ')

started_date = '&sdate=' + started_date

while (started_time == ''):
  started_time = input('Enter started time (format HH): ')

started_time = '&stime=' + started_time

while (ended_date == ''):
  ended_date = input('Enter ended date (format YYYY-MM-DD): ')

ended_date = '&sdate=' + ended_date

while(ended_time == ''):
  ended_time = input('Enter ended time (format HH): ')

ended_time = '&stime=' + ended_time

link = based + params + started_date + ended_date + started_time + ended_time

obj = json.load(urlopen(link))

# for k, v in obj.items():
  