# create a pasta cooking app.
# the app should create a least three type of pasta.
# Classes of various pasta must have the folloiwing methods : Type of pasta , Sauce, Topping, Dressing,
# Use  creational patterns for this task

# first create the class Pasta
class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None

    def __str__(self):
        return f'Type: {self.type}, Sauce: {self.sauce}, Topping: {self.topping}, Dressing: {self.dressing}'

# Abstract Builder
class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def build_type(self):
        pass

    def build_sauce(self):
        pass

    def build_topping(self):
        pass

    def build_dressing(self):
        pass

    def get_pasta(self):
        return self.pasta


# Concrete Builders
class SpaghettiBuilder(PastaBuilder):
    def build_type(self):
        self.pasta.type = "Spaghetti"

    def build_sauce(self):
        self.pasta.sauce = "Tomato Sauce"

    def build_topping(self):
        self.pasta.topping = "Parmesan Cheese"

    def build_dressing(self):
        self.pasta.dressing = "Olive Oil"


class PenneBuilder(PastaBuilder):
    def build_type(self):
        self.pasta.type = "Penne"

    def build_sauce(self):
        self.pasta.sauce = "Pesto Sauce"

    def build_topping(self):
        self.pasta.topping = "Pine Nuts"

    def build_dressing(self):
        self.pasta.dressing = "Balsamic Vinaigrette"


# Director
# definimos los metodos
class PastaChef:
    def __init__(self, builder):
        self.builder = builder

    def make_pasta(self):
        self.builder.build_type()
        self.builder.build_sauce()
        self.builder.build_topping()
        self.builder.build_dressing()

    def get_pasta(self):
        return self.builder.get_pasta()


# Client Code
def main():
    spaghetti_builder = SpaghettiBuilder()
    penne_builder = PenneBuilder()

    chef = PastaChef(spaghetti_builder)
    chef.make_pasta()
    spaghetti_pasta = chef.get_pasta()
    print(spaghetti_pasta)

    chef = PastaChef(penne_builder)
    chef.make_pasta()
    penne_pasta = chef.get_pasta()
    print(penne_pasta)


if __name__ == "__main__":
    main()
