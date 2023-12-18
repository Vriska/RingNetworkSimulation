import numpy as np
import copy
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def NodeComparison(n) : ### n is total number of nodes
    def NodeInitializer() :
        node = {}
        i = 0
        for i in range(0,n):
            node[i] = [0,0]
        return node

    def GaussianInts(numb):
        mean = n/2
        lis = []
        for i in range(0,numb):
            s = np.random.normal(mean, 0.5*mean)
            s = int(abs(s)) % n
            lis.append(s)
        return lis

    nodes = NodeInitializer()
    InitialRequestToend = GaussianInts(50)
    for num in InitialRequestToend:
        nodes[num] = [1,0]
    def RingToken():
        RingNodes = copy.deepcopy(nodes)
        for i in range(0,n):
            if RingNodes[i][0] == 1:
                for j in range(0,n):
                    if RingNodes[j][0]==1:
                        RingNodes[j][1]= RingNodes[j][1] + 1
                RingNodes[i][0]= 0
                k = random.randint(0,20)
                l = GaussianInts(k)
                for num in l :
                    if RingNodes[num][0]==0 :
                        RingNodes[num] = [1,0]
        return RingNodes
    def RandomToken() :
        RandomNodes = copy.deepcopy(nodes)
        l = []
        for i in range(0,n) :
            l.append(i)
        random.shuffle(l)
        for i in l :
            if RandomNodes[i][0] == 1:
                for j in range(0,n):
                    if RandomNodes[j][0]==1:
                        RandomNodes[j][1]= RandomNodes[j][1]+1
                RandomNodes[i][0] =0
                k = random.randint(0,20)
                l = GaussianInts(k)
                for num in l:
                    if RandomNodes[num][0]==0:
                        RandomNodes[num]= [1,0]
        return RandomNodes

    def AvgWaitTime(nodes) :
        dsum = 0
        for key in nodes:
            dsum = dsum + nodes[key][1]
        return dsum/len(nodes)
    return[AvgWaitTime(RingToken()),AvgWaitTime(RandomToken())]

size= []
diff = []

for n in range(0,150):
    g = NodeComparison(250 + 5*n)
    size.append(500+50*n)
    diff.append(g[0]-g[1])

print(size)
print(diff)

plt.scatter(size,diff,c="blue")
plt.xlabel("Number of Nodes")
plt.ylabel("Average Wait Time of (Non random nodes-  random nodes)")
plt.show()
