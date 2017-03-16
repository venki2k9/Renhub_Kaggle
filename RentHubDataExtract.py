import csv
import json
import time
import urllib
import csv


json_data=open('/Users/tumuluri/Downloads/renthub_train.json').read()

data = json.loads(json_data)

master_feature_set = set()

for data_key in data.keys():
    print(data_key)

for listing_id in  data["listing_id"].keys():
    features = data["features"][listing_id]
    for feature_item in features:
        master_feature_set.add(feature_item)

print(master_feature_set)
print(len(master_feature_set))

training_flat_file = '/Users/tumuluri/Downloads/renthub_train.csv'
field_list =  ["listing_id","interest_level","created","price","bedrooms","longitude","latitude","bathrooms","building_id","display_address","street_address"]

with open(training_flat_file,"w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=field_list)
    writer.writeheader()
csvfile.close()

for listing_id in  data["listing_id"].keys():
    print("listing_id :" + listing_id)
    interest_level = data["interest_level"][listing_id].encode("utf-8")
    created = data["created"][listing_id]
    price = data["price"][listing_id]
    bedrooms = data["bedrooms"][listing_id]
    longitude = data["longitude"][listing_id]
    latitude = data["latitude"][listing_id]
    bathrooms = data["bathrooms"][listing_id]
    building_id = data["building_id"][listing_id]
    features = data["features"][listing_id] #list
    photos = data["photos"][listing_id] #list
    display_address = data["display_address"][listing_id].encode("utf-8")
    street_address = data["street_address"][listing_id].encode("utf-8")

    #wrote the following fields into a csv file.
    with open(training_flat_file,"a") as csvfile:
        write = csv.DictWriter(csvfile,fieldnames=field_list)
        result = {"listing_id": listing_id,
                  "interest_level":interest_level,
                  "created":created,
                  "price":price,
                  "bedrooms":bedrooms,
                  "longitude":longitude,
                  "latitude":latitude,
                  "bathrooms":bathrooms,
                  "building_id":building_id,
                  "display_address":display_address,
                  "street_address":street_address
                  }
        write.writerow(result)
        csvfile.close()

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