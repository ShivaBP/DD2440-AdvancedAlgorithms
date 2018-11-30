
#import numpy
import time

import sys

import random

import math

#import numpy

X = 0

def main(argv):





    epsilon = 0.2 
    W = [1,2,3,4]
    numWeights = len(W)
    #numVertices = int (input())

    #s = round(1/(epsilon**2))
    
    global totNodes
    global X
    totNodes = 100
    #totNodes = int(input())
    totNodes = int(sys.stdin.readline())

    X = int(totNodes/2)

    
    s = 0
    if(totNodes >= 15000):
        div = 0.0
        s = 200
        X = int(totNodes*div)
    if(totNodes >= 10000):
        div = 0.0005
        s = int(totNodes*div)
        X = int(totNodes*div)
    elif(totNodes >= 5000):
        div = 0.03
        s = int(totNodes*div)
        X = int(totNodes*div)
    elif(totNodes >= 1000):
        div = 0.05
        s = int(totNodes*div)
        X = int(totNodes*div)
    elif(totNodes >= 300):
        div = 0.08
        s = int(totNodes*div)
        X = int(totNodes*div)
    elif(totNodes >= 50):
        div = 0.3
        s = int(totNodes*div)
        X = int(totNodes*div)
    else:
        div = 1
        s = int(totNodes*div)
        X = int(totNodes*div)

    s = 75
    if(s > totNodes):
        s = totNodes
    X = int(100)

    if(totNodes == 0):
        sys.stdout.write("end " + str(0) + "\n")
        sys.stdout.flush()
    #s = int(math.sqrt(totNodes))
    #X = int(math.sqrt(totNodes))

    '''
    if(s < 25):
        s = 25
        if(s > totNodes):
            s = totNodes
    '''
    #print(s)
        
    u = sample(s)
    c = []
    c.append(totNodes)
    for i in range(1, numWeights+1):
    #for i in range(1, 2):
        #sys.stderr.write(str(i) + "\n")
        c.append(approxconnectedcomps(s, u, i))

    #sys.stderr.write(str(c) + "\n")

    
    #c[0] += 1
    for i in range(0, len(c)):
        if(c[i] > 0):
            c[i] -= 1
    
    for i in range(0, len(c)-1):
        c[i] -= c[i+1]
        if(c[i] < 0):
            c[i] = 0

    sys.stderr.write(str(c) + "\n")

    sum = 0
    for i in range(0, len(c)-1):
        sum += (i+1) * c[i]
    #approxMST = totNodes - numWeights + sum
    approxMST = sum

    
    if(approxMST <= 0):
        approxMST = totNodes/2
    
    kattis = True
    if(kattis):
        sys.stdout.write("end " + str(approxMST) + "\n")
        sys.stdout.flush()
    else:
        sys.stdout.write("end1 " + str(approxMST) + "\n")
        sys.stdout.flush()
        MST = calcMST()

        sys.stdout.write("end " + str(MST) + "\n")
        sys.stdout.flush()

totNodes = 0
dict = {}
def approxconnectedcomps(s, u ,maxWeight):

    global dict
    global totNodes
    global X

    wastedbyoverlap = 0
    visitedTot = {}
    b = []
    for i in range(0, s):

        visited = {}
        queue = []

        temp = dict.get(u[i])
        if(temp == None):
            temp = requestVertex(u[i])
            dict[u[i]] = temp

        visited[u[i]] = 1
        
        overlap = False
        #for j in range(0, len(temp[1])):
        j = 0
        while(j < len(temp[1])):
            if(temp[1][j][1] <= maxWeight):
                #sys.stderr.write("added to queue" + str(temp[1][j][0]) + " with len "  + str(temp[1][j][1])+ "\n")
                if(visitedTot.get(temp[1][j][0]) == 1):
                    overlap = True
                    break
                    #sys.stderr.write("overlap first" + "\n")
                queue.append(temp[1][j][0])
            j += 1
        #sys.stderr.write(str(u[i]) + "\n")

        calceledByX = True
        j = 0
        while(j < X+1):
            
        #for j in range(0, X+1):

            if(overlap):
                break
            
            loop = 0
            while(loop < len(queue)):
                if(visited.get(queue[loop]) == 1):
                    queue.pop(loop)
                else:
                    loop += 1

            #sys.stderr.write(str(queue) + "\n")
            #sys.stderr.write(str(visited) + "\n")
                        
            if(len(queue) > 0):
                temp = dict.get(queue[0])
                if(temp == None):
                    temp = requestVertex(queue[0])
                    dict[queue[0]] = temp
                
                visited[queue[0]] = 1
                
                
                #for k in range(0, len(temp[1])):
                k = 0
                while(k < len(temp[1])):
                    if(visited.get(temp[1][k][0]) == None and temp[1][k][1] <= maxWeight):
                        #sys.stderr.write("added to queue" + str(temp[1][k][0]) + " with len "  + str(temp[1][k][1])+ "\n")
                        if(visitedTot.get(temp[1][k][0]) == 1):
                            overlap = True
                            break
                            #sys.stderr.write("overlap second" + "\n")

                        queue.append(temp[1][k][0])
                    k += 1
                queue.pop(0)
            else:
                calceledByX = False
                break

            j += 1
        
        if(calceledByX or overlap):
            b.append(0)
            if(overlap):
                wastedbyoverlap += 1
            #sys.stderr.write(str(calceledByX) + "\n")
            #sys.stderr.write(str(overlap) + "\n")
            #sys.stderr.write("return 0\n")
            #sys.stderr.write("\n")
        else:
            b.append(1)
            #sys.stderr.write("return 1\n")
            #sys.stderr.write("\n")
        
        for key in visited:
            visitedTot[key] = 1
    sum = 0
    for i in range(0, s):
        sum += b[i]
    
    #sum = (totNodes/(s-wastedbyoverlap))* sum
    sum = (totNodes/s)* sum
    return sum

def sample(s):
    u = []
    '''
    for i in range(0, s):
        u.append(i)
    '''
    
    u = []
    for i in range(0, s):  
        #print(i)
        index = 0
        index = random.randint(0,totNodes-1)
        contains = True
        while(contains):
            contains = False
            index = random.randint(0,totNodes-1)
            for j in range(0, len(u)):
                if(u[j] == index):
                    contains = True
                    break
        
        
        u.append(index)
    
    #sys.stderr.write(str(u) + "\n")
    
    return u

def requestVertex(vertex):
    #print(vertex)
    sys.stdout.write(str(int(vertex)) + "\n")
    sys.stdout.flush()
    #sys.stderr.write(str(int(vertex)) + "\n")
    #ans = input()
    ans = sys.stdin.readline()
    ans = ans.split(" ")
    node = [vertex, []]

    
    for i in range(0,int(ans[0])):
        #print(2*i+1 , 2*i+2)
        node[1].append([int(ans[2*i+1]), int(ans[2*i+2])])

    return node

def calcMST():
    global dict

    #Hämta alla (resterande) noder
    for i in range(0, totNodes):
        temp = dict.get(i)
        if(temp == None):
            temp = requestVertex(i)
            dict[i] = temp
    
    visited = {}
    #sys.stderr.write("len " + str(len(visited)) + "\n")
    #time.sleep(100)
    picklist = []
    startnode = 0

    temp = dict.get(startnode)
    visited[startnode] = 1

    for i in range(0, len(temp[1])):
        #if(visited.get(temp[1][i][0]) != 1):
        picklist.append(temp[1][i])

    sum = 0
    for i in range(0, totNodes-1):

        loop = 0
        while(loop < len(picklist)):
            if(visited.get(picklist[loop][0]) == 1):
                picklist.pop(loop)
            else:
                loop += 1

        if(len(picklist) == 0):
            sys.stderr.write("loop: " + str(i) + "of " + str(totNodes) + "\n")
            sys.stderr.write("da fukk " + "\n")



        smallestindex = 0
        for j in range(0, len(picklist)):
            if(picklist[j][1] < picklist[smallestindex][1]):
                smallestindex = j


        sum += picklist[smallestindex][1]

        temp = dict.get(picklist[smallestindex][0])
        visited[picklist[smallestindex][0]] = 1

        for i in range(0, len(temp[1])):
            picklist.append(temp[1][i])

    return sum

if __name__ == "__main__":
    main(sys.argv)