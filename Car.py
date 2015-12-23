class Car:
    'This class should simulate a car'

    def __init__(self,model,year):
        self.model = model
        self.year = year


    def displayYear(self):
        print "This car was mmade in %d" % self.year


    def displayCar(self):
        print "This is a year",self.year,self.model

"Now the actual program begins"

nissan = Car("versa",2013)
ford = Car("mustang",1996)

nissan.displayYear()
nissan.displayCar()

ford.displayYear()
ford.displayCar()