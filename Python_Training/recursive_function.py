class Car:
    def open_proceed(self):
        print("Door Opened")
        self._accelerate()
    
    def _accelerate(self):
        print("Throtle Increased")
        self.__engine_performing()

    def __engine_performing(self):
        print("Bursting open")
        print("Car is moving")

my_car = Car()
my_car.open_proceed()