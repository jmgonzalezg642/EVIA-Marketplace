# =============================================================================
# REPOSITORIO DE VEHÍCULOS
# Archivo: repositories/Vehiculo_Repository.py
# =============================================================================

from config.Conexion import Conexion


class VehiculoRepository:
    """
    Clase encargada de realizar operaciones SQL relacionadas con vehículos.
    """
    
    def guardar_vehiculo(self, vehiculo, id_vendedor):
        """
        Guarda un vehículo en la base de datos.
        
        Args:
            vehiculo: Objeto Vehiculo con los datos a guardar.
            id_vendedor: ID del vendedor en la base de datos.
            
        Returns:
            bool: True si se guardó correctamente.
        """
        conexion = Conexion.obtener_conexion()
        if conexion is None:
            return False
        
        try:
            cursor = conexion.cursor()
            consulta_sql = """
                INSERT INTO vehiculos (
                    id_vendedor,
                    tipo_vehiculo,
                    marca,
                    modelo,
                    precio,
                    autonomia_km,
                    capacidad_bateria_kwh,
                    peso_kg,
                    velocidad_maxima,
                    tipo_conector,
                    garantia_meses,
                    año,
                    es_nuevo,
                    estado_vehiculo
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            datos_vehiculo = (
                id_vendedor,
                vehiculo.tipo_vehiculo,
                vehiculo.marca,
                vehiculo.modelo,
                vehiculo.precio,
                vehiculo.autonomia_km,
                vehiculo.capacidad_bateria_kwh,
                vehiculo.peso_kg,
                vehiculo.velocidad_maxima,
                vehiculo.tipo_conector,
                vehiculo.garantia_meses,
                vehiculo.año,
                vehiculo.es_nuevo,
                vehiculo.estado_vehiculo
            )
            cursor.execute(consulta_sql, datos_vehiculo)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as error:
            print(f"   ❌ Error al guardar vehículo: {error}")
            if conexion.is_connected():
                conexion.close()
            return False
    
    def listar_vehiculos(self):
        """
        Lista todos los vehículos registrados en la base de datos.
        
        Returns:
            list: Lista de diccionarios con los datos de los vehículos.
        """
        conexion = Conexion.obtener_conexion()
        if conexion is None:
            return []
        
        try:
            cursor = conexion.cursor(dictionary=True)
            consulta_sql = """
                SELECT 
                    v.id_vehiculo,
                    v.tipo_vehiculo,
                    v.marca,
                    v.modelo,
                    v.precio,
                    v.autonomia_km,
                    v.capacidad_bateria_kwh,
                    v.peso_kg,
                    v.velocidad_maxima,
                    v.tipo_conector,
                    v.garantia_meses,
                    v.año,
                    v.es_nuevo,
                    v.estado_vehiculo,
                    u.nombre_usuario AS vendedor
                FROM vehiculos v
                JOIN usuarios u ON v.id_vendedor = u.id_usuario
                ORDER BY v.id_vehiculo ASC
            """
            cursor.execute(consulta_sql)
            lista_vehiculos = cursor.fetchall()
            cursor.close()
            conexion.close()
            return lista_vehiculos
        except Exception as error:
            print(f"   ❌ Error al listar vehículos: {error}")
            if conexion.is_connected():
                conexion.close()
            return []