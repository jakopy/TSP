import timeit
import time
##start = timeit.default_timer()
##start1=time.time()
import csv
import json
import math
from pulp import *

class tspsolve():
    def __init__(self,distancematrix):
        self.distancematrix = distancematrix
        
    def runtsp(self):
        Locations = self.distancematrix.keys()
        distancematrix = self.distancematrix
        rows = Locations
        cols = Locations
  
        prob = LpProblem("TSP", LpMinimize)
        Routes = LpVariable.dicts("Routes",(rows,cols),0,1,LpBinary)
        u = LpVariable.dicts('u',Locations,0,12323456,LpInteger)

        for r in rows:
            for c in cols:
                prob += distancematrix[r][c]*Routes[r][c]
                
        for r in rows:
            for c in cols:
                prob += lpSum(Routes[r][c] for r in rows) <= 1
                prob += lpSum(Routes[r][c] for c in cols) == 1

        n=len(Locations)
        for r in rows:
            for c in cols:
                if r not in Locations[0]:
                    prob+=  u[r]-u[c]+n*Routes[r][c] <= n-1

        Status = prob.solve()
        LpStatus[Status]
          
        ##print the routes with the result
        totaldistance=[]
        TheRoute = []
        for r in rows:
            for c in cols:
                if value(Routes[r][c]) > 0:
                    TheRoute.append(Routes[r][c])
                    totaldistance.append(value(Routes[r][c])*distancematrix[r][c])
        total = 0
        for i in TheRoute:
            print i
        for i in totaldistance:
            total += i
##        return TheRoute
        return 'total minimal distance is: ' +str(total)

##stop = timeit.default_timer()
##
##print stop - start     
##finish1=time.time()
##print finish1 - start1
