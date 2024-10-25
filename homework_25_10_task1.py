import math

#Вспомогательная функция, чтобы округлять ответы до 3 значащих цифр
def round_to_3(x):
   return round(x, 2 - math.floor(math.log10(abs(x))))
def print_number(x):
    s = str(round_to_3(x))
    while s[-1] == '.' or s[-1] == '0':
        if s[-1] == '.':
            s = s[:-1:]
            break
        s = s[:-1:]
    return s

class Physical_Quantity:
    def __init__(self, name, measure):
        self.name = name
        self.measure = measure
    def absolute_value(self):
        pass
    def get_absolute_value(self):
        print("Модуль велечины " + self.name + " примерно равен " + print_number(self.absolute_value()) + ' ' + self.measure + ".")
        return

class Vector(Physical_Quantity):
    def __init__(self, name, measure, x_projection, y_projection):
        self.name = name
        self.measure = measure
        self.x = float(x_projection)
        self.y = float(y_projection)
    def absolute_value(self):
        return math.sqrt(self.x**2 + self.y**2)
    def deg_angle(self):
        if self.y < 0:
            return math.degrees(math.atan2(self.y, self.x) + 2*math.pi)
        else:
            return math.degrees(math.atan2(self.y, self.x)) 
    def get_orientation(self):
        print ("Направление " + self.name + " определяется поворотом от оси X на угол примерно " + print_number(self.deg_angle()) + " (в градусах) против часовой стрелки.")

class Scalar(Physical_Quantity):
    def __init__(self, name, measure, value):
        self.name = name
        self.measure = measure
        self.value = float(value)
    def absolute_value(self):
        return abs(self.value)

#Создаём величину А по введённым параметрам
vector = True
n = 4
if input("Введите тип величины (\"скаляр\" или \"вектор\")" + '\n') == "скаляр":
    vector = False
    n = 3
print("Введите параметры величины")
parameters = []
for i in range (n):
    parameters.append(input())

if vector == True:
    A = Vector(*parameters)
    A.get_absolute_value()
    A.get_orientation()
else:
    A = Scalar(*parameters)
    A.get_absolute_value()
    


