# =============================================================================
# VISTA: INTERFAZ DE USUARIO - CON BASE DE DATOS
# Archivo: views/Vista_Usuario.py
# =============================================================================

LINEA = "=" * 55


class VistaUsuario:
    """Vista del sistema - Toda la interacción con el usuario"""
    
    # ============================================================
    # MENÚS PRINCIPALES
    # ============================================================
    
    def mostrar_bienvenida(self):
        print(f"\n{LINEA}")
        print("         ⚡ EVIA - MARKETPLACE ELÉCTRICO")
        print("      Compra y vende vehículos eléctricos")
        print(f"{LINEA}")
    
    def mostrar_menu_principal(self, usuario_actual=None):
        """Menú DINÁMICO según el rol del usuario"""
        
        print(f"\n{LINEA}")
        print("                    MENÚ PRINCIPAL")
        print(f"{LINEA}")
        
        if usuario_actual:
            print(f"   👤 {usuario_actual.nombre}")
            print(f"   📌 Rol: {usuario_actual.tipo_usuario}")
            print(f"{LINEA}")
        
        print("   1. 🚗 Ver Catálogo de Vehículos")
        
        if usuario_actual:
            if usuario_actual.es_comprador():
                print("   2. 🛒 Comprar Vehículo")
                print("   3. 🛍️  Mi Carrito")
                print("   4. 📦 Mis Pedidos")
            
            elif usuario_actual.es_vendedor_persona():
                print("   2. 🛒 Comprar Vehículo")
                print("   3. 📝 Publicar Vehículo")
                print("   4. 🛍️  Mi Carrito")
                print("   5. 📦 Mis Pedidos")
                print("   6. 📋 Mis Vehículos Publicados")
            
            elif usuario_actual.es_vendedor_empresa():
                print("   2. 📝 Publicar Vehículo")
                print("   3. 📋 Mis Vehículos Publicados")
                print("   4. 📊 Mi Dashboard de Ventas")
            
            elif usuario_actual.es_administrador():
                print("   2. 🛒 Comprar Vehículo")
                print("   3. 📝 Publicar Vehículo")
                print("   4. 👥 Gestionar Usuarios")
                print("   5. 📋 Ver Todos los Vehículos")
                print("   6. 📊 Dashboard General")
                print("   7. ⚙️  Configuración del Sistema")
        
        else:
            print("   2. 👤 Registrar Usuario")
            print("   3. 🔑 Seleccionar Usuario")
        
        print(f"{LINEA}")
        print("   0. 🚪 Salir")
        print(f"{LINEA}")
    
    # ============================================================
    # REGISTRO DE USUARIO
    # ============================================================
    
    def mostrar_menu_registro_usuario(self):
        print(f"\n{LINEA}")
        print("              👤 REGISTRO DE USUARIO")
        print(f"{LINEA}")
        print("   Roles disponibles:")
        print("   1. Comprador (solo compra)")
        print("   2. Vendedor Particular (compra + vende usado)")
        print("   3. Vendedor Empresa (solo vende: nuevo y usado)")
        print("   4. Administrador (hace todo)")
    
    def leer_datos_usuario(self):
        return {
            "nombre": input("   Nombre completo: ").strip(),
            "correo": input("   Correo electrónico: ").strip(),
            "cedula": input("   Cédula/NIT: ").strip(),
            "ciudad": input("   Ciudad: ").strip(),
            "telefono": input("   Teléfono: ").strip()
        }
    
    # ============================================================
    # LISTAR USUARIOS DESDE BD
    # ============================================================
    
    def mostrar_lista_usuarios_bd(self, lista_usuarios):
        """Muestra los usuarios registrados en la base de datos"""
        print(f"\n{LINEA}")
        print("              👥 USUARIOS REGISTRADOS (BD)")
        print(f"{LINEA}")
        
        if not lista_usuarios:
            print("   No hay usuarios registrados en la base de datos")
            return
        
        for u in lista_usuarios:
            print(f"   ID: {u.id_entidad} | {u.nombre} | {u.tipo_usuario} | {u.ciudad}")
    
    # ============================================================
    # PUBLICAR VEHÍCULO
    # ============================================================
    
    def preguntar_nuevo_o_usado(self):
        """Pregunta si el vehículo es NUEVO o USADO"""
        print("\n   ¿El vehículo es NUEVO o USADO?")
        print("   1. 🆕 NUEVO (de fábrica)")
        print("   2. 🔄 USADO (segunda mano)")
        opcion = input("   Seleccione (1-2): ").strip()
        return opcion == "1"
    
    def preguntar_tipo_vehiculo(self):
        print("\n   ¿Qué tipo de vehículo desea publicar?")
        print("   1. Carro")
        print("   2. Motocicleta")
        print("   3. Patineta")
        return input("   Seleccione (1-3): ").strip()
    
    def leer_datos_vehiculo(self):
        print("\n   --- DATOS DEL VEHÍCULO ---")
        return {
            "marca": input("   Marca: ").strip(),
            "modelo": input("   Modelo: ").strip(),
            "precio": float(input("   Precio (COP $): ").strip()),
            "autonomia_km": int(input("   Autonomía (km): ").strip()),
            "capacidad_bateria_kwh": float(input("   Batería (kWh): ").strip()),
            "peso_kg": float(input("   Peso (kg): ").strip()),
            "velocidad_maxima": int(input("   Velocidad máxima (km/h): ").strip()),
            "tipo_conector": input("   Tipo de conector: ").strip(),
            "garantia_meses": int(input("   Garantía (meses): ").strip()),
            "año": int(input("   Año del vehículo: ").strip()),
        }
    
    def leer_datos_carro(self):
        return {
            "num_puertas": int(input("   Número de puertas: ").strip()),
            "tipo_traccion": input("   Tipo de tracción (AWD, FWD, RWD): ").strip()
        }
    
    # ============================================================
    # CATÁLOGO Y COMPRA
    # ============================================================
    
    def mostrar_catalogo(self, vehiculos):
        """Muestra el catálogo separando NUEVOS y USADOS"""
        print(f"\n{LINEA}")
        print("                🚗 CATÁLOGO DE VEHÍCULOS")
        print(f"{LINEA}")
        
        if not vehiculos:
            print("   No hay vehículos disponibles")
            return
        
        nuevos = [v for v in vehiculos if v.es_nuevo and v.estado_vehiculo == "DISPONIBLE"]
        usados = [v for v in vehiculos if not v.es_nuevo and v.estado_vehiculo == "DISPONIBLE"]
        
        if nuevos:
            print("\n   🆕 VEHÍCULOS NUEVOS")
            print("   " + "-" * 40)
            for v in nuevos:
                print(f"   ID: {v.id_entidad} | {v.marca} {v.modelo} ({v.año}) | ${v.precio:,.0f}")
        
        if usados:
            print("\n   🔄 VEHÍCULOS USADOS")
            print("   " + "-" * 40)
            for v in usados:
                print(f"   ID: {v.id_entidad} | {v.marca} {v.modelo} ({v.año}) | ${v.precio:,.0f}")
        
        if not nuevos and not usados:
            print("   No hay vehículos disponibles")
        
        print(f"\n   Total de vehículos disponibles: {len(nuevos) + len(usados)}")
    
    def mostrar_detalle_vehiculo(self, vehiculo):
        print(vehiculo.obtener_especificaciones())
    
    def seleccionar_vehiculo(self):
        return int(input("\n   Ingrese el ID del vehículo: ").strip())
    
    def confirmar_compra(self, vehiculo):
        print(f"\n   ¿Confirma la compra de {vehiculo.marca} {vehiculo.modelo}?")
        print(f"   Precio: ${vehiculo.precio:,.0f} COP")
        respuesta = input("   (s/n): ").strip().lower()
        return respuesta in ("s", "si", "sí")
    
    # ============================================================
    # CARRITO Y PEDIDOS
    # ============================================================
    
    def mostrar_carrito(self, carrito):
        print(f"\n{LINEA}")
        print("              🛍️  MI CARRITO")
        print(f"{LINEA}")
        
        if carrito.esta_vacio():
            print("   El carrito está vacío")
            return
        
        for v in carrito.items:
            nuevo_usado = "NUEVO" if v.es_nuevo else "USADO"
            print(f"   - {v.marca} {v.modelo} ({nuevo_usado}) - ${v.precio:,.0f}")
        
        print(f"\n   TOTAL: ${carrito.total:,.0f} COP")
        print(f"{LINEA}")
    
    def mostrar_resumen_pedido(self, pedido):
        print(f"\n{LINEA}")
        print("              📦 RESUMEN DEL PEDIDO")
        print(f"{LINEA}")
        print(f"   Pedido #{pedido.id_entidad}")
        print(f"   Comprador: {pedido.usuario.nombre}")
        print(f"   Fecha: {pedido.fecha.strftime('%d/%m/%Y %H:%M')}")
        print(f"   Estado: {pedido.estado}")
        print("\n   Vehículos:")
        for v in pedido.items:
            nuevo_usado = "NUEVO" if v.es_nuevo else "USADO"
            print(f"   - {v.marca} {v.modelo} ({nuevo_usado}) - ${v.precio:,.0f}")
        print(f"\n   TOTAL: ${pedido.total:,.0f} COP")
        print(f"{LINEA}")
    
    def mostrar_mis_pedidos(self, pedidos):
        print(f"\n{LINEA}")
        print("              📦 MIS PEDIDOS")
        print(f"{LINEA}")
        
        if not pedidos:
            print("   No tienes pedidos")
            return
        
        for p in pedidos:
            print(f"\n   Pedido #{p.id_entidad} | Estado: {p.estado} | Total: ${p.total:,.0f}")
            for v in p.items:
                print(f"   - {v.marca} {v.modelo}")
    
    # ============================================================
    # LISTADOS
    # ============================================================
    
    def mostrar_lista_usuarios(self, usuarios):
        print(f"\n{LINEA}")
        print("              👥 USUARIOS REGISTRADOS")
        print(f"{LINEA}")
        
        if not usuarios:
            print("   No hay usuarios registrados")
            return
        
        for u in usuarios:
            print(f"   ID: {u.id_entidad} | {u.nombre} | {u.tipo_usuario}")
    
    def mostrar_mis_vehiculos(self, vehiculos, nombre_usuario):
        print(f"\n{LINEA}")
        print(f"            📋 VEHÍCULOS PUBLICADOS POR {nombre_usuario}")
        print(f"{LINEA}")
        
        if not vehiculos:
            print("   No has publicado ningún vehículo")
            return
        
        for v in vehiculos:
            nuevo_usado = "NUEVO" if v.es_nuevo else "USADO"
            print(f"   ID: {v.id_entidad} | {v.marca} {v.modelo} ({nuevo_usado}) | {v.estado_vehiculo}")
    
    def mostrar_configuracion(self, config):
        print(f"\n{LINEA}")
        print("              ℹ️  CONFIGURACIÓN DEL SISTEMA")
        print(f"{LINEA}")
        print(f"   Nombre: {config.nombre_sistema}")
        print(f"   Versión: {config.version_sistema}")
        print(f"   Institución: {config.institucion}")
        print(f"{LINEA}")
    
    def mostrar_resumen_memoria(self, config):
        print(f"\n   📊 ESTADO DEL SISTEMA")
        print(f"   Usuarios en memoria: {len(config.lista_usuarios)}")
        print(f"   Vehículos en memoria: {len(config.lista_vehiculos)}")
        print(f"   Pedidos en memoria: {len(config.lista_pedidos)}")
    
    # ============================================================
    # MENSAJES
    # ============================================================
    
    def mostrar_exito(self, mensaje):
        print(f"\n✅ {mensaje}")
    
    def mostrar_error(self, mensaje):
        print(f"\n❌ {mensaje}")
    
    def mostrar_error_permiso(self, accion):
        print(f"\n❌ No tienes permiso para {accion}")
    
    def mostrar_advertencia(self, mensaje):
        print(f"\n⚠️ {mensaje}")
    
    def mostrar_despedida(self):
        print(f"\n{LINEA}")
        print("   Gracias por usar EVIA. ¡Hasta pronto! ⚡")
        print(f"{LINEA}")
    
    def pausar(self):
        input("\n   Presione Enter para continuar...")