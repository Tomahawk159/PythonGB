class ComplexNumber:
    """Класс для сложения и умножения комплексных чисел"""

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


a = ComplexNumber(1 + 3j)
b = ComplexNumber(2 + 4j)

print(a + b)
print(a * b)
