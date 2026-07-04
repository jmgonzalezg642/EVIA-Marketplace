# =============================================================================
# MODELO: ITEM CARRITO
# Archivo: models/Log_ItemCarrito.py
# =============================================================================

class ItemCarrito:
    """Item dentro del carrito de compras"""
    
    def __init__(self, id_entidad, vehiculo, cantidad, incluye_cargador):
        self.id_entidad = id_entidad
        self.vehiculo = vehiculo
        self.cantidad = cantidad
        self.incluye_cargador = incluye_cargador
        self.precio_unitario = vehiculo.precio
    
    def calcular_subtotal(self):
        """Calcula el subtotal del item"""
        return self.precio_unitario * self.cantidad
    
    def __str__(self):
        cargador = "Con cargador" if self.incluye_cargador else "Sin cargador"
        return (f"[Ítem ID: {self.id_entidad}] {self.vehiculo.marca} {self.vehiculo.modelo} | "
                f"Cant: {self.cantidad} | {cargador} | Subtotal: ${self.calcular_subtotal():,.0f}")