from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QSizePolicy, QLineEdit, QMessageBox, QFormLayout, QLabel, QWidget
from PySide6.QtCore import Qt
from funciones.diseños import *
import shutil

class VentanaModificar(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_Widget = stacked_widget


        stacked_widget.setWindowTitle("Modificar datos!")
        stacked_widget.setFixedSize(700, 600)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        #creamos nuestro botón

        self.btn = QPushButton("Enviar")
        self.layout.addWidget(self.btn, 0, 1)
        self.btn.setMinimumSize(250, 30)

        self.btn.clicked.connect(lambda: self.modificar_datos())


        #creamos nuestra label
        self.ln_id = self.crear_line()
        self.layout.addWidget(self.ln_id, 1 , 3)

        self.ln_nombre = self.crear_line()
        self.layout.addWidget(self.ln_nombre, 2, 3)

        self.ln_cantidad = self.crear_line()
        self.layout.addWidget(self.ln_cantidad, 3, 3)

        self.ln_precio = self.crear_line()
        self.layout.addWidget(self.ln_precio, 4, 3)


        #creamos las etiquetas

        self.layout.addWidget(self.crear_etiqueta("Ingrese el ID: "), 1, 0)
        self.layout.addWidget(self.crear_etiqueta("Ingrese el nombre: "), 2, 0)
        self.layout.addWidget(self.crear_etiqueta("Ingrese la cantidad: "), 3, 0)
        self.layout.addWidget(self.crear_etiqueta("Ingrese el precio: "), 4, 0)

        #mostramos el nuevo registro
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout, 5, 1)    

        #botón para regresar
        self.boton_menu_principal = QPushButton("Regrese al menú principal")
        self.layout.addWidget(self.boton_menu_principal, 6, 1, 1, 1)
        self.boton_menu_principal.clicked.connect(lambda: self.stacked_Widget.setCurrentIndex(0))




    def modificar_datos(self):
        
        id = self.ln_id.text().strip()
        nombre = self.ln_nombre.text().strip()
        cantidad = self.ln_cantidad.text().strip()
        precio = self.ln_precio.text().strip()
        encontrado = False

        resultado = QMessageBox.question(
            self,
            "Confirmación",
            "¿Está seguro de actualizar los datos?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resultado == QMessageBox.Yes:

            while self.form_layout.count():
                item = self.form_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()


            with open("datos/copia.txt", "w") as r:


                with open("datos/archivos.txt", "r") as f:
                    
                    lineas = f.readlines()

                    for linea in lineas:
                        valor = linea.strip().split(",")
                        #comprobamos si el ID existe
                        if valor[0] == id:
                            encontrado = True
                            if nombre:
                                valor[1] = nombre
                            if cantidad:
                                valor[2] = cantidad
                            if precio:
                                valor[3] = precio

                            r.write(",".join(valor) + "\n")

                            #mostramos el nuevo registro

                            self.form_layout.addRow("ID: ", QLabel(valor[0]))
                            self.form_layout.addRow("Nombre: ", QLabel(valor[1]))
                            self.form_layout.addRow("Cantidad: ", QLabel(valor[2]))
                            self.form_layout.addRow("Precio: ", QLabel(valor[3]))
                            
                        else:
                            r.write(linea)
            
            shutil.copyfile("datos/copia.txt", "datos/archivos.txt")   

            if encontrado == False:
                QMessageBox.warning(self,"Error", "ID no encontrado!")                

        else:
            QMessageBox.warning(self, "Alerta", "Los datos no fueron actualizados!")

    
    def crear_line(self):
        ln = QLineEdit()
        ln.setMinimumSize(180, 30)
        ln.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)        
        ln.setAlignment(Qt.AlignCenter)

        return ln
    

    def crear_etiqueta(self, nombre):
        lbl = QLabel(nombre)
        lbl.setMinimumSize(150, 30)
        lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        return lbl
