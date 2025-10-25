from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy, QLineEdit, QMessageBox,QWidget
from PySide6.QtCore import Qt
from funciones.diseños import *
import shutil

class VentanaEliminar(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_Widget = stacked_widget


        stacked_widget.setWindowTitle("Eliminar Datos!")
        stacked_widget.setFixedSize(700, 600)
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)


        #creamos nuestro botón
        self.eliminar = QPushButton("Ingrese el ID: ")
        self.layout.addWidget(self.eliminar, 0, 0)
        self.eliminar.setMinimumSize(130, 30)
        self.eliminar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.eliminar.clicked.connect(lambda: self.borrar_datos())

        #creamos nuestro label
        self.obtener_id = QLineEdit()
        self.layout.addWidget(self.obtener_id, 0, 1)
        self.obtener_id.setMinimumSize(200, 30)
        self.obtener_id.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.obtener_id.setAlignment(Qt.AlignCenter)


        #boton para regresar al menú principal
        self.boton_menu_principal = QPushButton("Regrese al menú principal")
        self.layout.addWidget(self.boton_menu_principal, 6, 1, 1, 1)
        self.boton_menu_principal.clicked.connect(lambda: self.stacked_Widget.setCurrentIndex(0))


        aplicar_estilos(stacked_widget)

    def borrar_datos(self):
        id = self.obtener_id.text()
        encontrado = False

        if id.strip():

            respuesta = QMessageBox.question(
                self,
                "Eliminar datos!",
                "¿Está seguro de eliminar los datos?",
                QMessageBox.Yes | QMessageBox.No
            )

            if respuesta == QMessageBox.Yes:
                with open("datos/copia.txt", "w") as f:


                    with open("datos/archivos.txt", "r") as r:
                        lineas = r.readlines()

                        for linea in lineas:
                            valor = linea.strip().split(",")
                            if valor[0] != id:
                                f.write(linea)
                                print("Hola", valor, linea)
                            else:
                                encontrado = True

                shutil.copyfile("datos/copia.txt", "datos/archivos.txt")
                if encontrado == True:
                    QMessageBox.information(self, "Datos Eliminados!", "Los datos se eliminarons exitosamente!")                        
                else:
                    QMessageBox.information(self, "No se encontró!", "El ID no se encontró!")

            else:
                QMessageBox.information(self, "cancelado", "No se eliminaron los datos!")

            self.obtener_id.clear()
        
        else:
            QMessageBox.information(self,"No hay valor", "Ingrese un ID por favor!")