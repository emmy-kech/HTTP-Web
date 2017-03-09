from urllib.request import urlopen
import json
def find_country_ISOcodes():
	API_url="http://ws.postcoder.com/pcw/PCW9J-6Q5RS-N76M8-7YCPJ/country"
	request=urlopen(API_url)
	figure=request.read().decode("utf")
	json_object=json.loads(figure)
	print(json.dumps(json_object))
find_country_ISOcodes()