# Create a class named HouseRental, a subclass of House and Rental #
from house import House
from purchase_rental import Rental

class HouseRental(House, Rental):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


