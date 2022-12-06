import csv
from package import Package
from hashmap import HashMap

#Read in package data
with open('csv_files/package.csv') as f:
    packageData = csv.reader(f, delimiter=',')
    next(packageData)

    hashmap = HashMap()
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
            truck_3.append(p.ID)

        #First trucks packages
        if deadline != 'EOD':
            if 'Must' in notes or len(notes) == 0:
                truck_1.append(p.ID)
        
        #Second trucks packages
        if 'Delayed' in notes or 'Can only' in notes:
            truck_2.append(p.ID)
        
        #Evenly distibute remaining packages across trucks 2 and 3
        if p not in truck_1 and p not in truck_2 and p not in truck_3:
            if len(truck_2) < len(truck_3):
                truck_2.append(p.ID)
            else:
                truck_3.append(p.ID)

        #store package in a hashmap
        hashmap.insert(id, p)
#truck class
#time it leaves hub, time (deliv time)
#as you deliver, can take them off the truck

    def get_truck_1():
        return truck_1

    def get_truck_2():
        return truck_2
    
    def get_truck_3():
        return truck_3
    
    def get_hashmap():
        return hashmap