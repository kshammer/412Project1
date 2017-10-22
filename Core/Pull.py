import requests, time
import numpy as np


def addToPlayers(matchPlayers):
    for p in matchPlayers:
        if p is not None and p in players:
            for z in matchPlayers:
                if z is not None:
                    players[p].append(z)
        elif p is not None:
            players[p] = []
            for z in matchPlayers:
                if z is not None:
                    players[p].append(z)
#tims 114958061
#kyles 83615933 random match 3506289918
#lobby 1873152
#amin 130643254
#bradon 76854778
steamid = "83615933"
# Amount of matches to pull at a time
amountMatches = 10
#limit is how many
#offset is by how many matches back to start
#holds mmrAverages of each set of matches
mmrAverages = []
players = {}
#the range times amount matches is how many matches it will pull from
for z in range(10):
    print(z)
    #stores match ids of all the players in the set of matches
    matchIds = []
    mmrs = []
    #limit is amount of matches pulled offset is how many matches to start from
    payload = {'limit': amountMatches, 'offset': (z * amountMatches)}
    #get request
    r = requests.get("https://api.opendota.com/api/players/" + steamid + "/matches", payload)
    #gets the matchids of all the matches for the set the player has played in
    for i in range(amountMatches):
        matchIds.append(r.json()[i]['match_id'])
    #sleep to respect opendotas api limiters
    time.sleep(1)

    for i in range(amountMatches):
        #get request for each individual match
        q = requests.get("https://api.opendota.com/api/matches/" + str(matchIds[i]))
        #array of all the players in the matches
        matchPlayers = []
        #goes through all the players
        for p in range(10):
            try:
                #checks to make sure the game was a soloqueue if players account is hidden the party id will show up as None
                if q.json()['players'][9]['party_id'] == 9 or q.json()['players'][9]['party_id'] is None:
                    print(q.json()['players'][p]['account_id'])
                    #adds the players to the array
                    matchPlayers.append(q.json()['players'][p]['account_id'])
                    #if the player is showing their rank adds it to the array
                    if q.json()['players'][p]['solo_competitive_rank'] is not None:
                        mmrs.append(q.json()['players'][p]['solo_competitive_rank'])
            #sometimes random errors will show up with the get request
            except Exception:
                print("Could not parse / caught error")
        #sleep to respect opendota api limiters
        time.sleep(1)
        #adds the players to the dictionary of players
        addToPlayers(matchPlayers)
    #prints list of mmrs from the set of matches
    print(mmrs)
    #sometimes no mmrs are added. 
    if len(mmrs) > 0:
        #calculates the average mmr from the set of matches
        print(np.mean(mmrs))
        #adds it to array of averages
        mmrAverages.append(np.mean(mmrs))
#displays array of mmr averages and the dictionary of players
print(mmrAverages)
print(players)
