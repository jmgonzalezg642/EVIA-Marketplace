# =============================================================================
# MODELO: CARRO
# Archivo: models/Log_Carro.py
# =============================================================================

from models.Log_Vehiculo import Vehiculo


class Carro(Vehiculo):
    """Subclase de Vehiculo para Carros"""
    
    def __init__(self, id_entidad, marca, modelo, precio, autonomia_km,
                 capacidad_bateria_kwh, peso_kg, velocidad_maxima,
                 tipo_conector, garantia_meses, año, estado_vehiculo,
                 vendedor, es_nuevo, num_puertas, tipo_traccion):
        
        super().__init__(id_entidad, "CARRO", marca, modelo, precio,
                        autonomia_km, capacidad_bateria_kwh, peso_kg,
                        velocidad_maxima, tipo_conector, garantia_meses,
                        año, estado_vehiculo, vendedor, es_nuevo)
        
        self.num_puertas = num_puertas
        self.tipo_traccion = tipo_traccion
    
    def obtener_especificaciones(self):
        """Retorna las especificaciones completas del carro"""
        nuevo_usado = "🚗 NUEVO" if self.es_nuevo else "🚗 USADO"
        return (f"\n{'='*50}\n"
                f"{nuevo_usado} | {self.marca} {self.modelo} ({self.año})\n"
                f"  Precio      : ${self.precio:,.0f} COP\n"
                f"  Vendedor    : {self.vendedor.nombre}\n"
                f"  Puertas     : {self.num_puertas}\n"
                f"  Tracción    : {self.tipo_traccion}\n"
                f"  Autonomía   : {self.autonomia_km} km\n"
                f"  Batería     : {self.capacidad_bateria_kwh} kWh\n"
                f"  Estado      : {self.estado_vehiculo}\n"
                f"{'='*50}")
    
    def calcular_costo_mantenimiento(self):
        """Calcula costo estimado de mantenimiento"""
        return self.precio * 0.015 * (self.garantia_meses / 12)