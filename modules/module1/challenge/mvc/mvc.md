# **Gestión de Tareas - Aplicación de Consola en Python (MVC)**

## Descripción

**Gestión de Tareas** es una aplicación de consola en Python que permite gestionar una lista de tareas utilizando el patrón de diseño **Modelo-Vista-Controlador (MVC)**. La aplicación permite al usuario agregar nuevas tareas, listar las tareas existentes y marcar tareas como completadas. Está estructurada para mantener el código organizado y modular utilizando el patrón MVC, facilitando su escalabilidad y mantenimiento.

## Estructura del Proyecto

La aplicación está organizada en tres componentes principales siguiendo el patrón MVC:


```bash Copiar código

tareas_app/
│
├── controller.py   # Lógica del controlador
├── models.py       # Modelo y la lógica de negocio
├── view.py         # Interfaz de usuario (salidas e interacciones)
└── main.py         # Punto de entrada de la aplicación

```

### Descripción de los Archivos

- **`models.py`**: Contiene la clase `Tarea` que representa una tarea individual, así como la clase `GestorTareas`, que maneja las operaciones sobre las tareas (agregar, listar y completar tareas).
- **`view.py`**: Gestiona la interacción con el usuario a través de la consola. Muestra los menús, recoge entradas del usuario y muestra los resultados.
- **`controller.py`**: Actúa como intermediario entre el Modelo y la Vista. Recibe las acciones del usuario, realiza las operaciones necesarias sobre el Modelo y actualiza la Vista.
- **`main.py`**: Es el punto de entrada de la aplicación. Aquí se ejecuta el ciclo principal que inicia la aplicación.

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalado **Python 3.x** en tu máquina.

Puedes verificar si tienes Python instalado ejecutando el siguiente comando en tu terminal:

```bash
python --version
```
Si no tienes Python instalado, puedes descargarlo e instalarlo desde python.org.

## Instalación
**Clonar el repositorio:**

Si no tienes el proyecto aún, clónalo en tu máquina local utilizando el siguiente comando:

bash
Copiar código
git clone https://github.com/tu_usuario/gestion-tareas.git
Acceder al directorio del proyecto:

Una vez que hayas clonado el repositorio, navega al directorio del proyecto:

bash
Copiar código
cd gestion-tareas
Instalar dependencias (si es necesario):

En este proyecto no hay dependencias externas, ya que se utiliza solo la biblioteca estándar de Python. Sin embargo, si en el futuro decides agregar alguna, puedes usar pip para instalarlas.

Ejecución
Ejecutar la aplicación:

Para ejecutar la aplicación, simplemente corre el archivo main.py:

bash
Copiar código
python main.py
Interacción con la aplicación:

Al ejecutar la aplicación, el programa mostrará un menú en la consola con las siguientes opciones:

markdown
Copiar código
--- Menú de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Completar tarea
4. Salir
Agregar tarea: Te pedirá que ingreses la descripción de la tarea.
Listar tareas: Muestra todas las tareas actuales, indicando si están completadas o no.
Completar tarea: Te pedirá que ingreses el nombre de la tarea a completar.
Salir: Termina la aplicación.
Funcionalidades
Agregar tareas: Permite agregar tareas con una descripción. Las tareas son inicialmente marcadas como "Pendientes".
Listar tareas: Muestra todas las tareas con su descripción y estado (Pendiente/Completada).
Marcar tareas como completadas: Permite marcar una tarea como "Completada" introduciendo su nombre.
Ejemplo de Uso
Agregar una tarea:

El usuario selecciona la opción "1" para agregar una tarea.
La aplicación solicita la descripción de la tarea y la agrega a la lista.
Listar tareas:

El usuario selecciona la opción "2" para listar las tareas.
La aplicación muestra todas las tareas, indicando si están completadas o no.
Completar una tarea:

El usuario selecciona la opción "3" para completar una tarea.
La aplicación solicita la descripción de la tarea a completar y la marca como "Completada".
Salir de la aplicación:

El usuario selecciona la opción "4" para salir de la aplicación.
Ejemplo de Interacción
bash
Copiar código
--- Menú de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Completar tarea
4. Salir
Seleccione una opción: 1
Ingrese la descripción de la tarea: Comprar pan
Tarea agregada con éxito.

--- Menú de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Completar tarea
4. Salir
Seleccione una opción: 2
Comprar pan - Pendiente

--- Menú de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Completar tarea
4. Salir
Seleccione una opción: 3
Ingrese el nombre de la tarea para marcarla como completada: Comprar pan
Tarea completada.

--- Menú de Tareas ---
1. Agregar tarea
2. Listar tareas
3. Completar tarea
4. Salir
Seleccione una opción: 4
Saliendo de la aplicación...
Contribución
Si deseas contribuir al proyecto, ¡estás más que bienvenido! Para hacerlo, sigue estos pasos:

Fork el repositorio.
Crea una nueva rama para tu contribución:
bash
Copiar código
git checkout -b nombre-de-la-rama
Realiza tus cambios y haz commit de ellos:
bash
Copiar código
git commit -am 'Descripción de los cambios'
Push a tu rama:
bash
Copiar código
git push origin nombre-de-la-rama
Crea un Pull Request describiendo tus cambios.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Contacto
Si tienes alguna pregunta, sugerencia o problema con la aplicación, no dudes en abrir un Issue o enviarme un correo a tu_email@dominio.com.