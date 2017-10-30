import csv

my_dict = {5: [1, 2, 3], "testing": [2]}

cool = list(my_dict.keys())
print(cool)
for k, v in my_dict.items():
    for l in v:
        print(k, l)

# for node list
with open('mycsvfile.csv', 'w', newline="") as w:  # Just use 'w' mode in 3.x
    writer = csv.writer(w)
    for z in cool:
        writer.writerow([z])
#for edge list
with open('edgelisasdfasdt.csv', 'w', newline="") as q:
    write = csv.writer(q)
    for i,e in my_dict.items():
        for y in e:
            write.writerow(([i], [y]))