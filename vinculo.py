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

# boton
login.btn_ingreso.clicked.connect(entrada_login)

# ejecutable
login.show()
app.exec()
