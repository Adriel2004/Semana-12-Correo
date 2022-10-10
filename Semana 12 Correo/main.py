#GILMAR ADRIEL GONZALEZ ROMERO SMIS061221
#SOFIA GISSELL HERNANDEZ ASCENCIO SMIS015421

#Estas son las importaciones que ocupamos
from ast import Delete
from email import message
from ensurepip import bootstrap
from pydoc import text
from turtle import clear
from Source import email
from dotenv import load_dotenv
from os import environ
from tkinter import Button, Entry, Label  , Tk, dialog


#De las recomendadas en clase para cargar
load_dotenv()



mensaje_html="""

<!DOCYPE html>
<html>
<body>
<h1>LE SALUDAMOS DESDE PYTHON {}</h1>
<p>{}</p>
</body>
</html>
"""

#CONEXION CON LA CUENTA GOOGLE PARA ENVIAR CORREO
def enviar():
   variable=destinatario.get()
   variabl2=escribir2.get()
   variable3=escribir3.get()
   Correo = email.Email()
   Correo.mandar_email([variable],"PYTHON", message_format=mensaje_html.format(variabl2,variable3), format="html")

"""
#Mensaje al enviar -mostrar un mensaje mediante messagedialog-
boton1=Button 
email.message.showinfo('El mensaje se envio correctamente')
boton1.show()

"""
#-Me dio error al ejecutarlo y no supe como solucionarlo-

#CREAR DISEÑO DE VENTANA
ventana = Tk()
ventana.geometry("1000x600")
ventana.title("SEND EMAIL")
ventana.configure(bg="brown")


#ESTABLECER MEDIDAS Y DISEÑO DE CUADROS DE TEXTO
label1=Label(ventana, text="DESTINATARIO (CORREO):"  ,bg="lightblue")
destinatario=Entry(ventana )
nombre=Label(ventana, text="Nombre:"  ,bg="lightblue")
escribir2=Entry(ventana)
escribir3=Entry(ventana)
mensaje=Label(ventana, text="Redactar mensaje:",bg="lightblue")
boton1=Button(ventana, text="Enviar",  bg="lightblue", command=enviar )

label1.place(x=40,y=40)
destinatario.place(x=200, y=40, width=200, height=20)
nombre.place(x=40,y=70)
escribir2.place(x=200, y=70 , width=200, height=20)
mensaje.place(x=40 , y=100)
escribir3.place(x=40, y=140 , width=400, height=100)
boton1.place(x=400, y=240)
ventana.mainloop()