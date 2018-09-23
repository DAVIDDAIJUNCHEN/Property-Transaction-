# Create a class named Purchase #
class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
 
    def display(self):
        super().display()
        print('Purchase details')
        print('selling price:', price)
        print('estimated taxes:', taxes)

    def prompt_init():
        return dict(price=input('What is the selling price ?'),taxes = input('What are the estimated taxes ?'))
    prompt_init = staticmethod(prompt_init)

# Create a class named Rental #
class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs):
        self.furnish = furnished
        self.utilities = utilities
        self.rent = rent 
        
    def display(self):
        super().display()
        print("Rental details")
        print("rent: {}".foramt(self.rent))
        print("estimated utilies: {}".format(self.utilies))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        return dict(rent = input('What is monthly rent ?'), utilities = input("What are the estimated utilies ?"), furnished = input('Is the property furnished ?'))

    prompt_int = staticmethod(prompt_init)
