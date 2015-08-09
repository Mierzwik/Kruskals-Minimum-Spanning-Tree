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

    #Create and return sorted data in list
    stuff = list()
    for line in rawData:
        item = list()
        temp = line.split()
        item.append(temp[0])
        item.append(temp[1])
        
        item.append(int(temp[2]))
        stuff.append(item)
             
    return sorted(stuff, key=operator.itemgetter(2))

# Method to perform Kruskal's Algorithm    
def kruskal(data):
    tree = []
    pprint(data)
    return tree

stuff = setup()
result = kruskal(stuff)
print(result)
print(type([]))
