import sys
import fileinput
import numpy as np
import random
from random import randint
import math

epsilon = 0.2 
maxIter = int(8/epsilon)
W = {1,2,3,4}
numWeights = len(W)
numVertices = int (input())
vertices = np.zeros(numVertices)
for index in range(numVertices):
    vertices[index] = index

edges = list ()

def getVertexInfo(vertex):
    print(vertex)
    kattisInput = list(input())
    vertexInfo = list()
    for i in range(len(kattisInput)):
        if (kattisInput[i]== ' '):
            i = i+1
        else:
            vertexInfo.append(kattisInput[i])
            edges.append ( {vertex, kattisInput[i]})
            i= i +1
    return vertexInfo

def getDegree (  vertexInfo):
    return vertexInfo[0]

def averageDegree():
    # a random sample of vertices
    r =int (round ((1 / epsilon)*np.sqrt(numVertices)))
    chosenVertices = np.array(random.sample(list(vertices) , r))

    #approximate average degree
    iter= 0
    averageDegree = math.inf 
    while(iter <= maxIter):
        # compute  degree of each sampled vertex
        degrees = np.zeros(r)
        for index in range(r):
            vertexInfo = getVertexInfo(chosenVertices[index])
            degrees[index] = getDegree ( vertexInfo)
        
        #compute average degree of sampled vertices
        current = sum(degrees) / len(degrees)
        if ( current  <  averageDegree ):
            averageDegree = current 
        
        iter = iter +1 
    return averageDegree
        