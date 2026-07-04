# =============================================================================
# CONTROLADOR PRINCIPAL - CON BASE DE DATOS
# Archivo: controllers/Sistema_Controller.py
# =============================================================================

from patterns.Singleton_Configuracion import ConfiguracionSistema
from patterns.Factory_Entidades import FactoryEntidades
from patterns.Facade_Evia import FacadeEVIA
from models.Log_Carrito import Carrito
from models.Log_Pedido import Pedido

LINEA = "=" * 55


class SistemaController:
    """Controlador principal - Coordina todo el sistema"""
    
    def __init__(self, vista):
        self.vista = vista
        self.config = ConfiguracionSistema()
        self.facade = FacadeEVIA()
        self.usuario_actual = None
        self.carrito_actual = None
        self._cargar_usuarios_de_bd()
    
    # ============================================================
    # GESTIÓN DE USUARIO
    # ============================================================
    
    def _cargar_usuarios_de_bd(self):
        """Carga los usuarios desde la base de datos al Singleton"""
        usuarios_bd = self.facade.listar_usuarios()
        if usuarios_bd:
            self.config.lista_usuarios = []
            for u in usuarios_bd:
                try:
                    usuario = FactoryEntidades.crear_entidad(
                        "usuario",
                        u["rol_usuario"],
                        {
                            "id_entidad": u["id_usuario"],
                            "nombre": u["nombre_usuario"],
                            "correo": u["correo_usuario"],
                            "cedula": u["identificacion_usuario"],
                            "ciudad": u["ciudad_usuario"] or "",
                            "telefono": u["telefono_usuario"] or "",
                            "rol": u["rol_usuario"]
                        }
                    )
                    self.config.lista_usuarios.append(usuario)
                except Exception as e:
                    print(f"   ⚠️ Error al cargar usuario: {e}")
    
    def cerrar_sesion(self):
        """Cierra la sesión del usuario actual"""
        self.usuario_actual = None
        self.carrito_actual = None
    
    def seleccionar_usuario(self):
        """Selecciona el usuario que va a operar (desde BD)"""
        self._cargar_usuarios_de_bd()
        
        if not self.config.lista_usuarios:
            self.vista.mostrar_error("No hay usuarios registrados")
            return False
        
        self.vista.mostrar_lista_usuarios_bd(self.config.lista_usuarios)
        
        try:
            id_usuario = int(input("\n   Seleccione ID de usuario: "))
            for u in self.config.lista_usuarios:
                if u.id_entidad == id_usuario:
                    self.usuario_actual = u
                    self.carrito_actual = Carrito(self.config.generar_id_carrito(), u)
                    self.vista.mostrar_exito(f"Bienvenido {u.nombre}")
                    return True
            self.vista.mostrar_error("Usuario no encontrado")
            return False
        except ValueError:
            self.vista.mostrar_error("ID inválido")
            return False
    
    # ============================================================
    # REGISTRO DE USUARIO
    # ============================================================
    
    def registrar_usuario(self):
        """Registra un nuevo usuario con rol (guarda en BD)"""
        self.vista.mostrar_menu_registro_usuario()
        opcion = input("   Seleccione rol (1-4): ").strip()
        
        roles = {
            "1": "comprador",
            "2": "vendedor_persona",
            "3": "vendedor_empresa",
            "4": "administrador"
        }
        
        if opcion not in roles:
            self.vista.mostrar_error("Rol no válido")
            return
        
        datos = self.vista.leer_datos_usuario()
        
        try:
            # Crear usuario con ID temporal (la BD lo generará)
            usuario = FactoryEntidades.crear_entidad(
                "usuario",
                roles[opcion],
                {
                    "id_entidad": 0,
                    "nombre": datos["nombre"],
                    "correo": datos["correo"],
                    "cedula": datos["cedula"],
                    "ciudad": datos["ciudad"],
                    "telefono": datos["telefono"],
                    "rol": roles[opcion]
                }
            )
            
            if self.facade.guardar_usuario(usuario):
                self.vista.mostrar_exito(f"Usuario {usuario.nombre} registrado en la BD")
                self._cargar_usuarios_de_bd()
            else:
                self.vista.mostrar_error("No se pudo guardar el usuario en la BD")
            
        except Exception as e:
            self.vista.mostrar_error(f"Error: {e}")
    
    # ============================================================
    # LISTAR USUARIOS
    # ============================================================
    
    def listar_usuarios(self):
        """Lista todos los usuarios (solo administradores)"""
        if not self.usuario_actual or not self.usuario_actual.es_administrador():
            self.vista.mostrar_error_permiso("listar usuarios")
            return
        
        self._cargar_usuarios_de_bd()
        self.vista.mostrar_lista_usuarios_bd(self.config.lista_usuarios)
    
    # ============================================================
    # PUBLICAR VEHÍCULO
    # ============================================================
    
    def publicar_vehiculo(self):
        """Publica un vehículo - pregunta NUEVO o USADO dentro"""
        
        if not self.usuario_actual:
            self.vista.mostrar_error("Primero seleccione un usuario")
            return
        
        if not self.usuario_actual.puede_vender_usado() and not self.usuario_actual.puede_vender_nuevo():
            self.vista.mostrar_error_permiso("publicar vehículos")
            return
        
        es_nuevo = self.vista.preguntar_nuevo_o_usado()
        
        if es_nuevo and not self.usuario_actual.puede_vender_nuevo():
            self.vista.mostrar_error_permiso("vender vehículos NUEVOS")
            return
        
        if not es_nuevo and not self.usuario_actual.puede_vender_usado():
            self.vista.mostrar_error_permiso("vender vehículos USADOS")
            return
        
        if es_nuevo:
            print(f"\n   🏭 PUBLICANDO VEHÍCULO NUEVO")
            print(f"   Empresa: {self.usuario_actual.nombre}")
        else:
            print(f"\n   🏠 PUBLICANDO VEHÍCULO USADO")
            print(f"   Vendedor: {self.usuario_actual.nombre}")
        
        tipo = self.vista.preguntar_tipo_vehiculo()
        if tipo not in ["1", "2", "3"]:
            self.vista.mostrar_error("Tipo no válido")
            return
        
        datos = self.vista.leer_datos_vehiculo()
        datos["id_entidad"] = self.config.generar_id_vehiculo()
        datos["estado_vehiculo"] = "DISPONIBLE"
        datos["vendedor"] = self.usuario_actual
        datos["es_nuevo"] = es_nuevo
        
        if tipo == "1":
            datos.update(self.vista.leer_datos_carro())
            vehiculo = FactoryEntidades.crear_entidad("vehiculo", "1", datos)
        elif tipo == "2":
            self.vista.mostrar_advertencia("Motocicletas en desarrollo...")
            return
        elif tipo == "3":
            self.vista.mostrar_advertencia("Patinetas en desarrollo...")
            return
        
        if self.facade.guardar_vehiculo(vehiculo, self.usuario_actual.id_entidad):
            self.config.lista_vehiculos.append(vehiculo)
            nuevo_usado = "NUEVO" if es_nuevo else "USADO"
            self.vista.mostrar_exito(
                f"{'🏭' if es_nuevo else '🏠'} {vehiculo.marca} {vehiculo.modelo} "
                f"({nuevo_usado}) publicado y guardado en BD"
            )
        else:
            self.vista.mostrar_error("No se pudo guardar el vehículo en la BD")
    
    # ============================================================
    # COMPRAR VEHÍCULO
    # ============================================================
    
    def comprar_vehiculo(self):
        """Proceso de compra de un vehículo"""
        if not self.usuario_actual:
            self.vista.mostrar_error("Primero seleccione un usuario")
            return
        
        if not self.usuario_actual.puede_comprar():
            self.vista.mostrar_error_permiso("comprar vehículos")
            return
        
        disponibles = [v for v in self.config.lista_vehiculos 
                      if v.estado_vehiculo == "DISPONIBLE"]
        self.vista.mostrar_catalogo(disponibles)
        
        if not disponibles:
            return
        
        try:
            id_vehiculo = self.vista.seleccionar_vehiculo()
            vehiculo = None
            for v in disponibles:
                if v.id_entidad == id_vehiculo:
                    vehiculo = v
                    break
            
            if not vehiculo:
                self.vista.mostrar_error("Vehículo no encontrado")
                return
            
            self.vista.mostrar_detalle_vehiculo(vehiculo)
            
            if vehiculo.es_nuevo:
                print(f"   🏭 VENDIDO POR: {vehiculo.vendedor.nombre} (Empresa)")
            else:
                print(f"   🏠 VENDIDO POR: {vehiculo.vendedor.nombre} (Particular)")
            
            if self.vista.confirmar_compra(vehiculo):
                self.carrito_actual.agregar_vehiculo(vehiculo)
                self.vista.mostrar_exito(f"Vehículo agregado al carrito")
                
                if input("\n   ¿Finalizar compra ahora? (s/n): ").lower() in ("s", "si", "sí"):
                    self.finalizar_compra()
        except ValueError:
            self.vista.mostrar_error("ID inválido")
    
    # ============================================================
    # CARRITO Y PEDIDOS
    # ============================================================
    
    def ver_carrito(self):
        if not self.usuario_actual:
            self.vista.mostrar_error("Primero seleccione un usuario")
            return
        
        if not self.usuario_actual.puede_comprar():
            self.vista.mostrar_error("Los Vendedores Empresa no tienen carrito (solo venden)")
            return
        
        self.vista.mostrar_carrito(self.carrito_actual)
    
    def ver_mis_pedidos(self):
        if not self.usuario_actual:
            self.vista.mostrar_error("Primero seleccione un usuario")
            return
        
        if not self.usuario_actual.puede_comprar():
            self.vista.mostrar_error("Los Vendedores Empresa no tienen pedidos (solo venden)")
            return
        
        pedidos_usuario = [p for p in self.config.lista_pedidos 
                          if p.usuario.id_entidad == self.usuario_actual.id_entidad]
        self.vista.mostrar_mis_pedidos(pedidos_usuario)
    
    def finalizar_compra(self):
        if self.carrito_actual.esta_vacio():
            self.vista.mostrar_error("El carrito está vacío")
            return
        
        self.vista.mostrar_carrito(self.carrito_actual)
        
        if input("\n   ¿Confirmar pedido? (s/n): ").lower() in ("s", "si", "sí"):
            pedido = Pedido(
                id_entidad=self.config.generar_id_pedido(),
                usuario=self.usuario_actual,
                items=self.carrito_actual.items.copy(),
                total=self.carrito_actual.total
            )
            pedido.confirmar()
            self.config.lista_pedidos.append(pedido)
            self.carrito_actual.vaciar()
            self.vista.mostrar_resumen_pedido(pedido)
            self.vista.mostrar_exito("¡Compra exitosa!")
    
    # ============================================================
    # CATÁLOGO
    # ============================================================
    
    def ver_catalogo(self):
        disponibles = [v for v in self.config.lista_vehiculos 
                      if v.estado_vehiculo == "DISPONIBLE"]
        self.vista.mostrar_catalogo(disponibles)
    
    def ver_mis_vehiculos(self):
        if not self.usuario_actual:
            self.vista.mostrar_error("Primero seleccione un usuario")
            return
        
        if not self.usuario_actual.puede_vender_usado():
            self.vista.mostrar_error("No eres vendedor")
            return
        
        mis_vehiculos = [v for v in self.config.lista_vehiculos 
                        if v.vendedor.id_entidad == self.usuario_actual.id_entidad]
        self.vista.mostrar_mis_vehiculos(mis_vehiculos, self.usuario_actual.nombre)
    
    def mostrar_configuracion(self):
        if not self.usuario_actual or not self.usuario_actual.es_administrador():
            self.vista.mostrar_error_permiso("ver configuración")
            return
        self.vista.mostrar_configuracion(self.config)
        self.vista.mostrar_resumen_memoria(self.config)