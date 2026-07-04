# =============================================================================
# CONEXIÓN A BASE DE DATOS
# Archivo: config/Conexion.py
# =============================================================================

import mysql.connector
from mysql.connector import Error


class Conexion:
    """
    Clase encargada de crear la conexión entre Python y MySQL/MariaDB.
    Centraliza los datos de conexión para no repetirlos en varios archivos.
    """
    
    @staticmethod
    def obtener_conexion():
        """
        Obtiene una conexión a la base de datos bd_evia.
        
        Returns:
            connection: Objeto de conexión a MySQL o None si hay error.
        """
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Si tienes contraseña en XAMPP, colócala aquí
                database="bd_evia"
            )
            if conexion.is_connected():
                return conexion
        except Error as error:
            print(f"   ❌ Error al conectar con la base de datos: {error}")
            return None
    
    @staticmethod
    def cerrar_conexion(conexion):
        """
        Cierra la conexión a la base de datos.
        
        Args:
            conexion: Objeto de conexión a cerrar.
        """
        if conexion and conexion.is_connected():
            conexion.close()