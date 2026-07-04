-- =============================================================================
-- BASE DE DATOS: bd_evia
-- SISTEMA: EVIA Marketplace de Vehículos Eléctricos
-- =============================================================================

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- =============================================================================
-- CREAR BASE DE DATOS
-- =============================================================================
CREATE DATABASE IF NOT EXISTS `bd_evia` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_evia`;

-- =============================================================================
-- TABLA: usuarios
-- =============================================================================
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `identificacion_usuario` varchar(30) NOT NULL,
  `nombre_usuario` varchar(120) NOT NULL,
  `correo_usuario` varchar(120) NOT NULL,
  `ciudad_usuario` varchar(100) DEFAULT NULL,
  `telefono_usuario` varchar(20) DEFAULT NULL,
  `rol_usuario` varchar(40) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `identificacion_usuario` (`identificacion_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =============================================================================
-- TABLA: vehiculos
-- =============================================================================
DROP TABLE IF EXISTS `vehiculos`;
CREATE TABLE IF NOT EXISTS `vehiculos` (
  `id_vehiculo` int(11) NOT NULL AUTO_INCREMENT,
  `id_vendedor` int(11) NOT NULL,
  `tipo_vehiculo` varchar(30) NOT NULL,
  `marca` varchar(60) NOT NULL,
  `modelo` varchar(60) NOT NULL,
  `precio` decimal(15,2) NOT NULL,
  `autonomia_km` int(11) DEFAULT NULL,
  `capacidad_bateria_kwh` decimal(10,2) DEFAULT NULL,
  `peso_kg` decimal(10,2) DEFAULT NULL,
  `velocidad_maxima` int(11) DEFAULT NULL,
  `tipo_conector` varchar(30) DEFAULT NULL,
  `garantia_meses` int(11) DEFAULT NULL,
  `año` int(11) DEFAULT NULL,
  `es_nuevo` tinyint(1) DEFAULT 1,
  `estado_vehiculo` varchar(30) DEFAULT 'DISPONIBLE',
  `fecha_publicacion` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id_vehiculo`),
  KEY `id_vendedor` (`id_vendedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =============================================================================
-- TABLA: pedidos
-- =============================================================================
DROP TABLE IF EXISTS `pedidos`;
CREATE TABLE IF NOT EXISTS `pedidos` (
  `id_pedido` int(11) NOT NULL AUTO_INCREMENT,
  `id_comprador` int(11) NOT NULL,
  `total` decimal(15,2) NOT NULL,
  `fecha_pedido` datetime DEFAULT current_timestamp(),
  `estado_pedido` varchar(30) DEFAULT 'PENDIENTE',
  PRIMARY KEY (`id_pedido`),
  KEY `id_comprador` (`id_comprador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =============================================================================
-- TABLA: detalle_pedido
-- =============================================================================
DROP TABLE IF EXISTS `detalle_pedido`;
CREATE TABLE IF NOT EXISTS `detalle_pedido` (
  `id_detalle` int(11) NOT NULL AUTO_INCREMENT,
  `id_pedido` int(11) NOT NULL,
  `id_vehiculo` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT 1,
  `precio_unitario` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id_detalle`),
  KEY `id_pedido` (`id_pedido`),
  KEY `id_vehiculo` (`id_vehiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =============================================================================
-- RESTRICCIONES (CLAVES FORÁNEAS)
-- =============================================================================
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`id_vendedor`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`id_comprador`) REFERENCES `usuarios` (`id_usuario`);

ALTER TABLE `detalle_pedido`
  ADD CONSTRAINT `detalle_pedido_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`),
  ADD CONSTRAINT `detalle_pedido_ibfk_2` FOREIGN KEY (`id_vehiculo`) REFERENCES `vehiculos` (`id_vehiculo`);

-- =============================================================================
-- FIN DE LA ESTRUCTURA
-- =============================================================================
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;