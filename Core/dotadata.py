import requests
import time
import numpy as np
import threading


class dotadata:


    def __init__(self, playerID, batches=10, batchsize=10):
        self.id = playerID
        self.batches = batches
        self.batchsize = batchsize
        self.mmrAverages = []
        self.players = {}


    def addToPlayers(self, matchPlayers):
        # loops through all the players

        for p in matchPlayers:
            # checks to see if players has a value and is already in the dictionary
            if p is not None and p in self.players:
                for z in matchPlayers:
                    if z is not None:
                        # adds the list of players to the key
                        self.players[p].append(z)
            elif p is not None:
                # if key does not exist add the key and adds value as an empty list
                self.players[p] = []
                for z in matchPlayers:
                    if z is not None:
                        self.players[p].append(z)


    def getData(self):
        for z in range(self.batches):
            print(str(z) + " THIS IS THE OVERALL Z")
            # stores match ids of all the players in the set of matches
            matchIds = []
            mmrs = []
            # limit is amount of matches pulled offset is how many matches to start from
            payload = {'limit': self.batchsize, 'offset': (z * self.batchsize)}
            # get request
            matchIds = self.getMatches(self.id, payload, self.batchsize)

            for i in range(self.batchsize):
                # get request for each individual match
                #print("Getting match information")
                q = requests.get("https://api.opendota.com/api/matches/" + str(matchIds[i]))
                # array of all the players in the matches
                matchPlayers = []
                # goes through all the players
                for p in range(10):
                    try:
                        # checks to make sure the game was a soloqueue if players account is hidden the party id will show up as None
                        if q.json()['players'][9]['party_id'] == 9 or q.json()['players'][9]['party_id'] is None:
                            #print(q.json()['players'][p]['account_id'])
                            # adds the players to the array
                            matchPlayers.append(q.json()['players'][p]['account_id'])
                            # if the player is showing their rank adds it to the array
                            #print("Checking solo rank")
                            if q.json()['players'][p]['solo_competitive_rank'] is not None:
                                mmrs.append(q.json()['players'][p]['solo_competitive_rank'])
                    # sometimes random errors will show up with the get request
                    except Exception:
                        print("Could not parse / caught error")
                # sleep to respect opendota api limiters
                time.sleep(1)
                # adds the players to the dictionary of players
                #print("adding to players")
                self.addToPlayers(matchPlayers)
                self.getNeighbors(matchPlayers)
            # sometimes no mmrs are added.
            if len(mmrs) > 0:
                # calculates the average mmr from the set of matches
                print(np.mean(mmrs))
                # adds it to array of averages
                self.mmrAverages.append(np.mean(mmrs))
    def getMatches(self, steamID, payload, amountMatches):
        matchIds = []
        time.sleep(1)
        r = requests.get("https://api.opendota.com/api/players/" + str(steamID) + "/matches", payload)
        # gets the matchids of all the matches for the set the player has played in
        if (r.status_code == 200):
            for i in range(amountMatches):
                matchIds.append(r.json()[i]['match_id'])
        else:
            print("bad server request")
        return matchIds

    def getNeighbors(self, matchPlayers):
        size = 3
        for t in matchPlayers:
            submatchIds = []
            for z in range(size):
                print(str(z) + " THIS IS THE NEIGHBORS Z")

                payload = {'limit': size, 'offset': (z * size)}
                mmrs = []

                if t != self.id and t is not None:
                    print(t)
                    submatchIds = self.getMatches(t, payload, size)
                else:
                    continue

                for i in range(size):
                    if len(submatchIds) == 0:
                        continue
                    q = requests.get("https://api.opendota.com/api/matches/" + str(submatchIds[i]))
                    submatchPlayers = []
                    for p in range(10):
                        try:
                            if q.json()['players'][9]['party_id'] == 9 or q.json()['players'][9]['party_id'] is None:
                                #print(q.json()['players'][p]['account_id'])
                                submatchPlayers.append(q.json()['players'][p]['account_id'])
                                if q.json()['players'][p]['solo_competitive_rank'] is not None:
                                    mmrs.append(q.json()['players'][p]['solo_competitive_rank'])
                        except Exception:
                            print("Could not parse / caught error")
                    time.sleep(1)
                    self.addToPlayers(matchPlayers)
                if len(mmrs) > 0:
                    print(np.mean(mmrs))
                    self.mmrAverages.append(np.mean(mmrs))

