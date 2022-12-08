from load_trucks import *
from distances import *
from greedy import *
from utils import *

t1 = []
for i in truck_1:
    t1.append(i.ID)
print(t1)
t1o = []
x = optimized_route(truck_1,0,[])
for i in x:
    t1o.append(i.ID)
print(t1o)