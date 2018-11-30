import sys
import random
from random import randint
import math


epsilon = 0.2 
W = list()
W.append(1)
W.append(2)
W.append(3)
W.append(4)

numWeights = len(W)
numVertices = int (sys.stdin.readline())


def getVertexInfo(vertex):
    
    #print(vertex)
    sys.stdout.write(str(vertex) + "\n")
    sys.stdout.flush()
    kattisInput = list(sys.stdin.readline())
    vertexInfo = list()
    for i in range(0, len(kattisInput) ):
        if (kattisInput[i]== ' ' ):
            i = i+1
        elif(kattisInput[i] =='\n' ):
            i = i+1
        else:
            nei = int (kattisInput[i])
            vertexInfo.append(nei)
            i= i +1
    
    return vertexInfo

def getNeighbours( vertexInfo):
    
    numNeighbors = int ( vertexInfo [0]) 
    neighbors = list()
    pointer = 1
    while(pointer < len(vertexInfo) ):
        index = int (pointer)
        if (index %   2 == 1):
            neighbors.append(int (vertexInfo[index]))
            pointer = pointer + 1
        pointer = pointer + 1 
    return neighbors


def getNeighborWeight (vertexInfo , neighbor ):  
    weight = 0
    for i in range (1, (len(vertexInfo) -1 ) ):
        j = i +1   
        if ( (int(i) % 2 == 1 ) and  (vertexInfo[i] == neighbor) ):
            weight =  vertexInfo[j]
            break 
        else:
            i =  i+2
    return int(weight)

def BFS ( root ,   W , totalVisited):
    visited = list()
    queue = list()
    X = int (0.9 * numVertices)
      
    queue.append(root)
    visited.append(root)
    totalVisited.append(root)   
    while ( len(queue) > 0  and (len(visited) < X) ):     
        popped = queue[0] 
        queue.pop(0)
        info = getVertexInfo(popped)
        neighbours =  getNeighbours(info)
        for neighbor in neighbours:
            if ( (checkVisited(neighbor , visited) == 0)  and (getNeighborWeight(info, neighbor) <= W)):
                queue.append(neighbor)
                visited.append(neighbor)
                totalVisited.append(neighbor)

    return (queue , visited)

def checkVisited(vertex , visited):
    answer = 0
    for index in range(len(visited) ):
        if (visited[index] == vertex):
            answer = 1
            break 
        index = index +1 
    return int(answer)

def checkTotal(vertex , totalVisited):
    answer = 0
    for index in range(len(totalVisited) ):
        if (totalVisited[index] == vertex):
            answer = 1
            break 
        index = index +1 
    return int(answer)

def checkBFSTermination(queue ):
    answer = 0
    if (len(queue) == 0 ):
        answer = 1
    else:
        answer = 0
    return int(answer)


def approxCC (   W):
    totalVisited= list()
    s = 0 
    if (numVertices <= 1000):
        s = int (0.9 * numVertices)
    else:
        s = int ( math.sqrt( numVertices) )
    lastVertexIndex = int (numVertices -1 )
    chosenVertices = random.sample(range(0, lastVertexIndex), s)
    beta = list()
    for i in range(s):
        beta.append(0)

    for i in range(s):   
        #init BFS
        if ( checkTotal(chosenVertices[i] , totalVisited)== 1):
            i = i +1
        else:
            root = chosenVertices[i]
            (queue , visited ) =  BFS( root ,  W , totalVisited)

            if( checkBFSTermination(queue) == 1):          
                beta[i] = 1
            else:      
                beta[i] = 0

    # sum beta values
    sum = 0
    for i in range(s):
        sum = sum + beta[i]
    
    approxCC = (numVertices * sum) /( s)
    return  approxCC

def run():

    #approximate MST
    numConnectedComponents = 0 
    for i in range(0, (numWeights) ):
       
        numConnectedComponents = numConnectedComponents + approxCC( int(W[i]) )
        
    MST = numVertices - 4 + numConnectedComponents

    sys.stdout.write("end " + str(MST) + "\n")

    sys.stdout.flush()   


run()

