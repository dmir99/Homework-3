class Fooditems:
    def __init__(self):
        self.name = "None"
        self.fat = 0.0
        self.carbs = 0.0
        self.protein = 0.0

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        if calories is not None:
            return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


yname = input()
yfat = float(input())
ycarbs = float(input())
yprotein = float(input())
yservings = float(input())

default = Fooditems()
default.name = "None"
default.fat = 0.0
default.carbs = 0.0
default.protein = 0.0
calories = default.get_calories(yservings)
default.print_info()
print("Number of calories for {:.2f} serving(s):".format(yservings), "{:.2f}".format(calories))

print()

custom = Fooditems()
custom.name = yname
custom.fat = yfat
custom.carbs = ycarbs
custom.protein = yprotein
calories = custom.get_calories(yservings)
custom.print_info()
print("Number of calories for {:.2f} serving(s):".format(yservings), "{:.2f}".format(calories))



