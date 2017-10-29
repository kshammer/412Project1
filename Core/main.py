from Core.dotadata import dotadata
import csv

steamid = "83615933"
test = dotadata(steamid, batches=5,batchsize=5)
print("Starting")
test.getData()
print("done and printing out the players dictionary")
with open("mmrs.csv", 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(test.mmrAverages)
with open('players.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in test.players.items():
        writer.writerow([key, value])