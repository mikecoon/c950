import csv
from Package import Package
from hashmap import HashMap
from utils import set_location
from greedy import *

#Read in package data
with open('csv_files/package.csv') as f:
    packageData = csv.reader(f, delimiter=',')
    next(packageData)

    hm = HashMap()
    truck_1 = []
    truck_2 = []
    truck_3= []

    for package in packageData:
        id = int(package[0])
        address = package[1]
        city = package[2]
        state = package[3]
        zip = int(package[4])
        deadline = package[5]
        weight = int(package[6])
        notes = package[7]
        start = ''
        location = ''
        status = 'At hub'

        #create instance of a package
        p = Package(id, address, city, state, zip, deadline, weight, notes, start, location, status)

        #Package with wrong address put in truck 3 to allow time for address change
        if 'Wrong' in notes:
            p.start = ['11:00:00']
            truck_3.append(p)

        #First trucks packages
        if deadline != 'EOD':
            if 'Must' in notes or len(notes) == 0:
                p.start = ['8:00:00']
                truck_1.append(p)
        
        #Second trucks packages
        if 'Delayed' in notes or 'Can only' in notes:
            p.start = ['9:10:00']
            truck_2.append(p)
        
        #Evenly distibute remaining packages across trucks 2 and 3
        if p not in truck_1 and p not in truck_2 and p not in truck_3:
            if len(truck_2) < len(truck_3):
                p.start = ['9:10:00']
                truck_2.append(p)
            else:
                p.start = ['11:00:00']
                truck_3.append(p)

        #store package in a hashmap
        hm.insert(id, p)
    
    #Set package starting locations
    set_location(truck_1)
    set_location(truck_2)
    set_location(truck_3)

    '''#Sort packages in optimal order
    optimized_route(truck_1, 1, 0)
    optimized_route(truck_2, 1, 0)
    optimized_route(truck_3, 1, 0)'''
