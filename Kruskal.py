from unionfind import *
from re import split
from pprint import pprint
import operator

def setup():
    #Get information from file
    theFile = open('city-pairs.txt')
    rawData = theFile.read()
    theFile.close()
    
    #Split data string into list
    rawData = split('\n',rawData)
    rawData = filter(bool,rawData)
    
    cities = list()

    #Create and return sorted data in list
    stuff = list()
    for line in rawData:
        item = list()
        temp = line.split()
        item.append(temp[0])
        item.append(temp[1])
        item.append(int(temp[2]))
        cities.append(temp[0])
        
        stuff.append(item)

    cities = sorted(set(cities))
    return sorted(stuff, key=operator.itemgetter(2)),cities

# Method to perform Kruskal's Algorithm    
def kruskal(data,cities):
    distance = 0
    cities = init(cities)
    it = int(len(data))
    for edge in range(it):
        path = data.pop(0)
        if cities[path[0]] == None:
            union(cities, str(path[1]),str(path[0]))
            distance += path[2]
    return cities,distance

data,cities = setup()
result,distance = kruskal(data,cities)
pprint(result)
print("Distance of minimum spanning tree: " + str(distance))





