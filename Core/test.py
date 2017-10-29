import csv

my_dict = {"test": 1, "testing": 2}

with open('mycsvfile.csv', 'w') as w:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(w, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)