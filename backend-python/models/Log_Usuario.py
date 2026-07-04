# =============================================================================
# MODELO: USUARIO
# Archivo: models/Log_Usuario.py
# =============================================================================

class Usuario:
    """Usuario del sistema EVIA"""
    
    def __init__(self, id_entidad, nombre, correo, cedula, ciudad, rol, telefono):
        self.id_entidad = id_entidad
        self.nombre = nombre
        self.correo = correo
        self.cedula = cedula
        self.ciudad = ciudad
        self.telefono = telefono
        
        # ROLES:
        # - comprador: SOLO compra
        # - vendedor_persona: compra + vende usado
        # - vendedor_empresa: SOLO vende (nuevo y usado)
        # - administrador: hace todo
        self.rol = rol.lower()
    
    # ============================================================
    # PERMISOS DE COMPRA
    # ============================================================
    
    def puede_comprar(self):
        """Quiénes pueden COMPRAR: comprador, vendedor_persona, administrador"""
        return self.rol in ["comprador", "vendedor_persona", "administrador"]
    
    # ============================================================
    # PERMISOS DE VENTA
    # ============================================================
    
    def puede_vender_usado(self):
        """Quiénes pueden vender USADO: vendedor_persona, vendedor_empresa, administrador"""
        return self.rol in ["vendedor_persona", "vendedor_empresa", "administrador"]
    
    def puede_vender_nuevo(self):
        """Quiénes pueden vender NUEVO: solo vendedor_empresa y administrador"""
        return self.rol in ["vendedor_empresa", "administrador"]
    
    # ============================================================
    # VERIFICACIÓN DE ROL
    # ============================================================
    
    def es_comprador(self):
        return self.rol == "comprador"
    
    def es_vendedor_persona(self):
        return self.rol == "vendedor_persona"
    
    def es_vendedor_empresa(self):
        return self.rol == "vendedor_empresa"
    
    def es_administrador(self):
        return self.rol == "administrador"
    
    # ============================================================
    # TEXTO PARA MOSTRAR
    # ============================================================
    
    @property
    def tipo_usuario(self):
        tipos = {
            "comprador": "Comprador",
            "vendedor_persona": "Vendedor Particular",
            "vendedor_empresa": "Vendedor Empresa",
            "administrador": "Administrador"
        }
        return tipos.get(self.rol, self.rol)
    
    @property
    def permisos(self):
        """Muestra los permisos del usuario"""
        permisos = []
        if self.puede_comprar():
            permisos.append("🛒 Comprar")
        if self.puede_vender_usado():
            permisos.append("📝 Vender Usado")
        if self.puede_vender_nuevo():
            permisos.append("🏭 Vender Nuevo")
        if self.es_administrador():
            permisos.append("👑 Administrar")
        return " | ".join(permisos) if permisos else "Sin permisos"
    
    def __str__(self):
        return f"[{self.id_entidad}] {self.nombre} | {self.tipo_usuario}"