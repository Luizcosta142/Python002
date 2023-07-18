from math import hypot

# Implementando a Classe

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Apesar de ter implementado quarto dunder methods (além do __init__), nenhum deles é chamado diretamente
# na classe ou no uso típico da classe ilustrado pelas listagens do console

#O código a seguir testa o operador + para fazer a soma de vetores

v1 = Vector(2, 4)
v2 = Vector(2, 1)
v_soma = v1 + v2
print(v_soma)

#Calculando a magnitude de um vetor utilizado a função embutida abs

v = Vector(3, 4)
v_abs = abs(v)
print(v_abs)

#Utilizando o operaodr * para realizar a multiplicação por escalar dos vetores


Multiplicaco_por_escalar = v * 3
print(Multiplicaco_por_escalar)

#e uma magnitude multiplicada

magnitude_multiplicada = abs(v * 3)
print(magnitude_multiplicada)
