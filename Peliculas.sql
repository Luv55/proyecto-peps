-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 04-04-2025 a las 09:47:08
-- Versión del servidor: 10.3.39-MariaDB-1:10.3.39+maria~ubu2004
-- Versión de PHP: 8.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ciber`
--
CREATE DATABASE IF NOT EXISTS `ciber` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `ciber`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peliculas`
--

CREATE TABLE `peliculas` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `precio` decimal(9,2) NOT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `reparto` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `peliculas`
--

INSERT INTO `peliculas` (`id`, `nombre`, `descripcion`, `precio`, `foto`, `reparto`) VALUES
(1, 'Batman', 'Batman en Gotham', 9.99, 'https://via.placeholder.com/70x100?text=Inception', 'Batman, Catwoman'),
(2, 'Superman', 'Superman que vuela que te cagas', 11.50, 'https://via.placeholder.com/70x100?text=Interstellar', 'Superman, Superwoman'),
(3, 'Spiderman', 'Spiderman que se pega por las paredes', 8.75, 'https://via.placeholder.com/70x100?text=Matrix', 'Spiderman, Tio Ben');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario` varchar(100) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `perfil` varchar(100) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `fechaUltimoAcceso` date DEFAULT NULL,
  `fechaBloqueo` date DEFAULT NULL,
  `numeroAccesosErroneo` int(11) DEFAULT NULL,
  `debeCambiarClave` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `estado`, `correo`, `fechaUltimoAcceso`, `fechaBloqueo`, `numeroAccesosErroneo`, `debeCambiarClave`) VALUES
('root', '$2b$10$hJtLt4u0SqSf.h3S5Uuev.nu98ARhn.6SpvFCYbc1eeynJmy81cmK', 'admin', 'activo', 'root@pp.es', '2025-04-04', NULL, 0, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `peliculas`
--
ALTER TABLE `peliculas`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;