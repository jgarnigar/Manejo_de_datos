from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QSizePolicy, QFormLayout, QLabel, QWidget
from funciones.diseños import *

class VentanaMostrar(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_Widget = stacked_widget


        stacked_widget.setWindowTitle("Modificar datos!")
        stacked_widget.setFixedSize(700, 600)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        #creamos nuestro botón

        btn = QPushButton("Enviar")
        self.layout.addWidget(btn, 0, 0)
        btn.setMinimumSize(200, 30)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.clicked.connect(lambda: self.mostrar_datos())

        #creamos una etiqueta

        lbl = QLabel("Para mostrar los registros, presione el botón")
        self.layout.addWidget(lbl, 0, 1)
        lbl.setMinimumSize(200, 30)
        lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        #creamos nuestro form
        
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout, 1, 0)

        #botón para regresar
        self.boton_menu_principal = QPushButton("Regrese al menú principal")
        self.layout.addWidget(self.boton_menu_principal, 6, 1, 1, 1)
        self.boton_menu_principal.clicked.connect(lambda: self.stacked_Widget.setCurrentIndex(0))



    def mostrar_datos(self):

        while self.form_layout.count():
            item = self.form_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()        

        with open("datos/archivos.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                valor = line.strip().split(",")

                if not line:
                    continue

                if len(valor) < 4:
                    continue

                self.form_layout.addRow("ID: ", QLabel(valor[0]))
                self.form_layout.addRow("Nombre: ", QLabel(valor[1]))
                self.form_layout.addRow("cantidad: ", QLabel(valor[2]))
                self.form_layout.addRow("Precio: ", QLabel(valor[3]))
                self.form_layout.addRow("-------------", QLabel("-----"))
