from container import Container
from packages import Package

paquete1 = Package("SCL001", 10, 100, "Repuestos Motor")
paquete2 = Package("SCL002", 0.2, 200, "Celular")
paquete3 = Package("SCL003", 1, 20, "Accesorios Bicicleta")
paquete4 = Package("SCL004", 5, 30, "Libro")
paquete5 = Package("SCL005", 1, 10, "CD Musica")

container1 = Container(15)

#Imprimir paquete
print(paquete3.info_package())

#Calcular impuesto de un paquete
print(paquete1.calculo_impuesto())

#Agregar paquetes al container
print(container1.subir_paquete(paquete1))
print(container1.subir_paquete(paquete2))
print(container1.subir_paquete(paquete3))
print(container1.subir_paquete(paquete4))
print(container1.subir_paquete(paquete5))

#Información de los paquetes en el contenedor
for i in container1.packages:
    print(i.info_package())

#Imprimir total de impuestos del container
print(container1.obtener_total_impuestos())

#Eliminar paquete del container y mostrar informacion de los paquetes del contenedor
print(container1.eliminar_paquete("SCL001"))
for i in container1.packages:
    print(i.info_package())

#Eliminar paquete QUE NO EXISTE en el container
print(container1.eliminar_paquete("SCL006"))

#Obtener peso total del container
print(container1.obtener_peso())
