from unionfind import *
from pprint import pprint
import operator

def setup():
    #Get information from file
    theFile = open('city-pairs.txt')
    rawData = theFile.read()
    theFile.close()
    
    #Split data string into list
    rawData = rawData.split('\n')
    rawData = filter(bool,rawData)
    
    cities = list()

    #Create and return sorted data in list
    data = list()
    for line in rawData:
        item = list()
        temp = line.split()
        item.extend([temp[0],temp[1],int(temp[2])])
        cities.extend([temp[0],temp[1]])
        data.append(item)

    return sorted(data, key=operator.itemgetter(2)),sorted(set(cities))

# Method to perform Kruskal's Algorithm    
def kruskal(data,cities):
    distance = 0
    result = list()
    cities = init(cities)
    for edge in range(len(data)):
        path = data.pop(0)
        #If the two cities in the path do not have the same
        #canonical representative, join them together, then 
        #add path to result and calculate distance
        if find(cities,path[0]) != find(cities,path[1]):
            union(cities, path[0],path[1])
            result.extend((path[0] + ' -> ' + path[1], '(' + str(path[2]) + ' miles)'))
            distance += path[2]
    return result,distance

data,cities = setup()
result,distance = kruskal(data,cities)
pprint(result)
print("Distance of minimum spanning tree: " + str(distance))





