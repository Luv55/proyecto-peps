from bd import obtener_conexion
from __main__ import app
from funciones_auxiliares import sanitize_input
import sys

def insertar_chuche(nombre, descripcion, precio,foto,ingredientes):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO chuches(nombre, descripcion, precio,foto,ingredientes) VALUES (%s, %s, %s,%s,%s)",
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

def convertir_chuche_a_json(chuche):
    d = {}
    d['id'] = chuche[0]
    d['nombre'] = sanitize_input(chuche[1])
    d['descripcion'] = sanitize_input(chuche[2])
    d['precio'] = chuche[3]
    d['foto'] = sanitize_input(chuche[4])
    d['ingredientes']=sanitize_input(chuche[5])
    return d

def obtener_chuches():
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto,ingredientes FROM chuches")
            chuches = cursor.fetchall()
            chuchesjson=[]
            if chuches:
                for chuche in chuches:
                    chuchesjson.append(convertir_chuche_a_json(chuche))
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al obtener las chuches")
        chuchesjson=[]
        code=500
    return chuchesjson,code

def obtener_chuche_por_id(id):
    chuchejson = {}
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, descripcion, precio,foto,ingredientes FROM chuches WHERE id = %s LIMIT 1", (id,))
            chuche = cursor.fetchone()
            if chuche is not None:
                chuchejson = convertir_chuche_a_json(chuche)
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al consultar una chuche")
        code=500
    return chuchejson,code


def eliminar_chuche(id):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM chuches WHERE id = %s", (id,))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al eliminar una chuche")
        ret = {"status": "Failure" }
        code=500
    return ret,code

def actualizar_chuche(id, nombre, descripcion, precio, foto,ingredientes):
    try:
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE chuches SET nombre = %s, descripcion = %s, precio = %s, foto=%s, ingredientes=%s WHERE id = %s",
                       (nombre, descripcion, precio, foto,ingredientes,id))
            if cursor.rowcount == 1:
                ret={"status": "OK" }
            else:
                ret={"status": "Failure" }
        conexion.commit()
        conexion.close()
        code=200
    except:
        app.logger.info("Excepcion al actualziar una chuche")
        ret = {"status": "Failure" }
        code=500
    return ret,code
