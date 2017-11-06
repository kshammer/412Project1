from Core.dotadata import dotadata
import csv
import numpy as np
import json
steamid = "83615933"
test = dotadata(steamid, batches=10,batchsize=10)
print("Starting")
test.getData()

print("done and printing out the players dictionary")

cool = list(test.players.keys())
with open("dictionary.text", 'w') as coolFile:
    coolFile.write(json.dumps(test.players))
with open("nodes.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Id", "mmr"])
    for z in cool:
        matches = list(test.players[z].keys())
        try:
            wr.writerow([z, test.players[z]['mmr']])
        except KeyError:
            wr.writerow([z, "0"])
with open('edgelist.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Source", "Target", "Type", "Weight"])
    for i in cool:
        matches = list(test.players[i].keys())
        for m in matches[1:]:
            writer.writerow([i, m, "Undirected", test.players[i][m]])

print("This is the average MMR")
print(np.mean(test.mmrAverages))
