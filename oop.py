#  Object Orientated Programming

"""
Class: template for creating objects. All objects created using the same class will have the same
characteristics.
Object: an instance of a class.
Instantiate: Create an instance of a class.
Method: A function defined in a class.
Attribute: A variable bound to an instance of class.
"""


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)
kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make,
                                        kenwood.price,
                                        hamilton.make,
                                        hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)
hamilton.power = 5.5
print(hamilton.power)
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
