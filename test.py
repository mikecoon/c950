from load_trucks import *
from distances import *
from greedy import *
from utils import *


x, y ,z = optimized_route(truck_1,0,[], [0]),optimized_route(truck_2,0,[], [0]), optimized_route(truck_3,0,[], [0])

print(get_total_distance(x[0],x[1]))
print(get_total_distance(y[0],y[1]))
print(get_total_distance(z[0],z[1]))