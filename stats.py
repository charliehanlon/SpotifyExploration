from pandas import read_json
import json

# read file
myjsonfile=open('/Users/charliehanlon/Downloads/MyData/StreamingHistory0.json','r')
jsondata=myjsonfile.read()

# Parse
obj=json.loads(jsondata)

print(str(obj['endTime']))
print(str(obj['artistName']))
print(str(obj['trackName']))
print(str(obj['msPlayed']))
