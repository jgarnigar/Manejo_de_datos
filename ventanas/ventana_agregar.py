from PySide6.QtWidgets import QWidget, QPushButton,  QGridLayout, QLabel, QSizePolicy, QLineEdit, QMessageBox
from PySide6.QtCore import Qt



class VentanaAgregar(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_Widget = stacked_widget
        
        stacked_widget.setWindowTitle("Agregar Datos!")
        stacked_widget.setFixedSize(700, 600)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Crear QLineEdit
        self.agregar_id = self.crear_cajas()
        self.layout.addWidget(self.agregar_id, 1, 1)

        self.agregar_nombre = self.crear_cajas()
        self.layout.addWidget(self.agregar_nombre, 2, 1)

        self.agregar_cantidad = self.crear_cajas()
        self.layout.addWidget(self.agregar_cantidad, 3, 1)

        self.agregar_precio = self.crear_cajas()
        self.layout.addWidget(self.agregar_precio, 4, 1)

        #crear labels

        self.layout.addWidget(self.create_labels("Agregue un ID: "), 1, 0)
        self.layout.addWidget(self.create_labels("Agregue el nombre: "), 2, 0)
        self.layout.addWidget(self.create_labels("Agregue la cantidad: "), 3, 0)
        self.layout.addWidget(self.create_labels("Agregue su precio: "), 4, 0)


        # Crear botón
        self.boton_enviar = QPushButton("Enviar")
        #self.boton_enviar.setMinimumSize(130, 30)
        #self.boton_enviar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.addWidget(self.boton_enviar, 0, 0, 1, 2)
        self.boton_enviar.clicked.connect(self.enviar_datos)

        #boton para limpiar los datos
        self.boton_limpiar = QPushButton("Limpiar")
        self.layout.addWidget(self.boton_limpiar, 5, 0, 1, 2)
        self.boton_limpiar.clicked.connect(lambda: self.limpiar_datos())

        #boton para regresar al menú principal
        self.boton_menu_principal = QPushButton("Regrese al menú principal")
        self.layout.addWidget(self.boton_menu_principal, 6, 1, 1, 1)
        self.boton_menu_principal.clicked.connect(lambda: self.stacked_Widget.setCurrentIndex(0))


        self.aplicar_estilos()


    def create_labels(self, texto):
        label = QLabel(texto)
        label.setMinimumSize(150, 30)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        return label
        

    def crear_cajas(self):
        entrada = QLineEdit()
        entrada.setAlignment(Qt.AlignCenter)
        entrada.setMinimumSize(180, 30)
        entrada.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        return entrada

    def enviar_datos(self):
        id = self.agregar_id.text()
        nombre = self.agregar_nombre.text()
        cantidad = self.agregar_cantidad.text()
        precio = self.agregar_precio.text()
        id_encontrado = False

        if all(comprobar.strip() for comprobar in (id, nombre, cantidad, precio)):

            respuesta = QMessageBox.question(
                self,
                "Guardar datos!",
                "¿Desea guardar los datos?",
                QMessageBox.Yes | QMessageBox.No
            )

            with open("datos/archivos.txt", "r") as f:
                lineas = f.readlines()

                for linea in lineas:
                    valor = linea.strip().split(",")
                    if valor[0] == id:
                        QMessageBox.warning(self,"Error!", "Este ID ya existe, asigne otro por favor!")
                        id_encontrado = True

            if id_encontrado == False:
                with open("datos/archivos.txt", "a") as f:
                    f.write(f"{id}, {nombre}, {cantidad}, {precio} \n")

                if respuesta == QMessageBox.Yes:
                    QMessageBox.information(self, "Datos guardados!", "Los datos se han guardado!")        
                else:
                    QMessageBox.information(self, "Cancelado", "No se han guardado los datos!")

                self.limpiar_datos()

        else: 
            QMessageBox.warning(self, "Advertencia", "No hay datos!")

        

    def limpiar_datos(self):
        self.agregar_id.clear()
        self.agregar_cantidad.clear()
        self.agregar_nombre.clear()
        self.agregar_precio.clear()
                

    def aplicar_estilos(self):
        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
            QPushButton {
                background-color: #30343f;
                color: white;
                font-size: 14px;
                border-radius: 6px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #778da9;    
            }
            QLabel {
                background-color: #373f51;
                width: 130px;
                height: 30px;
                border-radius: 10px;
                color: white;
                font-size: 14px;
                padding: 8px;
            }
            QLineEdit {
                background-color: #373f51;
                width: 130px;
                height: 30px;
                border-radius: 10px;
                color: white;
            }
        """)
