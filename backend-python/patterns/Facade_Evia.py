# =============================================================================
# PATRÓN: FACADE
# Archivo: patterns/Facade_EVIA.py
# =============================================================================

from repositories.Usuario_Repository import UsuarioRepository
from repositories.Vehiculo_Repository import VehiculoRepository


class FacadeEVIA:
    """
    Patrón estructural Facade.
    Simplifica las operaciones de guardado y consulta de datos.
    """
    
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        self.vehiculo_repository = VehiculoRepository()
    
    # ============================================================
    # OPERACIONES CON USUARIOS
    # ============================================================
    
    def guardar_usuario(self, usuario):
        """
        Guarda un usuario en la base de datos.
        
        Args:
            usuario: Objeto Usuario.
            
        Returns:
            bool: True si se guardó correctamente.
        """
        return self.usuario_repository.guardar_usuario(usuario)
    
    def listar_usuarios(self):
        """
        Lista todos los usuarios de la base de datos.
        
        Returns:
            list: Lista de usuarios.
        """
        return self.usuario_repository.listar_usuarios()
    
    # ============================================================
    # OPERACIONES CON VEHÍCULOS
    # ============================================================
    
    def guardar_vehiculo(self, vehiculo, id_vendedor):
        """
        Guarda un vehículo en la base de datos.
        
        Args:
            vehiculo: Objeto Vehiculo.
            id_vendedor: ID del vendedor.
            
        Returns:
            bool: True si se guardó correctamente.
        """
        return self.vehiculo_repository.guardar_vehiculo(vehiculo, id_vendedor)
    
    def listar_vehiculos(self):
        """
        Lista todos los vehículos de la base de datos.
        
        Returns:
            list: Lista de vehículos.
        """
        return self.vehiculo_repository.listar_vehiculos()