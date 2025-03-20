# Proyecto Segundo Parcial
## Clase: Innovación tecnológica (Gpo 201)

**Creado por:** 
- Andres Rodriguez Cantu ─ A01287002
- Fernando Chavez Nolasco ─ A01284698
- Victor Manuel Sanchez Chavez ─ A01287522
- Roberto Andre Guevara Martinez ─ A01287324

**Fecha:** Marzo 19, 2025

# Descripción General
## Base de datos de una biblioteca.
El proyecto consta de una base de datos echa a partir desde las limitaciones de una consola. El proyecto es simple, pero como se trabaja desde una consola se agiliza mucho el proceso. 

## Lista de comandos
La lista de comandos es breve, tan solo cuenta con 7 comandos, sin embargo, con estos siete comandos, puedes tomar registro de libros, pedir rentado y devolver libros, ademas de buscar si hay algún libro en la libreria.
**Lista de comandos**
```txt
ayuda   ― Muestra la lista de comandos disponibles.
buscar  ― Busca un libro en la base de datos.
cls     ― Limpia la consola.
db      ― Imprime a la consola los primeros 10 elementos de la base de datos.
operacion       ― Reserva/Devuelve un libro
registro        ― Muestra el registro de rentas.
salir   ― Cierra el programa.
```

## El color en el texto
Basandonos en la librería **colored**, hicimos nuestra propia librería en donde pudimos integrar todos los colores que ocupamos para hacer posible el color desde la libreria. Sin embargo, para cambiar el color mientras que el usuario escribe en la consola si fue un reto. De hecho, el metodo que usamos para hacerlo hace que este programa fuera incompatible con usuarios de MAC (al usar la libreria `msvcrt` que comunica desde la interfaz de la consola al usuario). Para garantizar que funcionara, tuvimos que romper la funcionalidad de la consola y repararla a nuestro modo.

## Estructura de código
El archivo principal `main.py` está casí vacio, esto está hecho a proposito ya que, gracias a este metodo, pudimos hacer referencia de manera directa a los comandos que estan dentro de `lib/commands.py`. En pocas palabras, con este código, pudimos hacer que si el usuario escribe el nombre de la función en la terminal, este ejecutaría el comando SIEMPRE Y CUANDO este esté en la clase `cmd` de la libreria de comandos.
```py
while True:
    try:
        comando = input_color.start_input().strip()
        if not comando:
            continue
        parts = comando.split()
        comando_name = parts[0]
        args = parts[1:]
        getattr(cmd, comando_name)(main, *args)
```

# Instalación
## Prerequisitos
- Tener python en versión 3.11 o superior.
- Tener pip instalado
- Tener windows 10/11
- Tener powershell o consola moderna. (La que esta integrada en VSCode tambien cuenta)

## Pasos de instalación
### Con curl
1.- Abre command prompt o powershell 

2.- Escribe el siguiente comando en tu consola
```sh
curl -L "https://drive.google.com/uc?export=download&id=18RIVLym9fFeWjOosVT753X2ksl0zuBMv" -o "%USERPROFILE%\Downloads\main.zip"
```

3.- Extrae el archivo .zip

4.- Entra al archivo usando `cd "directorio\assignment-14"`

5.- Instala los requerimientos corriendo el siguiente comando en la terminal
```sh
pip install -r requirements.txt
```

6.- Corre el archivo de python con el siguiente comando
```sh
python main.py
```
### Con github
1.- Abre la siguiente liga

```sh
https://github.com/TEC-Andres/Programacion-Prepa/tree/master/Segundo%20Parcial/assignment-14
```

2.- Descarga el archivo en formato .zip

3.- Extraelo en explorador de archivos.

4.- Abre el folder en VSCode

5.- Instala los requerimientos corriendo el siguiente comando en la terminal
```sh
pip install -r requirements.txt
```

6.- Corre el archivo de python con el siguiente comando
```sh
python main.py
```