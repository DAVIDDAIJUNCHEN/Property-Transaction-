# This file contains Property class #
class Property:
    def __init__(self, sqaure_feet='', num_bedroom='', num_bathroom='', **kwargs):
        self.square_feet = square_feet
        self.num_bedroom = num_bedroom
        self.num_bathroom = num_bathroom
        super().__init__(**kwargs)

    def display(self):
        print("Property details")
        print('==========================================')
        print('Square root: {}'.format(self.square_feet))
        print('Bedrooms: {}'.format(self.num_bedroom))
        print('Bathrooms: {}'.format(self.bathroom))
        print()

    def prompt_init():
        return dict(square_feet=input('Please enter the square feet: '),
                beds = input('Please enter the number of bedrooms: '),
                baths = input('Please enter the number of baths: '))
    
    prompt_init = staticmethod(prompt_init)

