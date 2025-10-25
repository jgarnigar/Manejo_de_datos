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

    - Los datos guardados en agregar con la clase **VentanaAgregar** guardará los datos en **datos/archivos.txt** 

- ### 🔹 Buscar

    - Buscamos los datos utilizando la clase **VentanaBuscar** la cual buscará línea por línea un **ID** en **datos/archivos.txt**. Cuando encuentra el ID, muestra la línea completa en pantalla con una **layout.form**. Si el ID no se encuentra mostrará en pantalla una alerta.

- ### 🔹 Elminiar

    - Mostramos una advertencia si el usuario sí desea eliminar los datos.

    - Para eliminar un dato usamos la clase **VentanaEliminar** la cual pedirá un **ID**. Buscamos línea por línea en **datos/archivos.txt** el ID brindado y copia cada línea y la pegamos en **datos/copia.txt**, y si encontramos el **ID**, nos saltamos esa línea, es decir; esa línea no se copia en **datos/copia.txt**. Por último usamos la librería **shutil** para copiar los nuevos datos de **datos/copia.txt** y pasarlos sobreescribiendo el archivo **datos/archivos.txt**. 

    - Si el **ID** nunca fue encontrado, aún copia y pegamos los datos para evitar tener que hacerlo dos veces. Si el **ID** nunca es encontrado, mostramos una alerta de que el ID no fue encontrado.

- ### 🔹 Modificar

    - Mostramos una advertencia si el usuario sí desea modificar los datos.

    - Para modificar datos utilizamos la clase **VentanaModificar** la cual pedirá el **ID, Nombre, Cantidad y Precio**.

    - Buscamos en el archivo **datos/archivos.txt** el **ID** brindado y sobreescribimos el archivo **datos/copia.txt**. Cuando el programa encuentre la línea con el **ID** modificaremos los valores de esa línea por los valores ingresados únicamente de aquellos parámetros ingresados, es decir; si nombre no fue ingresado, no modificaremos el nombre original del proyecto.

    - Si el **ID** no es encontrado, mostramos una advertencia que el ID no fue encontrado. Como el archivo **datos/copia.txt** fue modificado, usamos la librería **shutil** para copiar esos datos a **datos/archivos.txt**.

- ### 🔹 Mostrar

    - Para mostrar todos los datos en **datos/archivos.txt** utilizamos la clase **VentanaMostrar** la cual pedirá un **ID**. Buscamos el **ID** en **datos/archivos.txt** y si el ID es encontrado, mostramos los datos en pantalla con un **layout.form**.

    - Si el **ID** no es encontrado, nostramos en pantalla una advertencia de que el **ID** no fue encontrado.

## ▶️ Ejecución

Para ejecutar el programa abra una terminal desde la carpeta **PROYECTO MANEJO DE DATOS** y ejecute la siguiente línea de código:

        python main.py


## 👨‍💻 Autor

Desarollado por ***Junior Eduardo Garniga Rojas***

