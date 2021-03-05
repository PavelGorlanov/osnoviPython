'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.m = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма чисел m1 и m2 равна')
        return f'm = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение чисел m1 и m2 равно')
        return f'm = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'm = {self.a} + {self.b} * i'


m_1 = ComplexNumber(5, -8)
m_2 = ComplexNumber(10, 3)
print(m_1)
print(m_1 + m_2)
print(m_1 * m_2)