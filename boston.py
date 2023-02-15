#Read json from url and print data
import json
import urllib.request
import urllib.parse
import urllib.error

url = input('https://pollysnips.s3.amazonaws.com/bostonEmployeeSalaries.json')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

