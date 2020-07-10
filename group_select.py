import heapq


def choose(countryCandidateList, groupSize):
    countrySizeDict = dict([(key, len(val)) for key,val in countryCandidateList.items()])
    countryHeap = [(-value, key) for key, value in countrySizeDict.items()]
    
    groups = []
    while True:
        group = []
        usedCountry = []
        for i in range(groupSize):
            value, country = heapq.heappop(countryHeap)
            try:
                group.append(countryCandidateList[country].pop())
                updatedCountry = (value + 1, country)
            except IndexError:
                del countryCandidateList[country]
            
            usedCountry.append(updatedCountry)
        if len(group) == groupSize:
            groups.append(group)
        
        for country in usedCountry:
            heapq.heappush(countryHeap, country)

        if len(countryCandidateList) < groupSize:
            break
    
    return groups
        
countryCandidateList = {"India" : ["I1", "I2", "I3","I4","I5","I6" ], "China" : ["C1", "C2", "C3"], "Japan" : ["J1", "J3", "J2"]}
groupSize = 3
    
print choose(countryCandidateList, groupSize)