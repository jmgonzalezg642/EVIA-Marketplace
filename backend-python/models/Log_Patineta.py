# =============================================================================
# MODELO: PATINETA
# Archivo: models/Log_Patineta.py
# =============================================================================

from models.Log_Vehiculo import Vehiculo


class Patineta(Vehiculo):
    """Subclase de Vehiculo para Patinetas"""
    
    def __init__(self, id_entidad, marca, modelo, precio, autonomia_km,
                 capacidad_bateria_kwh, peso_kg, velocidad_maxima,
                 tipo_conector, garantia_meses, año, estado_vehiculo,
                 vendedor, es_nuevo, plegable, peso_maximo_usuario):
        
        super().__init__(id_entidad, "PATINETA", marca, modelo, precio,
                        autonomia_km, capacidad_bateria_kwh, peso_kg,
                        velocidad_maxima, tipo_conector, garantia_meses,
                        año, estado_vehiculo, vendedor, es_nuevo)
        
        self.plegable = plegable
        self.peso_maximo_usuario = peso_maximo_usuario
    
    def obtener_especificaciones(self):
        """Retorna las especificaciones completas de la patineta"""
        nuevo_usado = "🛴 NUEVO" if self.es_nuevo else "🛴 USADO"
        es_plegable = "Sí" if self.plegable else "No"
        return (f"\n{'='*50}\n"
                f"{nuevo_usado} | {self.marca} {self.modelo} ({self.año})\n"
                f"  Precio      : ${self.precio:,.0f} COP\n"
                f"  Vendedor    : {self.vendedor.nombre}\n"
                f"  Plegable    : {es_plegable}\n"
                f"  Peso máx.   : {self.peso_maximo_usuario} kg\n"
                f"  Autonomía   : {self.autonomia_km} km\n"
                f"  Batería     : {self.capacidad_bateria_kwh} kWh\n"
                f"  Estado      : {self.estado_vehiculo}\n"
                f"{'='*50}")
    
    def calcular_costo_mantenimiento(self):
        """Calcula costo estimado de mantenimiento"""
        return self.precio * 0.008 * (self.garantia_meses / 12)