CREATE DATABASE IF NOT EXISTS PEPS;
USE PEPS;
CREATE TABLE peliculas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255)
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `fechaUltimoAcceso`) VALUES ('root', '1234', 'admin', '2022-03-01');
INSERT INTO `peliculas` (`id`, `nombre`, `descripcion`, `precio`, `foto`) VALUES ('1', 'Spiderman', 'Nueva pelicula de Spiderman', '5', 'https://img2.rtve.es/i/?w=1600&i=1442912664626.jpg');
INSERT INTO `peliculas` (`id`, `nombre`, `descripcion`, `precio`, `foto`) VALUES ('2', 'Batman', 'Nueva pelicula de Batman', '5', 'https://statics.forbesargentina.com/2022/06/629f81fe391f3.jpg');
INSERT INTO `peliculas` (`id`, `nombre`, `descripcion`, `precio`, `foto`) VALUES ('3', 'Superman', 'Nueva pelicula de Superman', '5', 'https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2022/08/03/16595421832009.jpg');