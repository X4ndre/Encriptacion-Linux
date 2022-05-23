from cryptography.fernet import Fernet
import os

def cargar_clave():
	return open("clv.key","rb").read()

def decrypt(archivo,clave):
	f = Fernet(clave)
	with open(archivo, "rb") as file:
		data = file.read()
	decrypted_data = f.decrypt(data)
	with open(archivo, "wb") as file:
		file.write(decrypted_data)

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
			decrypt(ruta_a,clave)

usuario = os.getlogin()

ruta = "/home/"

directorio = "/Descargas"

ruta = ruta + usuario + directorio

contenido = os.listdir(ruta)

clave = cargar_clave()

recorrido(contenido,ruta,clave)