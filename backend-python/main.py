# =============================================================================
# PUNTO DE ENTRADA - EVIA MARKETPLACE CON BASE DE DATOS
# Archivo: main.py (RAÍZ DEL PROYECTO)
# =============================================================================

from views.Vista_Usuario import VistaUsuario
from controllers.Sistema_Controller import SistemaController


def main():
    """Función principal del sistema"""
    
    # Crear vista y controlador
    vista = VistaUsuario()
    controlador = SistemaController(vista)
    
    # Bienvenida
    vista.mostrar_bienvenida()
    
    # Ciclo principal
    while True:
        vista.mostrar_menu_principal(controlador.usuario_actual)
        opcion = input("   Seleccione una opción: ").strip()
        
        # ============================================================
        # SIN USUARIO LOGUEADO
        # ============================================================
        if not controlador.usuario_actual:
            if opcion == "1":
                controlador.ver_catalogo()
            elif opcion == "2":
                controlador.registrar_usuario()
            elif opcion == "3":
                controlador.seleccionar_usuario()
            elif opcion == "0":
                vista.mostrar_despedida()
                break
            else:
                vista.mostrar_error("Opción no válida")
            vista.pausar()
            continue
        
        # ============================================================
        # COMPRADOR
        # ============================================================
        if controlador.usuario_actual.es_comprador():
            if opcion == "1":
                controlador.ver_catalogo()
            elif opcion == "2":
                controlador.comprar_vehiculo()
            elif opcion == "3":
                controlador.ver_carrito()
            elif opcion == "4":
                controlador.ver_mis_pedidos()
            elif opcion == "0":
                controlador.cerrar_sesion()
                vista.mostrar_exito("Sesión cerrada")
            else:
                vista.mostrar_error("Opción no válida")
        
        # ============================================================
        # VENDEDOR PARTICULAR
        # ============================================================
        elif controlador.usuario_actual.es_vendedor_persona():
            if opcion == "1":
                controlador.ver_catalogo()
            elif opcion == "2":
                controlador.comprar_vehiculo()
            elif opcion == "3":
                controlador.publicar_vehiculo()
            elif opcion == "4":
                controlador.ver_carrito()
            elif opcion == "5":
                controlador.ver_mis_pedidos()
            elif opcion == "6":
                controlador.ver_mis_vehiculos()
            elif opcion == "0":
                controlador.cerrar_sesion()
                vista.mostrar_exito("Sesión cerrada")
            else:
                vista.mostrar_error("Opción no válida")
        
        # ============================================================
        # VENDEDOR EMPRESA
        # ============================================================
        elif controlador.usuario_actual.es_vendedor_empresa():
            if opcion == "1":
                controlador.ver_catalogo()
            elif opcion == "2":
                controlador.publicar_vehiculo()
            elif opcion == "3":
                controlador.ver_mis_vehiculos()
            elif opcion == "4":
                vista.mostrar_advertencia("Dashboard en desarrollo...")
            elif opcion == "0":
                controlador.cerrar_sesion()
                vista.mostrar_exito("Sesión cerrada")
            else:
                vista.mostrar_error("Opción no válida")
        
        # ============================================================
        # ADMINISTRADOR
        # ============================================================
        elif controlador.usuario_actual.es_administrador():
            if opcion == "1":
                controlador.ver_catalogo()
            elif opcion == "2":
                controlador.comprar_vehiculo()
            elif opcion == "3":
                controlador.publicar_vehiculo()
            elif opcion == "4":
                controlador.listar_usuarios()
            elif opcion == "5":
                controlador.ver_catalogo()
            elif opcion == "6":
                vista.mostrar_advertencia("Dashboard General en desarrollo...")
            elif opcion == "7":
                controlador.mostrar_configuracion()
            elif opcion == "0":
                controlador.cerrar_sesion()
                vista.mostrar_exito("Sesión cerrada")
            else:
                vista.mostrar_error("Opción no válida")
        
        vista.pausar()


if __name__ == "__main__":
    main()