# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def set_serial(self, ism):
#         self.fist_name = ism
#
#     def get_serial(self):
#         return self.last_name
#
#     set_serial()

class TaxiCar:
    def __init__(self, name, year, price_per_day, num_plate):
        self.name = name
        self.year = year
        self.num_plate = num_plate
        self.price_per_day = price_per_day
        self.is_rented = False


class Driver:
    def __init__(self, first_name, last_name, license_id, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.license_id = license_id
        self.username = username
        self.password = password
        self.rented_cars = []


class Taxopark:
    def __init__(self):
        self.balance = 0
        self.username = "admin"
        self.password = 8086
        self.cars = []
        self.drivers = []

    def view_cars(self):
        count = 0
        for car in self.cars:
            count += 1
            if not self.cars:
                print("There is no car to view")
            else:
                print("=== Cars ===")
                print(f' {count}. Name: {car.name} \n    Year: {car.year} \n    Number plate: {car.num_plate} \n    Price: {car.price_per_day}EURO')

    def add_car(self):
        print("=== Adding car ===")
        name = input('Enter car name: ')
        year = input('Enter car year: ')
        num_plate = input('Enter car plate number: ')
        price_per_day = input('Enter car price per day: ')

        car = TaxiCar(name, year, price_per_day, num_plate)
        self.cars.append(car)
        print("Car added")

    def del_car(self):
        count = 0
        for car in self.cars:
            count += 1
            if not self.cars:
                print("There is no car")
            else:
                print("=== Deleting car ===")
                print(f' {count}. Name: {car.name} \n    Year: {car.year}')
        index = int(input('Enter car index: '))
        self.cars.pop(index-1)
        print("Car removed")

    def add_driver(self):
        print("=== Adding driver ===")
        fist_name = input('Enter driver first name: ')
        last_name = input('Enter driver last name: ')
        license_id = input('Enter driver license_id: ')
        username = input('Enter driver username: ')
        password = int(input('Enter driver password: '))
        driver = Driver(fist_name, last_name, license_id, username, password)
        self.drivers.append(driver)

    def del_driver(self):
        count = 0
        for driver in self.drivers:
            count += 1
            if not self.drivers:
                print("There is no driver")
            else:
                print("=== Deleting driver ===")
                print(f' {count}. Name: {driver.name} \n    Year: {driver.year}')
        index = int(input('Enter driver index: '))
        self.drivers.pop(index-1)
        print("Driver removed")


    def view_drivers(self):
        count = 0
        for driver in self.drivers:
            count += 1
            if not self.drivers:
                print("There is no driver in taxopark")
            else:
                print("=== Drivers ===")
                print(f' {count}. Fistname: {driver.first_name} \n    Lastname: {driver.last_name}\n    License number: {driver.license_id}')

    def give_car(self):
        print("=== Give car ===")
        count = 0
        for car in self.cars:
            count += 1
            if not self.cars:
                print("There is no car to view")
            else:
                print(f' {count}. Name: {car.name} \n    Year: {car.year} \n    Number plate: {car.num_plate} \n    Price: {car.price_per_day}EURO')

        index = int(input('Enter car index that you want to give: '))
        count2 = 0
        for driver in self.drivers:
            count2 += 1
            if not self.drivers:
                print("There is no driver in taxopark")
            else:
                print("=== Drivers ===")
                print(f' {count2}. Fistname: {driver.first_name} \n    Lastname: {driver.last_name}\n    License number: {driver.license_id}')

        index2 = int(input('Enter driver index that you want to give: '))
        self.drivers[index2-1].rented_cars.append(self.cars[index-1])
        self.cars[index-1].is_rented = True
        self.cars.pop(index-1)
        print("Driver rented")

    def take_car(self):
        print("=== Take car ===")

        if not self.drivers:
            print("There is no driver in taxopark")
            return
        count = 1
        for driver in self.drivers:
            print(f"{count}. {driver.first_name} {driver.last_name} | License: {driver.license_id}")
            count += 1

        driver_index = int(input("Enter driver index to take car from: "))

        if driver_index < 1 or driver_index > len(self.drivers):
            print("Invalid driver index")
            return

        driver = self.drivers[driver_index - 1]

        if not driver.rented_cars:
            print("Driver has no rented cars")
            return
        count = 1
        for car in driver.rented_cars:
            print(f"{count}. {car.name} | Plate: {car.num_plate} | Year: {car.year}")
            count += 1

        car_index = int(input("Enter car index to return: "))

        if car_index < 1 or car_index > len(driver.rented_cars):
            print("Invalid car index")
            return
        car = driver.rented_cars.pop(car_index - 1)
        car.is_rented = False
        self.cars.append(car)

        print(f"Car '{car.name}' returned to taxopark")

    def view_rented_cars(self):
        print("=== All rented cars ===")

        found = False

        for driver in self.drivers:
            if driver.rented_cars:
                found = True
                print(f"\n  Driver: {driver.first_name} {driver.last_name}")
                for car in driver.rented_cars:
                    print(f"  {car.name} | Year: {car.year} | Plate: {car.num_plate}")

        if not found:
            print("No rented cars in the taxopark")
    def edit_driver(self):
        print("=== Edit driver ===")
        count = 0
        for driver in self.drivers:
            count += 1
            if not self.drivers:
                print("There is no driver in taxopark")
            else:
                print("=== Drivers ===")
                print(f' {count}. Fistname: {driver.first_name} \n    Lastname: {driver.last_name}\n    License number: {driver.license_id}')
            index = int(input('Enter driver index that you want to edit: '))
            new_firs_name = input("Enter new driver name: ")
            new_last_name = input("Enter new driver last name: ")
            new_license_id = input("Enter your new license id: ")
            new_username = input("Enter new username: ")
            new_password = int(input("Enter new password: "))
            self.drivers[index-1].first_name = new_firs_name
            self.drivers[index-1].last_name = new_last_name
            self.drivers[index-1].license_id = new_license_id
            self.drivers[index-1].username = new_username
            self.drivers[index-1].password = new_password



def park_manager(p: Taxopark):
    while True:
        username = input('Enter username: ')
        password = int(input('Enter password: '))
        if p.username == username and p.password == password:
            print("=== Welcome to ADMMIN PANEL ===")
            kod = int(input(" 1. Add car \n 2. Delete car \n 3. View cars \n 4. Add Driver \n 5. Delete Driver \n 6. View Drivers' details \n 7. Giving car to the Driver \n 8. Taking car from the Driver \n 9. View rented cars \n 10. Exit \n Choose => "))
            if kod == 1:
                p.add_car()
            elif kod == 2:
                p.del_car()
            elif kod == 3:
                p.view_cars()
            elif kod == 4:
                p.add_driver()
            elif kod == 5:
                p.del_driver()
            elif kod == 6:
                p.view_drivers()
            elif kod == 7:
                p.give_car()
            elif kod == 8:
                p.take_car()
            elif kod == 9:
                p.view_rented_cars()
            elif kod == 10:
                park_manager(Taxopark())
            elif kod =="":
                print("Write a command")
            else:
                print("Wrong command!!!")
        else:
            for item in p.drivers:
                if item.username == username and item.password == password:
                    print("=== Welcome to DRIVER PANEL ===")
                    kod = int(input(" 1. View available cars \n 2. Edit your data \n 3. Exit \n Choose => "))
                    if kod == 1:
                        p.view_cars()
                    elif kod == 2:
                        p.edit_driver()
                    elif kod == 3:
                        break
                    else:
                        print("Wrong command!!!")
            print("Wrong PCommand")


park_manager(Taxopark())

