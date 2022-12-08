from distances import *

truck_1_sorted, truck_2_sorted, truck_3_sorted = [],[],[]
truck_1_sorted_idx, truck_2_sorted_idx, truck_3_sorted_idx = [0], [0], [0]

#O(n^2) runtime
def optimized_route(truck_distances, truck_number, current_location):
    if not len(truck_distances):
        return truck_distances
    next_location = 0
    shortest_distance = 50
    for distance in truck_distances:
        d = int(distance[1])
        if get_current_distance(current_location, d) <= shortest_distance:
            next_location = d
            shortest_distance = get_current_distance(current_location, d)
    for distance in truck_distances:
        d = int(distance[1])
        if get_current_distance(current_location, d) == shortest_distance:
            match truck_number:
                case 1:
                    truck_1_sorted.append(distance)
                    truck_1_sorted_idx.append(d)
                    truck_distances.pop(truck_distances.index(distance))
                    optimized_route(truck_distances, 1, next_location)
                case 2:
                    truck_2_sorted.append(distance)
                    truck_2_sorted_idx.append(d)
                    truck_distances.pop(truck_distances.index(distance))
                    optimized_route(truck_distances, 2, next_location)
                case 3:
                    truck_3_sorted.append(distance)
                    truck_3_sorted_idx.append(d)
                    truck_distances.pop(truck_distances.index(distance))
                    optimized_route(truck_distances, 3, next_location)

#Helper functions
def truck_1_sorted():
    return truck_1_sorted

def truck_1_sorted_idx():
    return truck_1_sorted_idx

def truck_2_sorted():
    return truck_2_sorted

def truck_2_sorted_idx():
    return truck_2_sorted_idx

def truck_3_sorted():
    return truck_3_sorted

def truck_3_sorted_idx():
    return truck_3_sorted_idx
