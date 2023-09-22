#CLASE PERSONA
class Persona:
    def __init__(self,identificación="",nombre="0",apellido="5",prueba="xd"):
        self.ide=identificación
        self.nom=nombre
        self.ape=apellido
        self.pruebadel=prueba

    #Funciónes que obtiene la identificación, el nombre y el apellido de la persona
    def obtener(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont=10
        while cont!=0:
            self.ide=str(input("Ingrese su identificación (solo números): "))
            cont=0
            for x in self.ide:
                if x not in num:
                    cont+=1
                else:
                    if len(self.ide)!=8:
                        cont+=1
        return self.ide
    
    def obtenernom(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont2=20
        while cont2!=0:
            self.nom=str(input("Ingrese su nombre (No se reciben números): "))
            cont2=0
            for x in self.nom:
                if x in num:
                    cont2+=1
        return self.nom

    def obtenerape(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont3=20
        while cont3!=0:
            self.ape=str(input("Ingrese su apellido (No se reciben números): "))
            cont3=0
            for x in self.ape:
                if x in num:
                    cont3+=1
        return self.ape

    def __set__(self):
        if self.ide=="72949694":
            self.ide="12345678"
    
    def __del__(self):
        del(self.pruebadel)



#CLASE ESTUDIANTE
class Estudiante(Persona):
    def __init__(self,identificación,nombre,apellido,semestre=0):
        super().__init__(identificación,nombre,apellido)
        self.sem=semestre
    
    def obtenersem(self):
        while self.sem<=0 or self.sem>=10:
            self.sem=int(input("Ingrese su número de semestre: "))
        return self.sem

    def __str__(self):
        return "Su nombre es: " + str(self.nom) + ", y su apellido: " + str(self.ape) + ", con identificación: " + str(self.ide) + " y semestre: " + str(self.sem)

#CLASE CLIENTE
class Cliente(Persona):
    def __init__(self,identificación,nombre,apellido,dirección="",cod="0",est=""):
        super().__init__(identificación,nombre,apellido)
        self.direc=dirección
        self.codigo=cod
        self.estado=est

    def obtenerdire(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont1=20
        while cont1!=0:
            self.direc=str(input("Ingrese su dirección (No se reciben números): "))
            cont1=0
            for x in self.direc:
                if x in num:
                    cont1+=1
        return self.direc

    def obtenercod(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont2=20
        while cont2!=0:
            self.codigo=str(input("Ingrese su código postal (No se reciben letras, 5 digitos): "))
            cont2=0
            for x in self.codigo:
                if x not in num:
                    cont2+=1
                if len(self.codigo)!=5:
                    cont2+=1
        return self.codigo

    def obtenerest(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont3=20
        while cont3!=0:
            self.estado=str(input("Ingrese el estado en el que se encuentra (No se reciben números): "))
            cont3=0
            for x in self.estado:
                if x in num:
                    cont3+=1
        return self.estado

    def __str__(self):
        return "Su nombre es: " + str(self.nom) + ", y su apellido: " + str(self.ape) + ", con identificación: " + str(self.ide) + " y su dirección fiscal es: " + str(self.direc) + " y su código postal es: " + str(self.codigo) + " y su estado es: " + str(self.estado)


#CLASE EMPLEADO
class Empleado(Persona):
    def __init__(self,identificación,nombre,apellido,ingreso=0,cargo="soy",sueldo=2500):
        super().__init__(identificación,nombre,apellido)
        self.ingreso=ingreso
        self.cargo=cargo
        self.sueldo=sueldo    

    def obteneringre(self):
        cont1=20
        while cont1!=0:
            self.ingreso=int(input("Ingrese su ingreso: "))
            cont1=0
            if self.ingreso<=0:
                cont1+=1
        return self.ingreso

    def obtenercargo(self):
        num=["1","2","3","4","5","6","7","8","9","0"]
        cont2=20
        while cont2!=0:
            self.cargo=str(input("Ingrese su cargo (No se reciben números): "))
            cont2=0
            for x in self.cargo:
                if x in num:
                    cont2+=1
        return self.cargo

    def obtenersueldo(self):
        respuesta=str(input("Su sueldo base es de 2500, ¿es correcto?"))
        if respuesta=="no":
            self.sueldo=int(input("Ingrese su sueldo: "))
            while self.sueldo<=0:
                self.sueldo=int(input("Ingrese su sueldo correctamente: "))
        return self.sueldo

    def __str__(self):
        return "Su nombre es: " + str(self.nom) + ", y su apellido: " + str(self.ape) + ", con identificación: " + str(self.ide) + " y su ingreso es de: " + str(self.ingreso) + " y su cargo es: " + str(self.cargo) + " y su sueldo es de: " + str(self.sueldo)






#Con esto se obtienen los datos de la persona para poder trabajar
c=Persona()
Identificacion=c.obtener()
Nombre=c.obtenernom()
Apellido=c.obtenerape()


#Con esto se llama a la clase estudiante con los datos de la persona ya definidos para poder pedir ingresar el semestre
Estudiante01=Estudiante(Identificacion,Nombre,Apellido)
Semestre=Estudiante01.obtenersem()
Estudiante01=Estudiante(Identificacion,Nombre,Apellido,Semestre)
print(Estudiante01)

#Con esto se llama a la clase cliente con los datos de la persona definidos para pedir los demás datos
Cliente01=Cliente(Identificacion,Nombre,Apellido)
Direccion=Cliente01.obtenerdire()
Codigo=Cliente01.obtenercod()
Estado=Cliente01.obtenerest()
Cliente01=Cliente(Identificacion,Nombre,Apellido,Direccion,Codigo,Estado)
print(Cliente01)

#Con esto se llama a la clase empleado con los datos de la persona definidos para pedir los demás datos
Empleado01=Empleado(Identificacion,Nombre,Apellido)
Ingreso=Empleado01.obteneringre()
Cargo=Empleado01.obtenercargo()
Sueldo=Empleado01.obtenersueldo()
Empleado01=Empleado(Identificacion,Nombre,Apellido,Ingreso,Cargo,Sueldo)
print(Empleado01)