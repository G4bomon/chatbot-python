-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-03-2023 a las 13:59:34
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `preguntas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `respuestas`
--

CREATE TABLE `respuestas` (
  `id` int(11) NOT NULL,
  `resultados` varchar(240) NOT NULL,
  `Palabra_1` varchar(15) NOT NULL,
  `Palabra_2` varchar(15) DEFAULT NULL,
  `Palabra_3` varchar(15) DEFAULT NULL,
  `Palabra_4` varchar(15) DEFAULT NULL,
  `Palabra_5` varchar(15) DEFAULT NULL,
  `Palabra_6` varchar(15) DEFAULT NULL,
  `Palabra_7` varchar(15) DEFAULT NULL,
  `Palabra_8` varchar(15) DEFAULT NULL,
  `Palabra_9` varchar(15) DEFAULT NULL,
  `Palabra_10` varchar(15) DEFAULT NULL,
  `single_response` varchar(5) NOT NULL,
  `required_words` varchar(24) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `respuestas`
--

INSERT INTO `respuestas` (`id`, `resultados`, `Palabra_1`, `Palabra_2`, `Palabra_3`, `Palabra_4`, `Palabra_5`, `Palabra_6`, `Palabra_7`, `Palabra_8`, `Palabra_9`, `Palabra_10`, `single_response`, `required_words`) VALUES
(1, 'Hola', 'hola', 'saludos', 'buenas', 'klk', NULL, NULL, NULL, NULL, NULL, NULL, 'True', NULL),
(2, 'estoy bien y tu?', 'como', 'estas', 'va', 'vas', 'sientes', NULL, NULL, NULL, NULL, NULL, 'False', 'como'),
(3, 'Estamos ubicados en la calle 23 numero 123', 'ubicados', 'direccion', 'donde', 'ubicacion', NULL, NULL, NULL, NULL, NULL, NULL, 'True', NULL),
(4, 'Siempre a la orden', 'gracias', 'te lo agradezco', 'thanks', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'True', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `respuestas`
--
ALTER TABLE `respuestas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `respuestas`
--
ALTER TABLE `respuestas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
