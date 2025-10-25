# 📊 Manejo de Datos ABC
Proyecto manejo de datos | Algoritmos | Junior Eduardo Garniga Rojas

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/jgarnigar/Manejo_de_datos)


---

## 🧩 Descripción
Un proyecto presentado para el manejo de datos: **Agregar, Buscar, Eliminar, Modificar y Mostrar** . Desarrollada con **PySide6** para una interfaz gráfica.

## ⚙️ Requisitos e instalación

### Requisitos

- Python 3.10 o más nuevo
- PySide6

### Instalación

- Para instalar el proyecto por favor clone el repositorio:

- [Proyecto Manejo de Datos](https://github.com/jgarnigar/Manejo_de_datos)

Instalar dependencias:

        pip install -r requirements.txt



## 🗂️ Estructura

La estructura de datos del proyecto es:

📦 proyecto-datos

┣ 📂 datos → archivos de texto para guardar los datos.

┃ ┣ 📄 archivos.txt

┃ ┗ 📄 copia.txt

┣ 📂 funciones → Función para diseños.

┃ ┣ 📂 pycache

┃ ┗ 📄 diseños.py

┣ 📂 imagenes → Recursos gráficos.

┃ ┗ 📄 halloween.png

┣ 📂 ventanas → Interfaces PySide6 y Funcionamiento

┃ ┣ 📂 pycache

┃ ┣ 📄 menu_principal.py

┃ ┣ 📄 ventana_agregar.py

┃ ┣ 📄 ventana_buscar.py

┃ ┣ 📄 ventana_eliminar.py

┃ ┣ 📄 ventana_modificar.py

┃ ┗ 📄 ventana_mostrar.py

┣ 📄 main.py → Archivo principal para ejecutar el programa.

┣ 📄 README.md → Documentación del proyecto

┗ 📄 requirements.txt → Dependencias necesarias para ejecutar el proyecto


## 💾 Datos guardados

Los datos se han guardado en la carpeta datos y se tienen los datos:
1. 📄 archivos.txt       → Los datos guardados
2. 📄 copia.txt          → Copia para modificar y eliminar


## ⚙️Procesamiento de datos

### 🏠 Menu Principal

El menú principal nos motrará los botones: **Agrear Buscar Elminar Modificar Mostrar**

- ### 🔹 Agregar

    - Pedimos **ID, Nombre, Cantidad, Precio** y los guardamos en **datos/archivos.txt**

- ### 🔹 Buscar

    - Pedimos un **ID** y lo buscamos en **datos/archivos.txt**. Si el **ID** es encontrado, lo mostramos en pantalla, sino mostramos una alerta.

- ### 🔹 Elminiar

    - Pedimos un **ID** para el producto, lo buscamos en **datos/archivos.txt** y lo eliminamos.

- ### 🔹 Modificar

    - Pedimos un **ID(mandatorio), Nombre, Cantidad, Precio** para el producto, lo buscamos en **datos/archivos.txt** y modificamos la línea por los datos ingresados.

- ### 🔹 Mostrar

    - Mostramos todos los datos de **datos/archivox.txt** y los mostramos por pantalla.

- ### 📄 Documentación Técnica
    - Consulta la [documentación técnica completa](DOCUMENTACION_TECNICA.md) para ver el funcionamiento interno de cada ventana.


## ▶️ Ejecución

Para ejecutar el programa abra una terminal desde la carpeta **PROYECTO MANEJO DE DATOS** y ejecute la siguiente línea de código:

        python main.py


## 👨‍💻 Autor

Desarollado por ***Junior Eduardo Garniga Rojas***

