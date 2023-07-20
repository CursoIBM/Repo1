-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-04-2018 a las 01:37:48
-- Versión del servidor: 10.1.31-MariaDB
-- Versión de PHP: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `curso_sql`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos_pedidos`
--

CREATE TABLE `productos_pedidos` (
  `NUMERO_PEDIDO` int(2) DEFAULT NULL,
  `CODIGO_ARTICULO` varchar(4) DEFAULT NULL,
  `UNIDADES` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `productos_pedidos`
--

INSERT INTO `productos_pedidos` (`NUMERO_PEDIDO`, `CODIGO_ARTICULO`, `UNIDADES`) VALUES
(1, 'AR01', 11),
(1, 'AR04', 10),
(1, 'AR15', 4),
(1, 'AR22', 18),
(3, 'AR02', 20),
(3, 'AR22', 3),
(5, 'AR04', 16),
(7, 'AR06', 16),
(8, 'AR02', 6),
(8, 'AR06', 5),
(8, 'AR07', 6),
(8, 'AR10', 2),
(8, 'AR12', 30),
(8, 'AR15', 15),
(8, 'AR18', 20),
(8, 'AR19', 18),
(8, 'AR25', 5),
(8, 'AR32', 15),
(8, 'AR33', 18),
(8, 'AR34', 5),
(8, 'AR35', 24),
(9, 'AR06', 14),
(11, 'AR08', 1),
(12, 'AR08', 12),
(13, 'AR08', 8),
(16, 'AR10', 17),
(19, 'AR13', 4),
(21, 'AR15', 11),
(22, 'AR17', 6),
(22, 'AR26', 4),
(22, 'AR28', 21),
(25, 'AR19', 12),
(26, 'AR19', 12),
(27, 'AR21', 11),
(28, 'AR21', 22),
(29, 'AR22', 12),
(30, 'AR23', 33),
(31, 'AR24', 31),
(32, 'AR25', 11),
(34, 'AR22', 7),
(34, 'AR27', 3),
(35, 'AR22', 9),
(35, 'AR27', 12),
(37, 'AR27', 11),
(39, 'AR29', 22),
(40, 'AR30', 1),
(42, 'AR31', 21),
(43, 'AR32', 3),
(44, 'AR22', 22),
(45, 'AR36', 21),
(46, 'AR37', 8),
(47, 'AR38', 12),
(48, 'AR38', 13),
(49, 'AR39', 13),
(50, 'AR39', 1),
(14, 'C002', 100),
(1, 'AR01', 11);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos_pedidos`
--
ALTER TABLE `productos_pedidos`
  ADD KEY `NUMERO_PEDIDO` (`NUMERO_PEDIDO`),
  ADD KEY `CODIGO_ARTICULO` (`CODIGO_ARTICULO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
