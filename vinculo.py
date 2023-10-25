from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QApplication
import conexion

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

# boton
login.btn_ingreso.clicked.connect(entrada_login)
principal.btn_creae.clicked.connect(crear_nuevo)
principal.btn_prender.clicked.connect()

# ejecutable
login.show()
app.exec()
