from Core.dotadata import dotadata
import csv
import numpy as np
steamid = "83615933"
test = dotadata(steamid, batches=10,batchsize=10)
print("Starting")
test.getData()

print("done and printing out the players dictionary")

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
#3159.84613046
