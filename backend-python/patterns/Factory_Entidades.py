# =============================================================================
# PATRÓN: FACTORY METHOD
# Archivo: patterns/Factory_Entidades.py
# =============================================================================

from models.Log_Usuario import Usuario
from models.Log_Carro import Carro
from models.Log_Motocicleta import Motocicleta
from models.Log_Patineta import Patineta


class FactoryEntidades:
    """Fábrica para crear entidades del sistema"""
    
    @staticmethod
    def crear_entidad(categoria, tipo, datos):
        """
        Crea una entidad según la categoría y tipo
        
        Args:
            categoria (str): 'usuario' o 'vehiculo'
            tipo (str): Para usuario: rol (comprador, vendedor_persona, vendedor_empresa, administrador)
                       Para vehiculo: '1' (Carro), '2' (Motocicleta), '3' (Patineta)
            datos (dict): Diccionario con los datos de la entidad
        
        Returns:
            object: Instancia de la entidad creada
        """
        
        # ============================================================
        # CATEGORÍA: USUARIO
        # ============================================================
        if categoria == "usuario":
            return Usuario(
                id_entidad=datos.get("id_entidad", 0),
                nombre=datos.get("nombre", ""),
                correo=datos.get("correo", ""),
                cedula=datos.get("cedula", ""),
                ciudad=datos.get("ciudad", ""),
                rol=datos.get("rol", "comprador"),
                telefono=datos.get("telefono", "")
            )
        
        # ============================================================
        # CATEGORÍA: VEHÍCULO
        # ============================================================
        elif categoria == "vehiculo":
            
            # ---------- CARRO (tipo 1) ----------
            if tipo == "1":
                return Carro(
                    id_entidad=datos["id_entidad"],
                    marca=datos["marca"],
                    modelo=datos["modelo"],
                    precio=datos["precio"],
                    autonomia_km=datos["autonomia_km"],
                    capacidad_bateria_kwh=datos["capacidad_bateria_kwh"],
                    peso_kg=datos["peso_kg"],
                    velocidad_maxima=datos["velocidad_maxima"],
                    tipo_conector=datos["tipo_conector"],
                    garantia_meses=datos["garantia_meses"],
                    año=datos["año"],
                    estado_vehiculo=datos["estado_vehiculo"],
                    vendedor=datos["vendedor"],
                    es_nuevo=datos["es_nuevo"],
                    num_puertas=datos["num_puertas"],
                    tipo_traccion=datos["tipo_traccion"]
                )
            
            # ---------- MOTOCICLETA (tipo 2) ----------
            elif tipo == "2":
                return Motocicleta(
                    id_entidad=datos["id_entidad"],
                    marca=datos["marca"],
                    modelo=datos["modelo"],
                    precio=datos["precio"],
                    autonomia_km=datos["autonomia_km"],
                    capacidad_bateria_kwh=datos["capacidad_bateria_kwh"],
                    peso_kg=datos["peso_kg"],
                    velocidad_maxima=datos["velocidad_maxima"],
                    tipo_conector=datos["tipo_conector"],
                    garantia_meses=datos["garantia_meses"],
                    año=datos["año"],
                    estado_vehiculo=datos["estado_vehiculo"],
                    vendedor=datos["vendedor"],
                    es_nuevo=datos["es_nuevo"],
                    num_cascos_incluidos=datos["num_cascos_incluidos"],
                    tipo_manillar=datos["tipo_manillar"]
                )
            
            # ---------- PATINETA (tipo 3) ----------
            elif tipo == "3":
                return Patineta(
                    id_entidad=datos["id_entidad"],
                    marca=datos["marca"],
                    modelo=datos["modelo"],
                    precio=datos["precio"],
                    autonomia_km=datos["autonomia_km"],
                    capacidad_bateria_kwh=datos["capacidad_bateria_kwh"],
                    peso_kg=datos["peso_kg"],
                    velocidad_maxima=datos["velocidad_maxima"],
                    tipo_conector=datos["tipo_conector"],
                    garantia_meses=datos["garantia_meses"],
                    año=datos["año"],
                    estado_vehiculo=datos["estado_vehiculo"],
                    vendedor=datos["vendedor"],
                    es_nuevo=datos["es_nuevo"],
                    plegable=datos["plegable"],
                    peso_maximo_usuario=datos["peso_maximo_usuario"]
                )
        
        # ============================================================
        # ERROR: Categoría o tipo no válido
        # ============================================================
        raise ValueError(f"Categoría o tipo no válido: {categoria}, {tipo}")