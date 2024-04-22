import json

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



# obj_ex = Example('kubek')
# obj_ex2 = Example('kubek')
# print(obj_ex)
# print(obj_ex2)
# print(obj_ex == obj_ex2)
#
# del obj_ex2
# print(obj_ex2)
# print(obj_ex)
#
# print(obj_ex.__class__.__name__)
# if obj_ex.__class__.__name__ == 'Exmple':
#     print('Prawda!')

# number = 3.0
# print(isinstance(number, float))

# print(isinstance(obj_ex, int))

with open('jsonQuest.json', 'r') as read_json:
    data = json.load(read_json)

print(type(data))
# for id, quest in enumerate(data):
#     print(f'{id} - {quest}')

for id in data:
    print(id)
    print(f"{id['question']} OPTION {id['options']} ANSWER {id['correct_answer']}")
    # print(id['options'])
    # for i in id:
    #     print(type(i))
    #     print(i.keys())
        # print(i[question])
    # print(type(id))

# for id, res in enumerate(self.options):
