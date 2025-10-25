from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QSizePolicy, QLineEdit, QMessageBox, QFormLayout, QLabel, QWidget
from PySide6.QtCore import Qt
from funciones.diseños import *

class VentanaBuscar(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_Widget = stacked_widget

        stacked_widget.setWindowTitle("Buscar Datos!")
        stacked_widget.setFixedSize(700, 600)
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        #creamos el botón
        self.btn_buscar = QPushButton("Ingrese el ID: ")
        self.layout.addWidget(self.btn_buscar, 0, 0)

        self.btn_buscar.setMinimumSize(130, 30)
        self.btn_buscar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.btn_buscar.clicked.connect(lambda: self.mostrar_datos())

        #creamos el QLineEdit

        self.obtener_id = QLineEdit()
        self.obtener_id.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.obtener_id, 0, 1)

        self.obtener_id.setMinimumSize(200, 30)
        self.obtener_id.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)


        #creamos el layout para el form que tendrá los datos
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout, 3, 1)        
        
        #botón para regresar
        self.boton_menu_principal = QPushButton("Regrese al menú principal")
        self.layout.addWidget(self.boton_menu_principal, 6, 1, 1, 1)
        self.boton_menu_principal.clicked.connect(lambda: self.stacked_Widget.setCurrentIndex(0))

        aplicar_estilos(stacked_widget)



    def mostrar_datos(self):

        while self.form_layout.count():
            item = self.form_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        id = self.obtener_id.text()
        encontrado = False

        if id.strip():

            with open("datos/archivos.txt", "r") as f:
                #convertimos f en un lista para usar in.
                lines = f.readlines()

                for line in lines:
                    valor = line.strip().split(",")

                    if valor[0] == id:
                        encontrado = True
                        print("Encontrado", valor[0])
                        self.form_layout.addRow("ID: ", QLabel(valor[0]))
                        self.form_layout.addRow("Nombre: ", QLabel(valor[1]))
                        self.form_layout.addRow("Cantidad: ", QLabel(valor[2]))
                        self.form_layout.addRow("Precio: ", QLabel(valor[3]))
                        break

                if encontrado == False:
                    QMessageBox.warning(self, "No se encontró", "El ID buscado no se encontró!")
        
        else:
            QMessageBox.warning(self,"No hay valor", "Ingrese un ID por favor!")

                

