-- =============================================================================
-- DATOS DE EJEMPLO PARA EVIA
-- Base de datos: bd_evia
-- =============================================================================

USE `bd_evia`;

-- =============================================================================
-- USUARIOS
-- =============================================================================
INSERT INTO `usuarios` (`id_usuario`, `identificacion_usuario`, `nombre_usuario`, `correo_usuario`, `ciudad_usuario`, `telefono_usuario`, `rol_usuario`) VALUES
(1, '100001', 'Usuario de prueba', 'prueba@evia.com', 'Bogotá', '3001112233', 'comprador'),
(2, '200001', 'Carlos Vendedor', 'carlos@evia.com', 'Medellín', '3002223344', 'vendedor_persona'),
(3, '300001', 'Tesla Colombia', 'ventas@tesla.com', 'Bogotá', '6015551234', 'vendedor_empresa'),
(4, '123456789', 'Daniela Gil', 'daniela@hotmail.com', 'Bogota', '321654897', 'administrador'),
(5, '123459876', 'Luis sanabria', 'luis@hotmail.com', 'bogota', '325164987', 'comprador');

-- =============================================================================
-- VEHÍCULOS (Ejemplos)
-- =============================================================================
INSERT INTO `vehiculos` (`id_vendedor`, `tipo_vehiculo`, `marca`, `modelo`, `precio`, `autonomia_km`, `capacidad_bateria_kwh`, `peso_kg`, `velocidad_maxima`, `tipo_conector`, `garantia_meses`, `año`, `es_nuevo`, `estado_vehiculo`) VALUES
(3, 'CARRO', 'Tesla', 'Model 3', 180000000, 500, 75, 1800, 220, 'CCS', 48, 2024, 1, 'DISPONIBLE'),
(3, 'CARRO', 'Nissan', 'Leaf', 120000000, 350, 60, 1600, 150, 'CHAdeMO', 36, 2024, 1, 'DISPONIBLE'),
(3, 'CARRO', 'Renault', 'Zoe', 95000000, 400, 52, 1500, 140, 'CCS', 36, 2023, 1, 'DISPONIBLE'),
(2, 'CARRO', 'Tesla', 'Model S', 85000000, 420, 85, 2100, 200, 'CCS', 12, 2020, 0, 'DISPONIBLE'),
(2, 'CARRO', 'Nissan', 'Leaf', 45000000, 250, 40, 1500, 130, 'CHAdeMO', 6, 2019, 0, 'DISPONIBLE');

-- =============================================================================
-- FIN DE DATOS
-- =============================================================================