from PySide6.QtWidgets import QApplication, QStackedWidget
from ventanas.menu_principal import *
from ventanas.ventana_agregar import *
from ventanas.ventana_buscar import *
from ventanas.ventana_eliminar import *
from ventanas.ventana_modificar import *
from ventanas.ventana_mostrar import *

app = QApplication([])
stacked_widget = QStackedWidget()


#Llamamos nuestra clase MenuPrincipal.
menu_principal = MenuPrincipal(stacked_widget)
agregar = VentanaAgregar(stacked_widget)
buscar = VentanaBuscar(stacked_widget)
eliminar = VentanaEliminar(stacked_widget)
modificar = VentanaModificar(stacked_widget)
mostrar = VentanaMostrar(stacked_widget)


#menu_principal tiene un índice 0
#pantalla_agregar tiene un índice 1
#pantalla_buscar tiene un índice 2
#pantalla_eliminar tiene un índice 3
#pantalla_modificar tiene un índice 4
#pantalla_mostrar tiene un índice 5


if __name__ == "__main__":
    stacked_widget.addWidget(menu_principal)
    stacked_widget.addWidget(agregar)
    stacked_widget.addWidget(buscar)
    stacked_widget.addWidget(eliminar)
    stacked_widget.addWidget(modificar)
    stacked_widget.addWidget(mostrar)

    stacked_widget.show()


    app.exec()