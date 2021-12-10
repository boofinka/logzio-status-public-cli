#!/usr/bin/env python

import os
import sys
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
region_dict_json = json.dumps(region_dict, indent=2)

## MENU ##
while keep:
    print(f'\nCurrent global status: {current_status}\n')
    for mi, selection in enumerate(region_list):
        print('{:2}'.format(str(mi + 1) + '.'), selection["name"])
    print('\n{:2}'.format('Q.'), 'Quit')
    user_selection = input('\nPlease select region: ').lower()
    if user_selection == 'q':
            sys.exit('Goodbye.\n')
            keep = False
    if user_selection.isnumeric():
        if 1 <= int(user_selection) <= len(region_list):
            selected_region_components = region_dict[selection["name"]]
            print(f'\n\n\033[4m{selection["name"]}\033[0m:\n')
            for k,v in selected_region_components.items():
                print(f'\033[1m{k}:\033[0m {v}')
            user_selection = input('\nCheck a different region? (y/n) ').lower()
            sys.stdout.write("\033[F") # Cursor up one line
            if user_selection == 'n':
                sys.exit('\nGoodbye.\n')
                keep = False
            else:
                keep=True
    else:
        print('\nPlease select a region from the list below.')
        
