# Encriptacion-Linux
Código en Python para encriptar archivos en Linux
## Módulos 
Los módulos utilizados fueron "cryptography.fernet" y "os".
cryptography.fernet asegura que el mensaje o archivo no pueda ser manipulado o leido sin una llave previamente generada.

Para instalar el modulo se tiene que poner dentro de terminal <br />

    pip install cryptography
El módulo os nos permite usar funciones establecidas en el Sistema Operativo, por ejemplo la ruta en la que se esta posicionado, nombre del ususario sesionado, e incluso la lista de archivos de un directorio en especifico. Este módulo viene preinstalado en Linux.

## Código de Encriptación

Contiene el codigo ejecutable que se necesita para encriptar los archivos de un directorio en especifico, en este mismo codigo se genera la clave que se usara para encriptar, así como una función recursiva para entrar en cada uno de los subdirectorios del directorio principal para encriptarlos.

## Código de Desencriptación

Contiene el código complementario al de encriptación el cual se usa para desencriptar lo antes encriptado, sigue un proceso similar al codigo de encriptación sin embargo este no contiene la función de:

    def generar_clave():
Debido a que no necesita generar una nueva clave, debido a que este necesita tomar la clave correcta para desencriptar los archivos, por lo que si sobreescribe la clave se vuelve imposible desencriptar los datos.

## Definir Codigo al Arranque del la Computadora
Para definir que el codigo de encriptación se ejecute en el inicio de la computadora se tiene que poner en terminal:

    crontab -e
Que nos permite crear o editar un archivo contrab el cual se usa para programar tareas para el sistema. Dentro de este archivo se pondra el siguente comando:

    @reboot python3 "Ruta donde se aloja el programa de encriptación"
Ejemplo:
    
    @reboot python3 /home/sebastian/Proyecto/Encriptacion.py
Con esto le indicamos que el comando se ejecute durante el inicio de la computadora

