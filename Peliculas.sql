CREATE DATABASE IF NOT EXISTS ciber;
CREATE USER 'user'@'%' IDENTIFIED BY 'userpw';
GRANT ALL PRIVILEGES ON ciber.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE ciber;
CREATE TABLE peliculas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255),
    reparto VARCHAR(255)
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    correo VARCHAR(255) NOT NULL,
    fechaUltimoAcceso DATE,
    fechaBloqueo DATE,
    numeroAccesosErroneo INTEGER,
    debeCambiarClave BOOLEAN
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`,`estado`, `correo`,`numeroAccesosErroneo`,`fechaUltimoAcceso`) VALUES ('root','$2b$10$hJtLt4u0SqSf.h3S5Uuev.nu98ARhn.6SpvFCYbc1eeynJmy81cmK', 'admin', 'activo','root@pp.es', 0, '2022-03-01 00:00');
INSERT INTO peliculas (nombre, descripcion, precio, foto, reparto) VALUES
('Batman', 'Batman en Gotham', 9.99, 'https://via.placeholder.com/70x100?text=Inception', 'Batman, Catwoman'),
('Superman', 'Superman que vuela que te cagas', 11.50, 'https://via.placeholder.com/70x100?text=Interstellar', 'Superman, Superwoman'),
('Spiderman', 'Spiderman que se pega por las paredes', 8.75, 'https://via.placeholder.com/70x100?text=Matrix', 'Spiderman, Tio Ben');