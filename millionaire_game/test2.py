#
# def calc_bonus(func, procentage):
#     salary_list = [2000, 3000, 2000]
#     base = func(salary_list)
#     return base * procentage
#
# def calculate(arr):
#     return sum(arr)
#
#
# def buy_supplies(item):
#     return f"Kupowanie {item}"
#
#
# items = ["napoje", "jedzenie", "dekoracje", "owoce"]
# for item in map(buy_supplies, items):
#     print(item)
#
# # print(calculate([2, 4, 5]))
# # print(calculate([1,2,3]))
# #
# # #alias
# # calc_total = calculate
# #
# # print(calc_total)
# #
# # purchase = [5, 5, 5]
# #
# # to_pay = calc_total(purchase)
# # print(to_pay)
# #
# # salaries = [2000, 3000, 2000,]
# # print(calc_bonus(calculate, 0.5))


# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
# Utwórz funkcję zwracającą tekst
# Utwórz dekorator przyjujący tę funkcję
# Wywołaj funkcję, by sprawdzić, że decorator działa

def uppercase_decorator(fnc):
    def upperText():
        txt = fnc()
        return txt.upper()
    return upperText

@uppercase_decorator
def lowwerText():
    lowText = 'text with lower char'
    return lowText

print(lowwerText())