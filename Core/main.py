from Core.dotadata import dotadata
import csv

steamid = "83615933"
test = dotadata(steamid, batches=5,batchsize=5)
print("Starting")
test.getData()

print("done and printing out the players dictionary")

with open("nodes.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile)
    for z in test.mmrAverages:
        wr.writerow([z])
with open('edgelist.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in test.players.items():
        for per in value:
            writer.writerow(([key], [per]))