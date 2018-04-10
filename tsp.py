#!/usr/bin/env python3
import sys
import math
import time
import timeit
BEGIN_CITY = '1'

D = {}
cities = []

def dataloader():
    datafile = open(sys.argv[1], "r")
    if datafile is None:
        print("Error file")
    distances = datafile.readlines()
    for line in distances:
        x = line.split(' ')
        i = str(x[0])
        j = str(x[1])
        d = x[2]
        d = d[0 : (len(d) - 1)]
        D[i,j] = int(d)
        if i not in cities:
            cities.append(i)
        if j not in cities:
            cities.append(j)
    cities.sort()

'''
# process of solving the problem
# city list
# (1) 2 3 4 5 6 7 8 ....................... n...... 1
#  (left_cities)    target_city   (scheduled_cities)
# <------------------------------------------------
'''

def tsp_DP(left, target_city):
    if left:
        #print("# recursive condition, left: ",left, "target_city: ",target_city)
        #print("return value, dist and target: "
        #      ,min((D[last_city, target_city] + tsp_DP(left - set([last_city]), last_city)[0], last_city) for last_city in left))
        return min((D.get((last_city, target_city), math.inf) + tsp_DP(left - set([last_city]), last_city)[0], last_city) for last_city in left)
    else:
        #print("## base conditon, target_city: ",target_city)
        return (D.get((BEGIN_CITY, target_city), math.inf), BEGIN_CITY)


def main():
    #start=time.time()
    dataloader()
    begin_city = BEGIN_CITY
    left_cities = set(cities) - set([BEGIN_CITY])
    best_route = []
    best_dist = 0
    while True:
        #print("@@@@@@@@@@@@@@@@@@@@@@@This is a new loop")
        dist, begin_city = tsp_DP(left_cities, begin_city)
        #print("begin_city: ", begin_city)
        #print("left_cities: ", left_cities)
        #print("distance: ", dist)
        left_cities -= set([begin_city])
        best_route.append(begin_city)
        if(best_dist == 0):
            best_dist = dist
        if left_cities == set():
            break;
    best_route.append(BEGIN_CITY)
    best_route.reverse()
    best_route.append(BEGIN_CITY)
    #end=time.time()
    #time_final=time.time()-start
    #print("Time is: ",time_final)
    print("OPTIMAL TOUR LENGTH: ",best_dist)
    print("TSP TOUR:")
    for x in best_route:
        print(x)

if __name__ == '__main__':
    main()
