from flask import request, session, make_response
import json
from __main__ import app
import python.controlador_peliculas as controlador_peliculas
from funciones_auxiliares import Encoder, sanitize_input, prepare_response_extra_headers,validar_session_admin,validar_session_normal

@app.route("/chuches",methods=["GET"])
def chuches():
    if (validar_session_normal()):
        respuesta,code= controlador_peliculas.obtener_chuches()
    else:
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/chuches/<id>",methods=["GET"])
def chuche_por_id(id):
    id = sanitize_input(id)
    if isinstance(id, str) and len(id)<64:
        if (validar_session_normal()):
            respuesta,code = controlador_peliculas.obtener_chuche_por_id(id)
        else:
            respuesta={"status":"Forbidden"}
            code=403
    else:
        respuesta={"status":"Bad parameters"}
        code=401
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/chuches",methods=["POST"])
def guardar_chuche():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        chuche_json = request.json
        if "nombre" in chuche_json and "descripcion" in chuche_json and "foto" in chuche_json and "ingredientes" in chuche_json:
            nombre = sanitize_input(chuche_json["nombre"])
            descripcion = sanitize_input(chuche_json["descripcion"])
            precio = chuche_json["precio"]
            foto = sanitize_input(chuche_json["foto"])
            ingredientes = sanitize_input(chuche_json["ingredientes"])
            if isinstance(nombre, str) and isinstance(descripcion, str) and isinstance(foto, str) and isinstance(ingredientes, str) and len(nombre)<128 and len(descripcion)<512 and len(foto)<128 and len(ingredientes)<512:
                if (validar_session_admin()):
                    precio = float(precio)
                    respuesta,code=controlador_peliculas.insertar_chuche(nombre, descripcion,precio,foto,ingredientes)
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

@app.route("/chuches/<int:id>", methods=["DELETE"])
def eliminar_chuche(id):
    if (validar_session_admin()):
        respuesta,code=controlador_peliculas.eliminar_chuche(id)
    else: 
        respuesta={"status":"Forbidden"}
        code=403
    response= make_response(json.dumps(respuesta, cls=Encoder), code)
    return response

@app.route("/chuches", methods=["PUT"])
def actualizar_chuche():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        chuche_json = request.json
        if "id" in chuche_json and "nombre" in chuche_json and "descripcion" in chuche_json and "foto" in chuche_json and "ingredientes" in chuche_json:
            id = request.json["id"]
            nombre = sanitize_input(chuche_json["nombre"])
            descripcion = sanitize_input(chuche_json["descripcion"])
            precio = chuche_json["precio"]
            foto = sanitize_input(chuche_json["foto"])
            ingredientes = sanitize_input(chuche_json["ingredientes"])
            if id.isnumeric() and isinstance(nombre, str) and isinstance(descripcion, str) and precio.isnumeric() and isinstance(foto, str) and isinstance(ingredientes, str) and len(id)<8 and len(nombre)<128 and len(descripcion)<512 and len(foto)<128 and len(ingredientes)<512:
                id=int(id)
                precio=float(precio)
                if (validar_session_normal()):
                    respuesta,code=controlador_peliculas.actualizar_chuche(id,nombre,descripcion,precio,foto,ingredientes)
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
