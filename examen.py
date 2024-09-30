from abc import ABC, abstractmethod

class EmpleadoInvalido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Empleado_32(ABC):
    def __init__(self, rfc, apellido, nombres, salario):
        self.__rfc = rfc
        self.__apellido = apellido
        self.__nombres = nombres
        self.__salario = salario
        self.__validar_salario()

    def __validar_salario(self):
        if self.__salario < 150:
            print("El salario debe ser al menos 150 pesos.")

    @abstractmethod
    def calcular_sueldo(self):
        pass

    def mostrar_informacion(self):
        return f"RFC: {self.__rfc}\nApellido: {self.__apellido}\nNombre: {self.__nombres}\nSalario: {self.__salario}"

class EmpleadoVendedor(Empleado_32):
    def __init__(self, rfc, apellido, nombres, salario, monto_vendido, tasa_comision):
        super().__init__(rfc, apellido, nombres, salario)
        self.__monto_vendido = monto_vendido
        self.__tasa_comision = tasa_comision

    def calcular_ingresos(self):
        return self.__monto_vendido * self.__tasa_comision

    def calcular_bonificacion(self):
        if self.__monto_vendido < 1000:
            return 0
        elif self.__monto_vendido < 5000:
            return (self.__monto_vendido * self.__tasa_comision) / 0.05
        else:
            return (self.__monto_vendido * self.__tasa_comision) / 0.1

    def calcular_descuento(self, ingresos):
        if ingresos < 1000:
            return ingresos * 0.11
        else:
            return ingresos * 0.15

    def calcular_sueldo(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento(ingresos)
        return ingresos + bonificacion - descuento

class EmpleadoPermanente(Empleado_32):
    def __init__(self, rfc, apellido, nombres, salario, sueldo_base, nss):
        super().__init__(rfc, apellido, nombres, salario)
        self.__sueldo_base = sueldo_base
        self.__nss = nss

    def calcular_ingresos(self):
        return self.__sueldo_base

    def calcular_descuento(self, ingresos):
        return ingresos * 0.11

    def calcular_sueldo(self):
        ingresos = self.calcular_ingresos()
        descuento = self.calcular_descuento(ingresos)
        return ingresos - descuento

try:
    vendedor = EmpleadoVendedor("ZAML", "Zaldivar", "Luis", 200, 3000, 0.10)
    print(vendedor.mostrar_informacion())
    print("Sueldo Vendedor:", vendedor.calcular_sueldo())
    
    permanente = EmpleadoPermanente("ESVE", "Estrada", "Ezequiel", 300, 2500, "123")
    print(permanente.mostrar_informacion())
    print("Sueldo Permanente:", permanente.calcular_sueldo())
except EmpleadoInvalido as e:
    print(e)