# =============================================================================
# MODELO: ESTACION DE CARGA
# Archivo: models/Log_EstacionCarga.py
# =============================================================================

class EstacionCarga:
    """Estación de carga para vehículos eléctricos"""
    
    def __init__(self, id_entidad, nombre, direccion, ciudad,
                 tipos_conector, potencia_kw, disponible=True):
        self.id_entidad = id_entidad
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tipos_conector = tipos_conector
        self.potencia_kw = potencia_kw
        self.disponible = disponible
    
    def soporta_conector(self, tipo_conector):
        """Verifica si la estación soporta un tipo de conector"""
        return tipo_conector in self.tipos_conector
    
    def reservar(self):
        """Reserva la estación"""
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def liberar(self):
        """Libera la estación"""
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return (f"[Estación ID: {self.id_entidad}] {self.nombre} | "
                f"{self.ciudad} | {self.potencia_kw} kW | {estado}")