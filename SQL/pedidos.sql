-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-04-2018 a las 01:37:36
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
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `NUMERO_PEDIDO` int(4) NOT NULL,
  `CODIGO_CLIENTE` varchar(4) DEFAULT NULL,
  `FECHA_PEDIDO` date DEFAULT NULL,
  `FORMA_PAGO` varchar(8) DEFAULT NULL,
  `DESCUENTO` int(4) DEFAULT NULL,
  `ENVIADO` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `pedidos`
--

INSERT INTO `pedidos` (`NUMERO_PEDIDO`, `CODIGO_CLIENTE`, `FECHA_PEDIDO`, `FORMA_PAGO`, `DESCUENTO`, `ENVIADO`) VALUES
(1, 'CT01', '2013-03-12', 'TARJETA', 0, 'SI'),
(2, 'CT02', '2013-02-19', 'EFECTIVO', 0, 'NO'),
(3, 'CT03', '2017-03-02', 'TARJETA', 0, 'SI'),
(4, 'CT04', '2018-02-05', 'EFECTIVO', 0, 'SI'),
(5, 'CT01', '2018-03-29', 'TARJETA', 0, 'SI'),
(6, 'CT03', '2018-01-01', 'EFECTIVO', 0, 'SI'),
(7, 'CT01', '2017-10-08', 'EFECTIVO', 0, 'SI'),
(8, 'CT02', '2017-03-06', 'EFECTIVO', 0, 'SI'),
(9, 'CT05', '2016-11-21', 'EFECTIVO', 0, 'SI'),
(10, 'CT06', '2017-07-12', 'EFECTIVO', 0, 'SI'),
(11, 'CT07', '2014-03-05', 'EFECTIVO', 0, 'SI'),
(12, 'CT08', '2013-02-08', 'EFECTIVO', 0, 'SI'),
(13, 'CT09', '2012-01-21', 'EFECTIVO', 0, 'SI'),
(14, 'CT10', '2014-11-15', 'EFECTIVO', 0, 'SI');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`NUMERO_PEDIDO`),
  ADD KEY `CODIGO_CLIENTE` (`CODIGO_CLIENTE`),
  ADD KEY `NUMERO_PEDIDO` (`NUMERO_PEDIDO`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
