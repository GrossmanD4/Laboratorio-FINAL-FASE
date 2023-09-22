# Super Clase
class Material():
    # Método constructor 
    def __init__(self,nombre,numVol):
        # variables de instancia
        self.nombre=nombre
        self.numVol=numVol
    def mostrar(self):
        print(f'Material: {self.nombre}\nVolumen: {self.numVol}')
# Sub Clase
class Libro(Material):
    def __init__(self, nombre, numVol,numLibros):
        super().__init__(nombre, numVol)
        self.numLibros=numLibros
    def mostrar(self):
        print('Libro: ',self.nombre,
              'Volumen: ',self.numVol,
              'Cantidad: ',self.numLibros)
        # print(f'Libro: {self.nombre}\nVolumen: {self.numVol}\nCantidad: {self.numLibros}')
# Sub Clase
class Revista(Material):
    def __init__(self, nombre, numVol, numRevista):
        super().__init__(nombre, numVol)
        self.numRevista=numRevista
    def mostrar(self):
        print(f'Revista: {self.nombre}\nVolumen: {self.numVol}')
        print(f'Cantidad: {self.numRevista}')
# Polimorfismo en una función
def mostrarObejtos(tipo):
    tipo.mostrar()
# instanciamos la SuperClase 'Material' y las SubClases 'Libro y Revista'
hoja=Material('Papiro','1.3 cm^3/g')
libro=Libro('El Silmarillion','1',10)
revista=Revista('el Economista','16',4)

mostrarObejtos(hoja)
mostrarObejtos(revista)
mostrarObejtos(revista)
