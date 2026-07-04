# =============================================================================
# MODELO: SESION
# Archivo: models/Log_Sesion.py
# =============================================================================




class Sesion:
    """Sesión de usuario en el sistema"""
    
    def __init__(self, id_entidad, usuario, fecha_inicio, fecha_expiracion):
        self.id_entidad = id_entidad
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_expiracion = fecha_expiracion
        self._esta_activa = True
    
    def esta_activa(self):
        """Retorna True si la sesión está activa"""
        return self._esta_activa
    
    def cerrar_sesion(self):
        """Cierra la sesión"""
        self._esta_activa = False
    
    def renovar(self):
        """Renueva la sesión"""
        self._esta_activa = True
    
    def __str__(self):
        estado = "Activa" if self._esta_activa else "Inactiva"
        return f"[Sesión ID: {self.id_entidad}] Usuario: {self.usuario.nombre} | Estado: {estado}"