from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap

class MenuPrincipal(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        #inicilizamos el incide
        self.stacked_Widget = stacked_widget
        #Creamos nuestra ventana
        stacked_widget.setWindowTitle("Menu Principal")
        stacked_widget.setFixedSize(700, 600)
        
        titulo = QLabel("Eliga una opción")
        titulo.hide()

        #creamos el layout para los botones
        self.layout = QGridLayout()
        self.setLayout(self.layout)


        #creamos los botones
        btn_agregar = self.crear_botones("Agregar", 1)
        btn_buscar = self.crear_botones("Buscar", 2)
        btn_eliminar = self.crear_botones("Eliminar", 3)
        btn_modificar = self.crear_botones("Modificar", 4)
        btn_mostrar = self.crear_botones("Mostrar datos", 5)

        #Posicionamos los botones
        self.layout.addWidget(titulo, 0, 2, 1, 2)
        self.layout.addWidget(btn_agregar, 0, 3, 1, 2)
        self.layout.addWidget(btn_buscar, 1, 3, 1, 1)
        self.layout.addWidget(btn_eliminar, 2, 3, 1, 3)
        self.layout.addWidget(btn_modificar, 3, 3, 1, 3)
        self.layout.addWidget(btn_mostrar, 4, 3, 1, 3)

        #agregamos una imagen

        imagen = QLabel()
        pixmap = QPixmap("imagenes/halloween.png")
        imagen.setPixmap(pixmap)
        imagen.setScaledContents(True)
        imagen.setFixedSize(200, 250)
        self.layout.addWidget(imagen, 1, 5, 4, 3)

        stacked_widget.setStyleSheet("background-color: #d8dbe2")
        self.aplicar_estilos()

    def crear_botones(self, texto, indice):
        boton = QPushButton(texto)
        boton.clicked.connect(lambda: self.stacked_Widget.setCurrentIndex(indice))
        boton.setMinimumSize(180, 30)
        boton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.addWidget(boton)
        return boton

    def aplicar_estilos(self):
        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
            QPushButton {
                background-color: #373f51;
                color: white;
                font-size: 14px;
                border-radius: 6px;
                padding: 8px;
           }
            
            QPushButton:hover {
                background-color: #778da9;    
            }
            QLabel {
                color: white;
                font-size: 20px;
                border-radius: 6px;
                padding: 8px;
                font-family: Helvetica;
                font-weight: bold;
                background-color: 0d1b2a;
            }
        """)
        