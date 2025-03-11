from __future__ import print_function
from __main__ import app
from flask import request,session
from pymysql import Error
from bd import obtener_conexion
import json
import sys
import traceback
import bleach
from funciones_auxiliares import sanitize_input
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

class LoginForm(FlaskForm): 
    username = StringField("Usuario", validators=[ DataRequired(message="El usuario es obligatorio"), Length(min=4, max=20, message="El usuario debe tener entre 4 y 20 caracteres"), Regexp(r"^[a-zA-Z0-9_]+$", message="El usuario solo puede contener letras, números y guiones bajos"), ])
    password = PasswordField("Contraseña", validators=[ DataRequired(message="La contraseña es obligatoria"), Length(min=6, message="La contraseña debe tener al menos 6 caracteres") ])


@app.route("/login",methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        username = sanitize_input(pelicula_json['username'])
        password = sanitize_input(pelicula_json['password'])
        username = 
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                 cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s and clave= %s",(username,password))
                 #cursor.execute("SELECT perfil FROM usuarios WHERE usuario = '" + username +"' and clave= '" + password + "'")
                 usuario = cursor.fetchone()
            conexion.close()
            if usuario is None:
                ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
            else:
                ret = {"status": "OK" }
                #session["usuario"]=username
                #session["perfil"]=usuario[0]
            code=200
        except Error as err:
            print("Excepcion al validar al usuario ")
            #traceback.print_exc()   
            ret={"status":"ERROR"}
            code=500
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code

@app.route("/registro",methods=['POST'])
def registro():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        pelicula_json = request.json
        username = sanitize_input(pelicula_json['username'])
        password = sanitize_input(pelicula_json['password'])
        perfil = sanitize_input(pelicula_json['profile'])
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                 cursor.execute("SELECT perfil FROM usuarios WHERE usuario = %s and clave= %s",(username,password))
                 #cursor.execute("SELECT perfil FROM usuarios WHERE usuario = '" + username +"' and clave= '" + password + "'")
                 usuario = cursor.fetchone()
                 if usuario is None:
                     print("INSERT INTO usuarios(usuario,clave,perfil) VALUES('"+ username +"','"+  password+"','"+ perfil+"')") 
                     print("INSERT INTO usuarios(usuario, clave, perfil) VALUES (%s, %s, %s)", (username, password, perfil))
                     cursor.execute("INSERT INTO usuarios(usuario,clave,perfil) VALUES('"+ username +"','"+  password+"','"+ perfil+"')")
                     if cursor.rowcount == 1:
                         conexion.commit()
                         ret={"status": "OK" }
                         code=200
                     else:
                         ret={"status": "ERROR" }
                         code=500
                 else:
                   ret = {"status": "ERROR","mensaje":"Usuario/clave erroneo" }
                   code=200
            conexion.close()
        except:
            print("Excepcion al registrar al usuario")   
            ret={"status":"ERROR"}
            code=500
    else:
        ret={"status":"Bad request"}
        code=401
    return json.dumps(ret), code


@app.route("/logout",methods=['GET'])
def logout():
    session.clear()
    return json.dumps({"status":"OK"}),200
