class House:
    houses_history = []
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.num_flor = numbers_of_floors

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print (f'{self.name} снесен, но он останется в истории')


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_flor}'

    # def __len__(self):
    #     return self.num_flor
    def __eq__(self, other): # =
        isinstance ( other, int )
        return self.num_flor == other.num_flor
    def __le__(self, other): # <=
        return self.num_flor <= other.num_flor
    def __ne__(self, other): # !=
        return self.num_flor != other.num_flor

    def __ge__(self, other): # >=
        return self.num_flor >= other.num_flor
    def __lt__(self, other): # <
        return self.num_flor < other.num_flor
    def __gt__(self, other): # >
        return self.num_flor > other.num_flor

    def __add__(self, value): # +
        isinstance ( value, House )
        self.num_flor += value
        return self
    def __radd__(self, other):
        isinstance ( other, House )
        return self + other
    def __radd__(self, other):
        isinstance ( other, House )
        return self + other


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов

del h2
del h3


print(House.houses_history)