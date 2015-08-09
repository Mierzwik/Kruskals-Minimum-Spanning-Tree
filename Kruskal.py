from unionfind import *
from re import split
from pprint import pprint
from math import floor
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
    #Create disjoined forests
    cities = init(cities)
    for edge in range(len(data)):     
        path = data.pop(0)
        # Since this is bi-directional, popping the next element
        # gets rid of the extra one we have.
        #data.pop(0)
        if cities[str(path[0])] == None:
            union(cities, str(path[0]),str(path[1]))
    return cities,distance

data,cities = setup()
result,distance = kruskal(data,cities)
pprint(result)
print("Distance of minimum spanning tree: " + str(distance))





