# =============================================================================
# MODELO: MOTOCICLETA
# Archivo: models/Log_Motocicleta.py
# =============================================================================

from models.Log_Vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    """Subclase de Vehiculo para Motocicletas"""
    
    def __init__(self, id_entidad, marca, modelo, precio, autonomia_km,
                 capacidad_bateria_kwh, peso_kg, velocidad_maxima,
                 tipo_conector, garantia_meses, año, estado_vehiculo,
                 vendedor, es_nuevo, num_cascos_incluidos, tipo_manillar):
        
        super().__init__(id_entidad, "MOTOCICLETA", marca, modelo, precio,
                        autonomia_km, capacidad_bateria_kwh, peso_kg,
                        velocidad_maxima, tipo_conector, garantia_meses,
                        año, estado_vehiculo, vendedor, es_nuevo)
        
        self.num_cascos_incluidos = num_cascos_incluidos
        self.tipo_manillar = tipo_manillar
    
    def obtener_especificaciones(self):
        """Retorna las especificaciones completas de la motocicleta"""
        nuevo_usado = "🏍️ NUEVO" if self.es_nuevo else "🏍️ USADO"
        return (f"\n{'='*50}\n"
                f"{nuevo_usado} | {self.marca} {self.modelo} ({self.año})\n"
                f"  Precio      : ${self.precio:,.0f} COP\n"
                f"  Vendedor    : {self.vendedor.nombre}\n"
                f"  Cascos incl.: {self.num_cascos_incluidos}\n"
                f"  Manillar    : {self.tipo_manillar}\n"
                f"  Autonomía   : {self.autonomia_km} km\n"
                f"  Batería     : {self.capacidad_bateria_kwh} kWh\n"
                f"  Estado      : {self.estado_vehiculo}\n"
                f"{'='*50}")
    
    def calcular_costo_mantenimiento(self):
        """Calcula costo estimado de mantenimiento"""
        return self.precio * 0.012 * (self.garantia_meses / 12)