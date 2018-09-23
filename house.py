# Create a class named House, a subclass of Property #
from property import Property

class House(Property):
    # valide tuple #
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced_yard = ('yes', 'no')

    def __init__(self, num_stories='', garage='', fenced_yard='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced_yard 
        self.num_stories = num_stories

    def display(self):
        super().display()
        print('House details')
        print('number of stories： {}'.format(self.num_stories))
        print('garage: {}'.format(self.garage))
        print('fenced yard: {}'.format(self.fenced))

    def prompt_init(self):
        parent_init = Property.prompt_init()
        
        fenced = ''
        while fenced.lower() not in valid_fenced_yard:
            input('Does the house have a fenced yard ? ({})'.format(','.join(House.valid_fenced_yard)))
        
        garage = ''
        while garage.lower() not in valid_garage:
            input('What does the garage have ? ({})'.format(','.join(House.valid_garage)))           
        
        num_stories = input('How many stories ?')

        parent_init.upate({'fenced':fenced, 'garage':garage, 'num_stories': num_stories})
    
    prompt_init = staticmethod(prompt_init)












