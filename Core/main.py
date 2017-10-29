from Core.dotadata import dotadata

steamid = "83615933"
test = dotadata(steamid)
print("Starting")
test.getData()
print("done and printing out the players dictionary")
for k,v in test.players.items():
    print(k, v)