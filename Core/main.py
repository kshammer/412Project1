from Core.dotadata import dotadata
import csv
import numpy as np
steamid = "83615933"
test = dotadata(steamid, batches=5,batchsize=5)
print("Starting")
test.getData()

print("done and printing out the players dictionary")

cool = list(test.players.keys())
with open("dictionary.text", 'w') as coolFile:
    coolFile.write(test.players)
with open("nodes.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Id"])
    for z in cool:
        wr.writerow([z])
with open('edgelist.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Source", "Target", "Type", "Weight", "mmr"])
    for i in cool:
        matches = list(test.players[i].keys)
        for m in matches:
            writer.writerow([i, m, "Undirected", test.players[i][m], test.players[m]['mmr']])

print(np.mean(test.mmrAverages))
