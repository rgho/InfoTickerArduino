

from bs4 import BeautifulSoup
import requests
import json
import datetime

def unixTimeToStr(unixTime):
	return datetime.datetime.fromtimestamp(int(unixTime)).strftime('%Y-%m-%d %H:%M:%S')


# Set the constants
latlong = '40.7127,-74.0059' #Hard code new york. 
APIkey = ''
url = 'https://api.forecast.io/forecast/%s/%s' % (APIkey, latlong)

#yesterday = datetime.today() - timedelta(days = 1)
#yesterdayStr = yesterday.strftime('%Y-%m-%d') 

# Make request
r = requests.get(url)
response =  (r.text)#.encode('ascii', 'ignore')
response = json.loads(response)
#print response

print response['hourly']['summary']
print '--------------'
for datapoint in response['hourly']['data']:
	print 'time', datapoint['time'], unixTimeToStr(datapoint['time'])
	print 'apparent temp', datapoint['apparentTemperature']
	print 'temp', datapoint['temperature']
	print 'humidity ', datapoint['humidity']
	print 'windspeed ', datapoint['windSpeed']
	print 'rain probability ', datapoint['precipProbability']
	print 'rain intensity ', datapoint['precipIntensity']
	print 'visibility', datapoint['visibility']
	print 'cloud cover ', datapoint['cloudCover']
	print '---------------'




