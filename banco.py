# cajero-
class CuentaBancaria:
    def __init__(self, nro_cuenta=0, dni=0, apellido="desconocido", nombre="desconocido", saldo_inicial=0, es_cuenta_corriente=False):
        self.nro_cuenta = nro_cuenta
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.saldo = saldo_inicial
        self.es_cuenta_corriente = es_cuenta_corriente

    def deposito(self, monto):
        self.saldo =self.saldo + monto
    
    def extraccion(self, monto):
        if self.saldo>monto or not self.saldo==0:
            self.saldo=self.saldo-monto
        
        else:
            print("saldo no disponible")
            
    def versaldo(self):
        return self.saldo
    
    def vertitular(self):
        return self.nombre, self.apellido, "dni:",self.dni
    
    def  vertodo(self):
        return self.nro_cuenta, "dni:" ,self.dni,self.apellido,self.nombre,self.saldo,self.es_cuenta_corriente
        

# Solicitar datos al usuario
print("=== INGRESO DE DATOS DE LA CUENTA ===")
    
numcuenta= int(input("Ingrese el número de cuenta: "))
dni= int(input("ingrese su dni: "))
ap= input("ingrese su apellido: ")
nombre=input("ingrese su nombre: ")
sal=float(input("ingrese el saldo: "))
escuentaCorriente=bool(input("es cuenta corriente? (True/False): "))

cuenta= CuentaBancaria(numcuenta, dni, ap, nombre, sal, escuentaCorriente)

          
while True:
    print("\n=== MENÚ DE OPCIONES ===")
    print("1. Depositar")
    print("2. Extraer")
    print("3. Ver saldo")
    print("4. Ver datos del titular")
    print("5. Ver todos los datos")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        monto=float(input("ingrese el monto a depositar: "))
        cuenta.deposito(monto)
        print("Depósito realizado con éxito.")
        
    elif opcion == '2':
        monto=float(input("ingrese el monto para extraer: "))
        cuenta.extraccion(monto)
        print("extraccion realizada")
    
    elif opcion == '3':
        saldo=cuenta.versaldo()
        print("saldo actual:",saldo)
        
    elif opcion == '4':
        titular=cuenta.vertitular()
        print("datos: ",titular)
    
    elif opcion == '5':
        datos=cuenta.vertodo()
        print("Datos completos de la cuenta:", datos)
    
    elif opcion == '6':
        print("saliendo")
        break
