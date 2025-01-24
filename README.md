\Para que funcione correctamente todo, copiar y pegar el siguiente one-liner:

```bash
docker-compose down -v; chmod -R 755 *; chmod 644 Peliculas.sql; chown $USER:$USER Peliculas.sql; docker-compose up --build
```
Accedemos a la web con el enlace http://localhost:9094/static/index.html
