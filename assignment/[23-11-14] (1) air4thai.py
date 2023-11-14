import json 
import math
from urllib.request import urlopen

slug = ['PM25', 'PM10', 'O3', 'CO', 'NO2', 'SO2', 'WS', 'WD', 'TEMP', 'RH', 'BP', 'RAIN']
slugSlot = [6, 6, 4, 4, 5, 5, 4, 4, 6, 4, 4, 6]

link = 'http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID=70t&param=PM25,PM10,O3,CO,NO2,SO2,WS,WD,TEMP,RH,BP,RAIN&type=hr&sdate=2023-10-01&edate=2023-11-06&stime=00&etime=16'
obj = json.load(urlopen(link))
main_station = obj['stations'][0]['data']

heading = "|    Date & Time    |"

for head in range(len(slug)):
  heading += " " + slug[head] + " |"

print(heading)

for count in range(len(main_station)):
  line = ''
  for slot, value in main_station[count].items():
    if (slot == 'DATETIMEDATA'):
      line += '|' + value + '|'
    else:
      index = slug.index(slot)
      tValue = str(value)

      if (tValue == 'None'):
        tValue = '---'

      if (len(tValue) < slugSlot[index]):
        spacing = slugSlot[index] - len(tValue)
        tempLine = ''

        if ((spacing % 2) != 0):
          front = math.ceil(spacing / 2)
          back = spacing - front

          for f in range(front):
            tempLine += ' '
          
          tempLine += tValue

          for b in range(back):
            tempLine += ' '
        else:
          space = spacing / 2

          for f in range(int(space)):
            tempLine += ' '
          
          tempLine += tValue

          for b in range(int(space)):
            tempLine += ' '
        
        line += tempLine + '|'
      else:
        line += tValue + '|'

  print(line)