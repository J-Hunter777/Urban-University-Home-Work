# Локальное, встроенное и глобальное пространство имен
from sqlite3.dbapi2 import paramstyle

print("_____________________________________________")
print("Локальные и глобальное пространство имен")
print()
def printer():
    global a, b
    a = 'Str'
    b = 'Str2'
    c = 15
    d = 20
    print(a, b, '- global')
    print(c, d, '- local')
printer()

# Способы вызова функции по умолчанию
print("_____________________________________________")
print("Способы вызова функции по умолчанию")
print()
def print_params(a, b, c):
    print(a, b, c, '- print param')
    print(a + c, '- summa 1 and 3 param')
print_params(1, 2,3)

def print_params(a = 1, b = 2, c = 3):
    print(a, b, c, '- print param')
    print(a + c, '- summa 1 and 3 param')
print_params(7)

def print_params(*, a, b, c):
    print(a, b, c, '- print param')
print_params(a = 1, b = 2, c = 3)

# Параметры по умолчанию внутри функции
print("_____________________________________________")
print("Параметры по умолчению внутри функции")
print()
def def_with_params(a, b):
    print(a + b)
def_with_params(1, 2)
def_with_params(4, 3)

def def_with_params(a = 1, b = 2):
    print(a + b)
def_with_params()
def_with_params(4, 3)

def def_with_params(a, b=2):
    print(a + b)
def_with_params(2)
def_with_params(4, 3)

def def_with_params(a, b=2, c=3):
    print(a + b + c)
def_with_params(1, 2)
def_with_params(4, 3, 5)

def def_with_params(a, b=2, c=[]):
    c.append(a)
    print(c)
def_with_params(3)
def_with_params(3)
def_with_params(3)

def def_with_params(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)
def_with_params(3)
def_with_params(3)
def_with_params(3)

# Распаковка позиционных параметров

print("_____________________________________________")
print("Распаковка позиционных параметров")
print()
def print_params(*args):
    print(args)
print_params(1, 2, 3, 4, 5, 6)

def print_params(*args):
    print(*args)
print_params(1, 2, 3, 4, 5, 6)

def print_params(a, b, c):
    print(a, b, c)
list_ = [1, 2, 3]
print_params(*list_)

def print_params(a, b, c):
    print(a, b, c)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    print(kwargs)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    for key in kwargs:
        print(key)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)

def print_params(a, b, c):
    print(a, b, c)
list_ = [1, 2]
dict_ = {'c': 3}
print_params(*list_, **dict_)

# Произвольное число параметров
print("_____________________________________________")
print("Произвольное число параметров")
print()

def test_func(*params):
    print(params)
test_func()
test_func(1, 2, 3, 4, 5, 6)

def test_func(*params):
    print("Тип: ",type(params))
    print("Аргумент: ", params)
print("Все параметры бдут кортежем")
test_func("Soft", 1, 2, 2.95, "Caramel")

def summator(*values):
    s = 0
    for i in values:
        s += i
    return s
print(summator(1, 2, 3, 4))

def summator(txt, *values):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}'
print(summator("Сумма чисел: ", 1, 2, 3, 4, 5))

def summator(txt, *values, type = " sum"):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s}{type}'
print(summator("Сумма чисел: ", 1, 2, 3, 4, 5, type = " summator"))

def info(**values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
info(name = "Julia", course = "Python")
info(name = "Ivan", course = "Robototehnika")

def info1(**values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
    for key, value in values.items():
        print(key, value)
info1(name = "Julia", course = "Python")

def info(*types, **values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
    for key, value in values.items():
        print(key, value)
    print(types)
info(1, 2, 3, name = "Julia", course = "Python")

def info(value, *types, names_author = "Den", **values):
    print("Тип: ", type(values))
    print("Аргумент: ", values)
    for key, value in values.items():
        print(key, value)
    print(types)
info("Пример использования параметров всеъ типов", 1, 2, 3, names_author = "Den", name = "Julia", course = "Python")

def my_sum(n, *args, txt = "Сумма чисел"):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt + ":", s)
my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 2, 3, 4, 5, txt = "Сумма квадратов")
