import sys
import heapq

def vote(n, roadmap, processingtime, station):
    #create a set to store vertices without duplication
    vertex = set()
    for k in roadmap.keys():
        vertex.update([str(k[0])+'g',str(k[0])+'o',str(k[0])+'r'])
        vertex.update([str(k[1])+'g',str(k[1])+'o',str(k[1])+'r'])
    #convert vertex set into a list
    vertex = list(vertex)
    #create a dictionary to store the processing time
    graph = {u: {} for u in vertex}
    #set the respective processing time 
    for i in range(1,n+1):
        graph[str(i)+'g'][str(i)+'o'] = processingtime[i][1]
        graph[str(i)+'o'][str(i)+'g'] = processingtime[i][1]
        graph[str(i)+'o'][str(i)+'r'] = processingtime[i][0]
        graph[str(i)+'r'][str(i)+'o'] = processingtime[i][0]
    #store the travelling period between each pair of vertices
    for k, v in roadmap.items():
        if v > 0:
            graph[str(k[0])+'g'][str(k[1])+'g'] = v
            graph[str(k[1])+'g'][str(k[0])+'g'] = v
            graph[str(k[0])+'o'][str(k[1])+'o'] = v
            graph[str(k[1])+'o'][str(k[0])+'o'] = v
        else:
            graph[str(k[0])+'o'][str(k[1])+'g'] = abs(v)
            graph[str(k[0])+'r'][str(k[1])+'o'] = abs(v)
            graph[str(k[1])+'o'][str(k[0])+'g'] = abs(v)
            graph[str(k[1])+'r'][str(k[0])+'o'] = abs(v)
    #mark all vertices as unvisited by initialising the cost for all vertices to be infinite        
    time = {town: float('inf') for town in vertex}
    #create a heap queue
    pq = []
    #create list of vertices with voting station
    votetowns = [str(i)+'g' for i in station]
    #mark the starting vertices by initialising their cost to be zero and add them to the heap queue
    for i in votetowns:
        time[i]=0
        heapq.heappush(pq,(0,i))
    #use Dijkstra's algorithm to find the shortest path    
    while len(pq)>0:
        #pick an unvisited vertex with the smallest time by popping from a heap queue to be the current vertex
        currtime,currtown= heapq.heappop(pq)
        #skip if a shortest path has already been found for current vertex
        if currtime > time[currtown]:
            continue
        #check if there is a shorter path from the current vertex to each neighbour 
        for neighbour,weight in graph[currtown].items():
            temptime = currtime+weight
            if temptime < time[neighbour]:
                #update shortest path for neighbour
                time[neighbour] = temptime
                #add neighbour to the heap queue
                heapq.heappush(pq,(temptime,neighbour))
    #return shortest path for each vertex to the nearest station
    return [time[str(i)+'g'] for i in range(1,n+1)]

n = int(sys.stdin.readline())
roadmap = {}
s = sys.stdin.readline().split()
for t in s:
    u = t.split(':')
    roadmap[int(u[0]), int(u[1])] = int(u[2])
processingtime = [0] * (n + 1)
s = sys.stdin.readline().split()
i = 1
for t in s:
    u = t.split(':')
    processingtime[i] = int(u[0]), int(u[1])
    i += 1
station = [int(t) for t in sys.stdin.readline().split()]
print(' '.join([str(i) for i in vote(n, roadmap, processingtime, station)]))