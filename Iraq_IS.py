# First change the json file to csv
import json
import csv

with open('conflict_data_new_lined.json') as json_file:
    whole_information = json.load(json_file)


information_iraq = []
for fatality in whole_information:
    if fatality['country'] == 'Iraq' and fatality['dyad_name'] == 'IS - Civilians':
        information_iraq.append(fatality)

deaths_per_year = {}
for entry in information_iraq:
    if entry['year'] in deaths_per_year.keys():
        year = entry['year']
        deaths_per_year[year][0] += 1 # index0 for fatalities
        deaths_per_year[year][1] += entry['deaths_civilians'] #index1 for death civilians
    else:
        year = entry['year']
        deaths_per_year[year] = [0, 0]
 


with open('IraqIS.csv', 'w', newline='') as file:
    csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(['year', 'fatalities', 'deaths_civilians'])
    for key in deaths_per_year.keys():
        csvwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow([key, deaths_per_year[key][0], deaths_per_year[key][1]])
        

