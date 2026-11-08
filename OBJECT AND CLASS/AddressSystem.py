class Address:
    def __init__(self, city, state):
        self.city = city 
        self.state = state


class Person:
    def __init__(self, name, address):
        self.city = city    
        self.address = address


def show(self):
        print(f'{self.name} lives in {self.address.city}, {self.address.state}')



addr = Address("Jaipur", "Rajasthan")
p = Person("Aman", addr)
p.show()
print(p.address.city)