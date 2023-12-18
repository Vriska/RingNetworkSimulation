import copy
serviceTime = [3,6,4,5,2]
arrivalTime = [0,2,4,6,8]
ID = [i for i in range(0, len(serviceTime))]
d = []
for i in range(0,len(serviceTime)) :
    d.append([arrivalTime[i],serviceTime[i]])
data = dict(list(zip(ID,d)))
print(data)
factor = 2
def scheduler(data,factor):
    n = 0
    k = 0
    responseratio = 0
    maxresponse = 0
    scheduled = 0
    complete={}
    active={}
    while len(complete) != len(serviceTime) :
        if k<= (len(data)-1):
            while n >= data[k][0]:
                active.update(copy.deepcopy({k:data[k]}))
                k = k+1
                if k==(len(data)) :
                    break
        if len(active) != 0:
            keys = list(active.keys())
            #print(keys)
            for g in keys:
                responseratio = ((n -data[g][0])*factor + data[g][1])/data[g][1]
                if responseratio > maxresponse :
                    maxresponse = responseratio
                    scheduled = g
                #print(responseratio)
            maxresponse=0
            print("Scheduled process ID: " +str(scheduled))
            active[scheduled][1] = active[scheduled][1] - 1
            #if len(data[scheduled]) ==2:
               #data[scheduled].append(n)
            if active[scheduled][1] == 0:
                data[scheduled].append(n+1 - data[scheduled][0])
                complete.update({scheduled:data[scheduled]})
                active.pop(scheduled)
        print(data)
        print("active : " + str(active))
        n=n+1
        print("current step " + str(n))

    averageTN =  sum([complete[x][2] for x in range(0,len(complete))])/len(complete)
    print("Our avg turn around time: " + str(averageTN))
    averageWTN= sum([complete[x][2]/complete[x][1] for x in range(0,len(complete))])/len(complete)
    print("Our avg weighted turn around time is: " +str(averageWTN))
    print("Processes in format - ID: [arrival time, service time, turnaround time]")
    return(complete)

print(scheduler(data,factor))

