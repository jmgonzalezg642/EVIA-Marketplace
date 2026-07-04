# =============================================================================
# MODELO: VEHÍCULO (BASE)
# Archivo: models/Log_Vehiculo.py
# =============================================================================

class Vehiculo:
    """Clase base para TODOS los vehículos (nuevos y usados)"""
    
    def __init__(self, id_entidad, tipo_vehiculo, marca, modelo, 
                 precio, autonomia_km, capacidad_bateria_kwh,
                 peso_kg, velocidad_maxima, tipo_conector, 
                 garantia_meses, año, estado_vehiculo, 
                 vendedor, es_nuevo):
        
        self.id_entidad = id_entidad
        self.tipo_vehiculo = tipo_vehiculo  # CARRO, MOTOCICLETA, PATINETA
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.autonomia_km = autonomia_km
        self.capacidad_bateria_kwh = capacidad_bateria_kwh
        self.peso_kg = peso_kg
        self.velocidad_maxima = velocidad_maxima
        self.tipo_conector = tipo_conector
        self.garantia_meses = garantia_meses
        self.año = año
        self.estado_vehiculo = estado_vehiculo  # DISPONIBLE, VENDIDO, RESERVADO
        self.vendedor = vendedor
        self.es_nuevo = es_nuevo  # True = NUEVO, False = USADO
        self.fecha_publicacion = None
    
    @property
    def tipo_publicacion(self):
        """Retorna 'NUEVO' o 'USADO' según el atributo"""
        return "NUEVO" if self.es_nuevo else "USADO"
    
    def obtener_especificaciones(self):
        """Método que deben sobreescribir las subclases"""
        raise NotImplementedError("Subclase debe implementar obtener_especificaciones()")
    
    def calcular_costo_mantenimiento(self):
        """Método que deben sobreescribir las subclases"""
        raise NotImplementedError("Subclase debe implementar calcular_costo_mantenimiento()")
    
    def __str__(self):
        return (f"[{self.id_entidad}] {self.marca} {self.modelo} "
                f"({self.año}) - {self.tipo_publicacion} - ${self.precio:,.0f}")