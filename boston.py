#Read json from url and print data
#run notebook for graphing .ipynb
import json
import urllib.request
import urllib.parse
import urllib.error

url = "https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
print(type(data))
info = json.loads(data)

js = json.loads(data)
print(type(js))

data = js["data"]
print(type(data))
print(data[0])
#meta = js["meta"]

