Para que funcione correctamente todo, ejecutar los siguientes comandos:

docker-compose down -v
chmod 644 Peliculas.sql
chown ciber2:ciber2 Peliculas.sql
docker-compose up --build
