class Restaurant():
    """模拟餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print(self.restaurant_name + " restaurant is opening!")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't roll back the number.")

    def increment_number_served(self, increse_num):
        if increse_num >= 0:
            self.number_served += increse_num
        else:
            print("You can't roll back the number.")

    def read_number_served(self):
        print("There have been " + str(self.number_served) + " people eating in the restaurant!")


my_restaurant = Restaurant("KFC", 'COOK')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(2)
my_restaurant.increment_number_served(-5)
my_restaurant.read_number_served()
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='icecream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=[]

    def show_flavors(self):
        for flavor in self.flavors:
            print("-"+flavor.title())
a=IceCreamStand('ASDA')
a.flavors=['csa','scasd','scsd']
a.show_flavors()