# =============================================================================
# REPOSITORIO DE USUARIOS
# Archivo: repositories/Usuario_Repository.py
# =============================================================================

from config.Conexion import Conexion


class UsuarioRepository:
    """
    Clase encargada de realizar operaciones SQL relacionadas con usuarios.
    Aquí se ubican las consultas de base de datos.
    """
    
    def guardar_usuario(self, usuario):
        """
        Guarda un usuario en la base de datos.
        
        Args:
            usuario: Objeto Usuario con los datos a guardar.
            
        Returns:
            bool: True si se guardó correctamente, False en caso contrario.
        """
        conexion = Conexion.obtener_conexion()
        if conexion is None:
            return False
        
        try:
            cursor = conexion.cursor()
            consulta_sql = """
                INSERT INTO usuarios (
                    identificacion_usuario,
                    nombre_usuario,
                    correo_usuario,
                    ciudad_usuario,
                    telefono_usuario,
                    rol_usuario
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """
            datos_usuario = (
                usuario.cedula,
                usuario.nombre,
                usuario.correo,
                usuario.ciudad,
                usuario.telefono,
                usuario.rol
            )
            cursor.execute(consulta_sql, datos_usuario)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Exception as error:
            print(f"   ❌ Error al guardar usuario: {error}")
            if conexion.is_connected():
                conexion.close()
            return False
    
    def listar_usuarios(self):
        """
        Lista todos los usuarios registrados en la base de datos.
        
        Returns:
            list: Lista de diccionarios con los datos de los usuarios.
        """
        conexion = Conexion.obtener_conexion()
        if conexion is None:
            return []
        
        try:
            cursor = conexion.cursor(dictionary=True)
            consulta_sql = """
                SELECT 
                    id_usuario,
                    identificacion_usuario,
                    nombre_usuario,
                    correo_usuario,
                    ciudad_usuario,
                    telefono_usuario,
                    rol_usuario
                FROM usuarios
                ORDER BY id_usuario ASC
            """
            cursor.execute(consulta_sql)
            lista_usuarios = cursor.fetchall()
            cursor.close()
            conexion.close()
            return lista_usuarios
        except Exception as error:
            print(f"   ❌ Error al listar usuarios: {error}")
            if conexion.is_connected():
                conexion.close()
            return []