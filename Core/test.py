import csv
with open("test.csv", 'w', newline="") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Id", "Cool"])
