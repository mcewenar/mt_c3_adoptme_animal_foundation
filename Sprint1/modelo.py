class Billete:
    def __init__(self):
        self.__valor = 0
        self.__cantidad = 0
    def asignarValor(self,v):
        self.__valor = v
    def asignarCantidad(self,c):
        self.__cantidad = c
    def verValor(self):
        return self.__valor
    def verCantidad(self):
        return self.__cantidad

class Sistema(Billete):
    def __init__(self):
        Billete.__init__(self)
        #super().__init__() OTRA FORMA DE HERENCIA
        self.objetos_Billete = []
        self.totalidad_cajero = 0
        
        
    def devuelta(self,cambio):
        resta = self.cantidadCajero()
        cambio1 = 0
        papeles = 0
        if cambio > resta:
            print("Su petición supera el dinero disponible de la caja. Por favor ingrese una suma inferior.")
            print("Nuestro banco pobre tan solo tiene $"+str(resta))

        else:
            resta = resta - cambio
            for d in self.objetos_Billete:
                if cambio >= 0:
                    div = cambio//d.verValor()
                    if div > d.verCantidad():
                        papeles = d.verCantidad()
                    else:
                        papeles = div
                    cambio1 = cambio % d.verValor()
                    cambio -= d.verValor()*papeles
                    if papeles != 0:
                        print("Se entregó {0} billete(s) de".format(papeles),"$"+str(d.verValor()))

            if papeles != 0:   
                print("Sobró $" + str(cambio1))
                print("Nuestro banco pobre ahora tan solo tiene $"+str(resta))
            else:
                print("No es posible hacer la transacción")
            
        print()
        print("Fue un placer. Vuelva pronto.\n\n")
            
            
        
    def cantidadCajero(self):
        for f in self.objetos_Billete:
            self.totalidad_cajero += f.verCantidad() * f.verValor()
        return self.totalidad_cajero
    
    def crearBilletes(self,v,c):
        billetico = Billete()
        billetico.asignarValor(v)
        billetico.asignarCantidad(c)
        nuevo_billete = self.objetos_Billete.append(billetico)
        return nuevo_billete
        
        
def main():
    denominaciones = [500,200,100,50,10]
    sis = Sistema()
    while True:
        while True:
            try:
                opcion = int(input("Ingrese la opción que desea: \nElige 1. Para retirar dinero.\nElige 2. para agregar billetes (Opción no válida para clientes). "))
                break
            except ValueError:
                print("Dato inválido. Por favor ingresa nuevamente")
        if opcion == 1:
            while True:
                try:
                    Dinero = int(input("Ingrese el valor que desea retirar: "))
                    break
                except ValueError:
                    print("Dato inválido. Por favor ingresa nuevamente")
            sis.devuelta(Dinero)
        elif opcion == 2:
            while True:
                try:
                    for v in denominaciones:
                        c = int(input("Ingrese la cantidad de billetes de $"+ str(v)+": "))
                        sis.crearBilletes(v,c)
                    print("Se ha ingresado los billetes satisfactoriamente")
                    break
                except:
                    print("Dato erróneo. Inténtalo nuevamente")
                    continue
        else:
            print("Valor erróneo")
            continue

main()