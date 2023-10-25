from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication
import conexion
import pymongo
import colorama
import random
import time

#iniciar la aplicacion
app = QtWidgets.QApplication([])

#cargar archivo .ui
login = uic.loadUi("./interfaz-grafica/login.ui")
principal= uic.loadUi("./interfaz-grafica/principal.ui")

#funcion para leer los datos ingresados
def entrada_login():
    correo= login.line_correo.text()
    contrasena= login.line_contrasena.text()
    usuario = conexion.usuarios.find_one({"correo": correo})
    
    if correo == usuario["correo"] and contrasena == usuario["contraseña"]:
        entrada_principal()
    else:
        login.label_error.setText("correo o contraseña error")

def entrada_principal():
    
    login.hide()
    principal.show()
    app.exec()

#funcion para crear nuevo sensor
def crear_nuevo():
    id = principal.line_id.text()
    nombre = principal.line_nombre.text()
    min = principal.line_min.text()
    max = principal.line_max.text()
    conexion.sensores.insert_one({"id":id,"nombre":nombre,"minimo":min,"maximo":max})

#funcion actividad sensor
def activo():
    lista_sensores = list(conexion.sensores.find())

    med_fue_rango = 0  # mediciones fuera de rango

    while med_fue_rango < 3:
        sensor = random.choice(lista_sensores)
        minimo = float(sensor["minimo"])
        maximo = float(sensor["maximo"])
        valor = random.uniform(minimo, maximo)
    
        if minimo <= valor <= maximo:
            principal.label_sensor.setText(colorama.Fore.GREEN + f"{sensor['nombre']}: {valor}" + colorama.Style.RESET_ALL)
        else:
            principal.label_sensor.setText(colorama.Fore.RED + f"{sensor['nombre']}: {valor}" + colorama.Style.RESET_ALL)
            med_fue_rango += 1
        time.sleep(1)


# boton
login.btn_ingreso.clicked.connect(entrada_login)
principal.btn_crear.clicked.connect(crear_nuevo)
principal.btn_prender.clicked.connect(activo)

# ejecutable
login.show()
app.exec()
