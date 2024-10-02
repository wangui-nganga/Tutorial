# the vehicle ha a capital V
# move is a method



class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def moves(self):
        print('moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla','Model 3')

#print(my_car.make)
#print(my_car.model)
my_car.get_make_model()
my_car.moves()



your_car = Vehicle('Nissan','Probox')
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self,make,model,faa_id):
       super().__init__(make,model) # better tha code in lines 7-9
       self.faa_id = faa_id

    def moves(self):
        print('Flies along..')



class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')


class Golfcart(Vehicle):
    pass

cessna = Airplane('cessna','Skyhawk', 'N-12345')
toyota = Truck('Toyota','Nissan')
golfwagon= Golfcart('Yamaha','GC100')


cessna.get_make_model()
cessna.moves()      
toyota.get_make_model()
toyota.moves()        
golfwagon.get_make_model()
golfwagon.moves()


# polymophisim ability to behave diffrently in responce to the same input messages

print('n\n')

for v in (my_car,your_car,cessna,toyota,golfwagon):
    v.get_make_model()
    v.moves()


        
        
        
        