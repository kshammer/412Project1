import requests, time
import numpy as np
#tims 114958061
#kyles 83615933 random match 3506289918
#lobby 1873152
#amin 130643254
#bradon 76854778
steamid = "130643254"
amountMatches = 10
#limit is how many
#offset is by how many matches back to start
mmrAverages = []
players = [[]]
for z in range(10):
    print(z)
    matchIds = []
    mmrs = []
    payload = {'limit': amountMatches, 'offset': (z * amountMatches)}
    r = requests.get("https://api.opendota.com/api/players/" + steamid + "/matches", payload)
    for i in range(amountMatches):
        matchIds.append(r.json()[i]['match_id'])
    time.sleep(1)
    for i in range(amountMatches):
        q = requests.get("https://api.opendota.com/api/matches/" + str(matchIds[i]))

        for p in range(10):
            try:
                print(q.json()['players'][p]['account_id'])
                if q.json()['players'][p]['account_id'] is not None and q.json()['players'][p]['account_id'] not in players:
                    
                if q.json()['players'][p]['solo_competitive_rank'] is not None and (q.json()['players'][9]['party_id'] == 9 or q.json()['players'][9]['party_id'] is None):
                    #print(q.json()['players'][p]['solo_competitive_rank'])
                    mmrs.append(q.json()['players'][p]['solo_competitive_rank'])
            except Exception:
                print("Could not parse / caught error")
        time.sleep(1)
    print(mmrs)
    print(np.mean(mmrs))
    mmrAverages.append(np.mean(mmrs))
print(mmrAverages)






