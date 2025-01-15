Para que funcione correctamente todo, copiar y pegar el siguiente one-liner:

docker-compose down -v;
chmod 644 Peliculas.sql;
chown ciber2:ciber2 Peliculas.sql;
docker-compose up --build
