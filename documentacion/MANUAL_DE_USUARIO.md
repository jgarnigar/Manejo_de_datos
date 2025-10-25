# 📊 Manejo de Datos ABC

**Autor:** Junior Eduardo Garniga Rojas  
**Lenguaje:** Python 3.10  
**Biblioteca principal:** PySide6  
**Tipo de proyecto:** Aplicación de escritorio con interfaz gráfica  

📦 [Repositorio en GitHub](https://github.com/jgarnigar/Manejo_de_datos)

## 🧩 Descripción

Un proyecto presentado para el manejo de datos: **Agregar, Buscar, Eliminar, Modificar y Mostrar** . Desarrollada con **PySide6** para una interfaz gráfica.

## Menu Principal

![Menú principal](imagenes\menu_principal.png)

## ⚙️ Requisitos e instalación

### Requisitos

- Python 3.10 o más nuevo
- PySide6

### Instalación

- Para instalar el proyecto por favor clone el repositorio:

- [Proyecto Manejo de Datos](https://github.com/jgarnigar/Manejo_de_datos)

        git clone https://github.com/jgarnigar/Manejo_de_datos.git


### Instalar dependencias:

        pip install -r requirements.txt

### Ejecutar el programa:

        python main.py



## 🗂️ Estructura

La estructura de datos del proyecto es:

📦 proyecto-datos

┣ 📂 datos → archivos de texto para guardar los datos.

┃ ┣ 📄 archivos.txt

┃ ┗ 📄 copia.txt


┣ 📂 documentación → Archivos de documentación del proyecto

┃ ┣ 📄 Proyecto_instrucciones.pdf

┃ ┗ 📄 MANUAL_DE_USUARIO.md

┣ 📂 funciones → Función para diseños.

┃ ┣ 📂 __pycache__

┃ ┗ 📄 diseños.py

┣ 📂 imagenes → Recursos gráficos.

┣ 📂 ventanas → Interfaces PySide6 y Funcionamiento

┃ ┣ 📂 __pycache__

┃ ┣ 📄 menu_principal.py

┃ ┣ 📄 ventana_agregar.py

┃ ┣ 📄 ventana_buscar.py

┃ ┣ 📄 ventana_eliminar.py

┃ ┣ 📄 ventana_modificar.py

┃ ┗ 📄 ventana_mostrar.py

┣ 📄 .gitignore → Archivos y carpetas a ignorar por Git

┣ 📄 main.py → Archivo principal para ejecutar el programa

┣ 📄 README.md → Documentación del proyecto

┣ 📄 requirements.txt → Dependencias necesarias para ejecutar el 
proyecto

┗ 📄 DOCUMENTACION_TECNICA.md → Documentación técnica completa


## Funcionamiento

### 📋 Menu Principal

Interfaz de acceso a las funciones: **Agregar, Buscar, Eliminar, Modificar, Mostrar**

### ➕ Agregar

Esta interfaz guarda los datos ingresados en **datos/archivos.txt**

- *Ejemplo de uso* 

    - Ejecuta "python main.py"
    - Se abre la interfaz menú principal
    - Selecciona "Agregar".    
    - Ingresa los datos: **ID, Nombre, Cantidad, Precio**
    - ![Menú Agregar](imagenes\ventana_agregar.png)    
    - Presiona Enviar.
    - ![Datos Agregados](imagenes\ventana_agregar_datos_agregados.png)    
    - Presiona Regrese al menú principal
    


### 🔍 Buscar

Esta interfaz busca un registro en **datos/archivos.txt** con un ID.

- *Ejepmlo de uso*

    - Ejecuta "python main.py".
    - Se abre la interfaz menú principal.
    - Selecciona "Buscar".
    - Ingresa el ID.
    - ![Buscar ID](imagenes\ventana_buscar_datos.png)
    - Presiona Enviar.
    - ![ID encontrado](imagenes\ventana_buscar_datos_encontrado.png)
    - Presiona Regrese al menú principal

### ❌ Eliminar

Interfaz para eliminar un registro en **datos/archivos.txt** con un ID.

- *Ejepmlo de uso*

    - Ejecuta "python main.py".
    - Se abre la interfaz menú principal.
    - Selecciona "Eliminar".
    - Ingresa el ID.
    - ![ventana eliminar](imagenes\ventana_eliminar.png)
    - Presiona Enviar.
    - ![Dato eliminado](imagenes\ventana_eliminar_eliminado.png)
    - Presiona Regrese al menú principal


### 🧩 Modificar

- *Ejepmlo de uso*

    - Ejecuta "python main.py".
    - Se abre la interfaz menú principal.
    - Selecciona "Modificar".
    - Ingresa el ID.
    - Ingrese qué datos desea modificar
    - Presiona Enviar.
    - ![Datos modificados](imagenes\ventana_modificar_datos.png)
    - Presiona Regrese al menú principal

### 📋 Mostrar

- *Ejepmlo de uso*

    - Ejecuta "python main.py".
    - Se abre la interfaz menú principal.
    - Selecciona "Mostrar".
    - Presiona Enviar.
    - ![Mostrar datos](imagenes\ventana_mostrar_datos.png)
    - Presiona Regrese al menú principal


## 👨‍💻 Autor

Desarrollado por **Junior Eduardo Garniga Rojas**  
📧 Contacto: [ jgarnigar@miumg.edu.gt ] 
🔗 GitHub: [jgarnigar](https://github.com/jgarnigar)