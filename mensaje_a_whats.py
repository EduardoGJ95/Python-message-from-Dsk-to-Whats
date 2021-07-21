#librerías a importar
import pywhatkit as wt

try:
	wt.sendwhatmsg("+525532358798","Hola, te mandé mensaje desde el escritorio con Python",21,25)
		#("numero_a_enviar","mensaje","hora","minuto")
	print("Mensaje enviado")
except:
	print("Error al mandar el mensaje")
