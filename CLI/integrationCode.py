#!/usr/bin/env python

import requests
import json

## VARIABLES ##
region = {}
region_dict = {}
rd = {}
region_list = []
region_componenet_list = []
keep = True

## CODE ##
all_components = requests.get('https://status.logz.io/api/v2/summary.json').text
all_components_json = json.loads(all_components)
all_components_json = json.loads(all_components)["components"]
current_status = json.loads(all_components)["status"]["description"]

for i in all_components_json:
    if i["group"] == True:
        region_list.append(i)
    else:
        pass

for region in region_list:
    rn = region["name"]
    region_componenet_list.append(region["name"])
    for comp in region["components"]:
        for x in all_components_json:
            if comp == x["id"] and x["group"] == False:
                rd[x["name"]] = x["status"]
                region_dict[rn] = rd
