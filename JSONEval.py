import json
import time
from collections import defaultdict

json_data = json.load(open("skills.json"))
filtered_json = defaultdict()
filtered_json = []
count = 0
for x in range(len(json_data)):
    for y in range(len(json_data[x])):
        name = json_data[x][y]["Name"]
        date_stamp = json_data[x][y]["DateStamp"]
        if name == "Expected Wait Time":
            if x == 0:
                count += 1
                filtered_json.append(json_data[x][y])
                print(str(count) + " - " + time.strftime("%d %b %Y %H:%M.%S", time.localtime(date_stamp / 1000)))
            elif (x != 0) & (date_stamp != json_data[x-1][y]["DateStamp"]):
                count += 1
                filtered_json.append(json_data[x][y])
                print(str(count) + " - " + time.strftime("%d %b %Y %H:%M.%S", time.localtime(date_stamp/1000)))

      #  print(json_data[x][y])
print("There are {} entries".format(count))
with open('ExpectedWaitTimeOutput_noDuplicates.json', 'w+') as outfile:
    json.dump(filtered_json, outfile, sort_keys=True, indent=4)
