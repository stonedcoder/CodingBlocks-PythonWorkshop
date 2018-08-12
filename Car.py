class Car :
    population = 0
    slogan = "Khushiyon ki chaaabi"

    def _init_(self ,name="Paras ki gaddi"):
    self.name= name
    Car.population +=1

    def start(self ,sound):
    print(sound)

    def set_slogan(self,data):
    Car.slogan = data



    my_car=Car("Naman Ki car ")
    my_car.set_slogan("learning python")


print(my_car.name)



raunaq_sports= Car("My bugaati chiron")
raunaq_sports.set_slogan("too fast")

print(raunaq_sports.name)

my_car.start("vrooomvroom ")

print(my_car.slogan)

print(Car.population)




raj_car = Car()
print(raj_car.name)