from packages import Package

class Container:

    def __init__(self, capacidad, packages = []):
        self.capacidad = capacidad
        self.packages = packages

    def obtener_peso(self):
        peso_tolal = 0
        for i in self.packages:
            peso_tolal += i.peso
        return peso_tolal

    def subir_paquete(self, new_package):
        if self.capacidad - self.obtener_peso() >= new_package.peso:
            self.packages.append(new_package)
            return True
        return False

    def eliminar_paquete(self, id):
        for i in self.packages:
            if i.id == id:
                print(i.info_package())
                self.packages.remove(i)
                return True
        return False
        
    def obtener_total_impuestos(self):
        totalImp = 0
        for i in self.packages:
            totalImp += i.calculo_impuesto()
        return totalImp
