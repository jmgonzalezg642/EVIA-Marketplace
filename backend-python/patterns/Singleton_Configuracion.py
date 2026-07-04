# =============================================================================
# PATRÓN: SINGLETON
# Archivo: patterns/Singleton_Configuracion.py
# =============================================================================

class ConfiguracionSistema:
    """
    Singleton - Configuración única del sistema
    
    Esta clase garantiza que solo exista una instancia en toda la ejecución.
    Almacena todas las listas de datos y los contadores de IDs.
    """
    
    _instancia = None
    
    def __new__(cls):
        """Controla la creación de la instancia única"""
        if cls._instancia is None:
            cls._instancia = super(ConfiguracionSistema, cls).__new__(cls)
            
            # ============================================================
            # CONFIGURACIÓN DEL SISTEMA
            # ============================================================
            cls._instancia.nombre_sistema = "EVIA"
            cls._instancia.version_sistema = "1.0"
            cls._instancia.institucion = "EVIA S.A"
            
            # ============================================================
            # LISTAS DE DATOS (MEMORIA RAM)
            # ============================================================
            cls._instancia.lista_usuarios = []
            cls._instancia.lista_vehiculos = []
            cls._instancia.lista_pedidos = []
            cls._instancia.lista_estaciones = []
            
            # ============================================================
            # CONTADORES DE ID (INDEPENDIENTES POR ENTIDAD)
            # ============================================================
            cls._instancia._contador_usuarios = 1
            cls._instancia._contador_vehiculos = 1
            cls._instancia._contador_pedidos = 1
            cls._instancia._contador_estaciones = 1
            cls._instancia._contador_carritos = 1
        
        return cls._instancia
    
    # ============================================================
    # GENERADORES DE ID
    # ============================================================
    
    def generar_id_usuario(self):
        id_actual = self._contador_usuarios
        self._contador_usuarios += 1
        return id_actual
    
    def generar_id_vehiculo(self):
        id_actual = self._contador_vehiculos
        self._contador_vehiculos += 1
        return id_actual
    
    def generar_id_pedido(self):
        id_actual = self._contador_pedidos
        self._contador_pedidos += 1
        return id_actual
    
    def generar_id_estacion(self):
        id_actual = self._contador_estaciones
        self._contador_estaciones += 1
        return id_actual
    
    def generar_id_carrito(self):
        id_actual = self._contador_carritos
        self._contador_carritos += 1
        return id_actual
    
    # ============================================================
    # MÉTODOS DE CONSULTA
    # ============================================================
    
    def mostrar_configuracion(self):
        return f"{self.nombre_sistema} | Versión: {self.version_sistema} | Institución: {self.institucion}"
    
    def obtener_resumen_memoria(self):
        return (f"Usuarios en memoria: {len(self.lista_usuarios)}\n"
                f"Vehículos en memoria: {len(self.lista_vehiculos)}\n"
                f"Pedidos en memoria: {len(self.lista_pedidos)}")