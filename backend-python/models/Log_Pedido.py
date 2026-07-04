# =============================================================================
# MODELO: PEDIDO
# Archivo: models/Log_Pedido.py
# =============================================================================

from datetime import datetime


class Pedido:
    """Pedido formal de compra"""
    
    IVA_PORCENTAJE = 0.19
    
    def __init__(self, id_entidad, usuario, items, total):
        self.id_entidad = id_entidad
        self.usuario = usuario
        self.items = items
        self.total = total
        self.fecha = datetime.now()
        self.estado = "PENDIENTE"  # PENDIENTE, CONFIRMADO, ENTREGADO, CANCELADO
    
    def confirmar(self):
        """Confirma el pedido"""
        self.estado = "CONFIRMADO"
        for vehiculo in self.items:
            vehiculo.estado_vehiculo = "VENDIDO"
    
    def cancelar(self):
        """Cancela el pedido"""
        self.estado = "CANCELADO"
        for vehiculo in self.items:
            vehiculo.estado_vehiculo = "DISPONIBLE"
    
    def calcular_subtotal(self):
        """Calcula el subtotal del pedido"""
        return sum(v.precio for v in self.items)
    
    def calcular_iva(self):
        """Calcula el IVA del pedido"""
        return self.calcular_subtotal() * self.IVA_PORCENTAJE
    
    def calcular_total(self):
        """Calcula el total del pedido con IVA"""
        return self.calcular_subtotal() + self.calcular_iva()
    
    def __str__(self):
        return (f"Pedido #{self.id_entidad} | Usuario: {self.usuario.nombre} | "
                f"Total: ${self.total:,.0f} | Estado: {self.estado}")