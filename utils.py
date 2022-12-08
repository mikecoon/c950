import distances
import greedy
import load_trucks

def set_location(truck):
    for package in truck:
        for address in distances.get_address():
            if package.address == address[2]:
                package.location = address[0]

#i need to optimize greedy algo for my package class...
def get_total_distance(truck_list, idx_list):
    total_distance=0
    for idx in range(len(idx_list)): 
        try:
            total_distance = distances.get_distance(int(idx_list[idx]), int(idx_list[idx+1]), total_distance)
            delivery_status = distances.get_time_left(distances.get_current_distance(int(idx_list[idx]), int(idx_list[idx+1])), truck_list[idx].start)
            truck_list[idx].status = str(delivery_status)
            #Updates the package in the hashmap with the new status time
            load_trucks.hm.insert(truck_list[idx].ID, truck_list)
        except IndexError:
            pass

    return total_distance
