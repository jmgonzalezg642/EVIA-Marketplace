# =============================================================================
# MODELO: CARRITO
# Archivo: models/Log_Carrito.py
# =============================================================================

class Carrito:
    """Carrito de compras del usuario"""
    
    def __init__(self, id_entidad, usuario):
        self.id_entidad = id_entidad
        self.usuario = usuario
        self.items = []  # Lista de vehículos
        self.total = 0.0
    
    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo al carrito"""
        self.items.append(vehiculo)
        self.total += vehiculo.precio
        return True
    
    def eliminar_vehiculo(self, id_vehiculo):
        """Elimina un vehículo del carrito"""
        for item in self.items:
            if item.id_entidad == id_vehiculo:
                self.items.remove(item)
                self.total -= item.precio
                return True
        return False
    
    def esta_vacio(self):
        """Retorna True si el carrito está vacío"""
        return len(self.items) == 0
    
    def vaciar(self):
        """Vacía el carrito"""
        self.items = []
        self.total = 0.0
    
    def calcular_total(self):
        """Calcula el total del carrito"""
        return self.total
    
    def __str__(self):
        return f"Carrito de {self.usuario.nombre} | {len(self.items)} vehículos | Total: ${self.total:,.0f}"