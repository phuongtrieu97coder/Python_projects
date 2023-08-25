cars = [
    {'Model':'BMW-34534','Brand':'BMW','Color':'blue'},
    {'Model':'Honda-34534','Brand':'Honda','Color':'white'},
    {'Model':'Ford-34534','Brand':'Ford','Color':'black'}
]
fields = ['Model','Brand','Color']

import csv 

with open('cars.csv','w') as csvFile:
    csvWriter = csv.DictWriter(csvFile,fieldnames=fields)
    csvWriter.writeheader()
    for item in cars:
        csvWriter.writerow(item)