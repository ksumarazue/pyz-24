class UpperExample():
    pass

class Example(UpperExample):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Jestem obiektem, a moje imie to: {self.name}'
    def __eq__(self, other): # __repr__
        if isinstance(other, Example):
            return self.name == other.name
        return f'Jestem obiektem, a moje imie to: {self.name}'


obj_ex = Example('kubek')
print(obj_ex)

print(obj_ex.__class__.__name__)
if obj_ex.__class__.__name__ == 'Exmple':
    print('Prawda!')


# number = 3.0
# print(isinstance(number, float))

print(isinstance(obj_ex, int))