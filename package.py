class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, notes, start, location, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.start = start
        self.location = location
        self.status = status
    
    def __str__(self):  # overwite print(Package) otherwise it will print object reference 
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.notes)
    
