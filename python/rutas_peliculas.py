from flask import request, session, make_response
import json
from __main__ import app
import python.controlador_peliculas as controlador_peliculas
from funciones_auxiliares import Encoder, sanitize_input, prepare_response_extra_headers,validar_session_admin,validar_session_normal

@app.route("/peliculas",methods=["GET"])
def peliculas():
    if (validar_session_normal()):
        respuesta,code= controlador_peliculas.obtener_peliculas()
    else:
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/peliculas/<id>",methods=["GET"])
def pelicula_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            respuesta,code = controlador_peliculas.obtener_pelicula_por_id(id)
        else:
            respuesta={"status":"Forbidden"}
            code=403
    else:
        respuesta={"status":"Bad parameters"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/peliculas",methods=["POST"])
def guardar_pelicula():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        if "nombre" in pelicula_json and "descripcion" in pelicula_json and "foto" in pelicula_json and "ingredientes" in pelicula_json:
            nombre = sanitize_input(pelicula_json["nombre"])
            descripcion = sanitize_input(pelicula_json["descripcion"])
            precio = pelicula_json["precio"]
            foto = sanitize_input(pelicula_json["foto"])
            ingredientes = sanitize_input(pelicula_json["ingredientes"])
            if isinstance(nombre, str) and isinstance(descripcion, str) and isinstance(foto, str) and isinstance(ingredientes, str) and len(nombre)<128 and len(descripcion)<512 and len(foto)<128 and len(ingredientes)<512:
                if (validar_session_admin()):
                    precio = float(precio)
                    respuesta,code=controlador_peliculas.insertar_pelicula(nombre, descripcion,precio,foto,ingredientes)
                else: 
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder))  
    return response

@app.route("/peliculas/<int:id>", methods=["DELETE"])
def eliminar_pelicula(id):
    if (validar_session_admin()):
        respuesta,code=controlador_peliculas.eliminar_pelicula(id)
    else: 
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/peliculas", methods=["PUT"])
def actualizar_pelicula():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        if "id" in pelicula_json and "nombre" in pelicula_json and "descripcion" in pelicula_json and "foto" in pelicula_json and "ingredientes" in pelicula_json:
            id = request.json["id"]
            nombre = sanitize_input(pelicula_json["nombre"])
            descripcion = sanitize_input(pelicula_json["descripcion"])
            precio = pelicula_json["precio"]
            foto = sanitize_input(pelicula_json["foto"])
            ingredientes = sanitize_input(pelicula_json["ingredientes"])
            if id.isnumeric() and isinstance(nombre, str) and isinstance(descripcion, str) and precio.isnumeric() and isinstance(foto, str) and isinstance(ingredientes, str) and len(id)<8 and len(nombre)<128 and len(descripcion)<512 and len(foto)<128 and len(ingredientes)<512:
                id=int(id)
                precio=float(precio)
                if (validar_session_normal()):
                    respuesta,code=controlador_peliculas.actualizar_pelicula(id,nombre,descripcion,precio,foto,ingredientes)
                else: 
                    respuesta={"status":"Forbidden"}
                    code=403
            else:
                respuesta={"status":"Bad request"}
                code=401
        else:
            respuesta={"status":"Bad request"}
            code=401
    else:
        respuesta={"status":"Bad request"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response
