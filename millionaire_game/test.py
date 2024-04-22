class UpperExample():
    pass

class Example(UpperExample):
    """This is example testing class"""
    def __init__(self, name):
        self.name = name

    # def __repr__(self): # __repr__
    #     return f'Jestem obiektem, a moje imie to: {self.name}'

    def __eq__(self, other):
        if isinstance(other, Example):
            return self.name == other.name
        else:
            return False
    def __del__(self):
        pass
        # usun obiekt example
        # usun jego zależności



obj_ex = Example('kubek')
obj_ex2 = Example('kubek')
print(obj_ex)
print(obj_ex2)
print(obj_ex == obj_ex2)

del obj_ex2
print(obj_ex2)
# print(obj_ex)
#
# print(obj_ex.__class__.__name__)
# if obj_ex.__class__.__name__ == 'Exmple':
#     print('Prawda!')

# number = 3.0
# print(isinstance(number, float))

# print(isinstance(obj_ex, int))


