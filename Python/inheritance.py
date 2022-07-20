
class Car:
    #https://www.programiz.com/python-programming/property
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model
        self._color: str = None

    @property
    def color(self) -> str:
        print ("getting value...")
        return self._color
    
    
    @color.setter
    def color(self, color: str) -> None:
        # Perform some action when setting the color...
        # Insert into database, print to console, whatever.
        print ("setting value...")
        self._color = color

        return None

    @color.deleter
    def color(self):
        # Perform some action when deleting an object...
        # Delete from database, print to console, whatever.
        print("Deleting FR-S' color...")
        del self._color

    def print_info(self) -> None:
        info: str = "Make: {0.make}\nModel: {0.model}\nColor: {0.color}\n"
        print(info.format(self))


# Fully documented example:

class FRS(Car):

    def __init__(self, color: str) -> None:
        super().__init__(make='Scion', model='FR-S')
        self.color: str = color


# No code documentation just minimum required to work:

class IS300(Car):

    def __init__(self, color):
        super().__init__('Lexus', 'IS300')
        self.color = color


# Extra example just because I know we talked about it before.

# Backend of the 'class' shortcut:

# Defining our own __init__ function to put into the class:
def subaru_init(self, color):
    car = Car(make='Subaru', model='Outback')
    self.make = car.make
    self.model = car.model
    self.color = color


# Creating the class:
# Every class automatically inherits from type.
Outback = type('Outback', (Car,), {'__init__': subaru_init})

# ----------------------------------------------------------------------------


Nicky = FRS('Red')
Nicky.print_info()

Alex = IS300('Blue')
Alex.print_info()

Mel = Outback('Gray')
Mel.print_info()

print(Mel.__dict__)

