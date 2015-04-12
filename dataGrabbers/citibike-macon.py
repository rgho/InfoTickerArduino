import requests
import json
import datetime #import timedelta


date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


url ='http://www.citibikenyc.com/stations/json'
r = requests.get(url)
result =  (r.text).encode('ascii', 'ignore')
result = json.loads(result)

executionTime = result['executionTime']
for item in result['stationBeanList']:
	if item['id'] == 437:
		print 'time', executionTime
		print 'station', item['stationName']
		print 'available', item['availableBikes']
