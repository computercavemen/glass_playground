class Car:
    make = "Chevy"
    model = "Impala"
    year = "2021"
    color = "blue"
    license_plate = "d34k34"
    damaged = False
    mileage = 1000
    weight = 500


    def drive(self):
        self.mileage += 1


    def crash(self, othercar):
        if self.weight > othercar.weight: 
            othercar.damaged = True
        elif self.weight < othercar.weight: 
            self.damaged = True
        else: 
            self.damaged = True
            othercar.damaged = True

class Garage_slot:
    car = None


    def is_free(self):
        if self.car == None:
            return True
        else: 
            return False


    def park_car(self, newcar):
        self.car = newcar


    def remove_car(self):
        self.car = None


class Garage:
    slots = [Garage_slot(), Garage_slot(), Garage_slot(), Garage_slot(), Garage_slot()]


    def find_empty_slot(self):
        for x in self.slots: 
            if x.is_free() == True: 
                return x
        return None


my_garage = Garage()

for x in range(6):
    my_slot = my_garage.find_empty_slot()
    if my_slot == None:
        print("Could not find a slot!")
    else: 
        my_car = Car()
        my_slot.park_car(my_car)
        print("Successfully parked car!")

    


