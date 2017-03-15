import csv
import json
import time
import urllib

json_data=open('/Users/tumuluri/Downloads/renthub_train.json').read()

data = json.loads(json_data)

for data_key in data.keys():
    print(data_key)

for listing_id in  data["listing_id"].keys():
    print("listing_id :" + listing_id)
    interest_level = data["interest_level"][listing_id]
    created = data["created"][listing_id]
    price = data["price"][listing_id]
    bedrooms = data["bedrooms"][listing_id]
    longitude = data["longitude"][listing_id]
    latitude = data["latitude"][listing_id]
    bathrooms = data["bathrooms"][listing_id]
    building_id = data["building_id"][listing_id]
    features = data["features"][listing_id] #list
    photos = data["photos"][listing_id] #list
    display_address = data["display_address"][listing_id]
    street_address = data["street_address"][listing_id]



#print(data["listing_id"]["110554"])
#print(data["interest_level"]["110554"])
#print(data["photos"]["110554"][1])
#print(data["features"]["110554"])

#urllib.urlretrieve(data["photos"]["110554"][1], "/Users/tumuluri/Downloads/00000001.jpg")

#photo_url = data["photos"]["110554"][1]

#resource = urllib.urlopen(photo_url)
#output = open("/Users/tumuluri/Downloads/file01","wb")
#output.write(resource.read())
#output.close()