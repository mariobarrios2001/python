class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passagers =[]
    
    def add_passager(self, name):
        if not self.open_seats():
            return False                
        self.passagers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passagers)

flight = Flight(3)

print(flight)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.add_passager(person)
    if success:
        print(f"Added {person} to flight successfulluy")
    else:
        print(f"No avaiable seats for {person}")       