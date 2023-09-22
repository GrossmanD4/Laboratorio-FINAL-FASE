class Figura:
    
    def __init__(self,lado=0, altura=0, radio=0):
        self.lado = lado
        self.altura = altura
        self.radio = radio
    
class Cuadrado_area(Figura):
    def __init__(self,lado,altura,radio):
        super().__init__(lado,altura,radio)
        
    def mostrar_area(self):
        print(f"El area del cuadrado es: {self.lado**2}")
        
class Circulo_area(Figura):
    def __init__(self,radio,lado,altura):
        super().__init__(radio,lado,altura)
    
    def mostrar_area(self):
        print(f"El area del circulo es: {((self.radio)**2) * 3.14}")
        
class Triangulo_area(Figura):
    def __init__(self,lado,altura,radio):
        super().__init__(lado,altura,radio)

    def mostrar_area(self):
        print(f"El area del triangulo es: {(self.lado * self.altura)/2}")

cuadrado = Cuadrado_area(4,0,0)
cuadrado.mostrar_area()
circulo = Circulo_area(0,0,5)
circulo.mostrar_area()
triangulo = Triangulo_area(8,6,0)
triangulo.mostrar_area()

print(isinstance(cuadrado,Figura))
print(isinstance(cuadrado,Cuadrado_area))

print(isinstance(circulo,Circulo_area))
print(isinstance(circulo,Figura))

print(isinstance(triangulo,Figura))
print(isinstance(triangulo,Triangulo_area))