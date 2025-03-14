from bd import obtener_conexion
from __main__ import app
from funciones_auxiliares import sanitize_input
import sys

def insertar_pelicula(nombre, descripcion, precio,foto,ingredientes):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO peliculas(nombre, descripcion, precio,foto,ingredientes) VALUES (%s, %s, %s,%s,%s)",
                       (nombre, descripcion, precio,foto,ingredientes))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret = {"status": "Failure" }
        code=200
        conexion.commit()
        conexion.close()
    except:
        app.logger.info("Excepcion al insertar un juego")
        ret = {"status": "Failure" }
        code=500
    return ret,code

def convertir_pelicula_a_json(pelicula):
    d = {}
    d['id'] = pelicula[0]
    d['nombre'] = sanitize_input(pelicula[1])
    d['descripcion'] = sanitize_input(pelicula[2])
    d['precio'] = pelicula[3]
    d['foto'] = sanitize_input(pelicula[4])
    d['ingredientes']=sanitize_input(pelicula[5])
    return d

def obtener_peliculas():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto,ingredientes FROM peliculas")
            peliculas = cursor.fetchall()
            peliculasjson=[]
            if peliculas:
                for pelicula in peliculas:
                    peliculasjson.append(convertir_pelicula_a_json(pelicula))
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al obtener las peliculas")
        peliculasjson=[]
        code=500
    return peliculasjson,code

def obtener_pelicula_por_id(id):
    peliculajson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto,ingredientes FROM peliculas WHERE id = %s LIMIT 1", (id,))
            pelicula = cursor.fetchone()
            if pelicula is not None:
                peliculajson = convertir_pelicula_a_json(pelicula)
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al consultar una pelicula")
        code=500
    return peliculajson,code


def eliminar_pelicula(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM peliculas WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al eliminar una pelicula")
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_pelicula(id, nombre, descripcion, precio, foto,ingredientes):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE peliculas SET nombre = %s, descripcion = %s, precio = %s, foto=%s, ingredientes=%s WHERE id = %s",
                       (nombre, descripcion, precio, foto,ingredientes,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al actualziar una pelicula")
        ret = {"status": "Failure" }
        code=500
    return ret,code
