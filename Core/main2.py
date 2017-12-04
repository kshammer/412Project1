from Core.dotadatasimple import dotadatasimple
import csv
import numpy as np

steamid = "83615933"
test = dotadatasimple(steamid)
test.getData()
cool = list(test.players.keys())
with open("nodes.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile)
    for z in cool:
        wr.writerow([z])
with open('edgelist.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in test.players.items():
        for per in value:
            writer.writerow(([key], [per]))
print(np.mean(test.mmrAverages))