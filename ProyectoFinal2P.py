#PARA NUESTRO PORYECTO OCUAPAMOS IMPORTAR VARIAS LIBRERIAS COMO TKINTER PARA LAS INTERFAZ GRAFICA
#MYSQL.CONNECTOR PARA LA CONEXION A LA BASE DE DATOS DE MYSQL A PYTHON
#Y TAMBIEN LA LIBRERIA SOCKET PARA PODER EXTRAER LA INSTANCIA DE MYSQL Y PUERTO
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import socket
#ESTOS ROOT NOS PARA CREAR EL TAMAñO Y TITULO DE NUESTRAS VENTANAS
root = Tk()
root.geometry("750x450")
root.title("MySQL CRUD Operations")
#NOMBRE DE LA INSTANCIA DE MYSQL
hostname = socket.gethostname()
port = 3306
instance_name = hostname
print("Nombre de la instancia de MySQL: " + instance_name)
#PUERTO DE LA INSTANCIA DE MYSQL
hostname = socket.gethostname()
port = 3306
instance_port = str(port)
print("Nombre de la instancia de MySQL: " + instance_name)
#ESTA FUNCION SALDO NOS SIRVE PARA CONSULTAR EL SALDO QUE TENEMOS EN CADA CUENTA
def Saldo():
    connection = mysql.connect(host ='localhost',
                        database ='proyecto',
                        user ='root', 
                        password ='123456')
    cursor = connection.cursor()
    cursor.execute("SELECT SALDO FROM CUENTA WHERE iDCUENTA=1")
    row = cursor.fetchone()
    saldo_entry.insert(0, row[0])
    cursor = connection.cursor()
    cursor.execute("SELECT SALDO FROM CUENTA WHERE IDCUENTA=2")
    row = cursor.fetchone()
    phone_entry.insert(0, row[0])
#ESTA FUNCION TRANSACCIONAL NOS PERMITE EJECUTAR EL PROCEDIMIENTO ALMACENADO TRANSACCCIONAL EL CUAL
#SOLO NOS DEJA PARA DINERO DE UN A CUENTA A OTRA MIENTRAS LAS CANTIDADES ESTEN DENTRO DE LOS VALORES EXITENDES
#DE LA CUENTA QUE SE VA A TRANSFERIR
def Transaccional():
    con = mysql.connect(host="localhost", user="root", password="123456", database="proyecto")
    cursor = con.cursor()
    try:
      m6 = int(m6_Entry.get())
      m8 = int(m8_Entry.get())
      m7 = int(m7_Entry.get())
      cursor.callproc('PA_INSERTAR_TRANSACCIONAL', (m6, m8, m7))
      con.commit()
      print(f'Transferred {m7} from account {m6} to account {m8}')
      messagebox.showinfo("Status", "Transaccion Exitosa")
    except:
       messagebox.showinfo("Status", "fail")
       pass
#ESTA FUNCION NOTRANSACCIONAL NOS PERMITE EJECUTAR EL PROCEDIMIENTO ALMACENADO NOTRANSACCCIONAL EL CUAL
#SOLO NOS DEJA PARA DINERO DE UN A CUENTA A OTRA EXISTA O NO EXISTA DINERO EN UNA DE LAS CUENTAS
def NoTransaccional():
    con = mysql.connect(host="localhost", user="root", password="123456", database="proyecto")
    cursor = con.cursor()
    try:
      m6 = int(m6_Entry.get())
      m8 = int(m8_Entry.get())
      m7 = int(m7_Entry.get())
      cursor.callproc('PA_INSERTAR_NO_TRANSACCIONAL', (m6, m8, m7))
      con.commit()
      print(f'Transferred {m7} from account {m6} to account {m8}')
      messagebox.showinfo("Status", "Transaccion Exitosa")
#LUEGO DEL EXCEPT VOLVEMOS A EJECUTAR EL MISMO CODIGO QUE EN EL TRY YA QUE SI SOLO SE LO DEJA EN EL TRY
#NO SE EJECUTAR DEBIADO A QQUE EL ALTER CHECK QUE ESTABLECIO EN LA TABLA CUENTA NO PERMITE PASAR DINERO
#SI UNA CUENTA SUS VALORES SON IGUALES A 0 POR REPETIMOS LA FUNCION QUE SE EJECUTE EN EL TRY
    except:
      m6 = int(m6_Entry.get())
      m8 = int(m8_Entry.get())
      m7 = int(m7_Entry.get())
      cursor.callproc('PA_INSERTAR_TRANSACCIONAL', (m6, m8, m7))
      con.commit()
      print(f'Transferred {m7} from account {m6} to account {m8}')
      messagebox.showinfo("Status", "Transaccion Exitosa")



#ESTE APARTADO SON LAS INTEFACES GRAFICAS DEL PROYECTO DONDE SE ESTABLECEN LOS BOTONES Y LAS DEMAS COSAS
###################################################################################
saldo = Label(root, text="Cuenta1[ID en Base de datos=1]: ", font=("verdana 10"))
saldo.place(x=3, y=155)
saldo_entry = Entry(root, font=("verdana 10"))
saldo_entry.place(x=230, y=155)
phone = Label(root, text="Cuenta2[ID en Base de datos=2]: ", font=("verdana 10"))
phone.place(x=3, y=195)
phone_entry= Entry(root, font=("verdana 10"))
phone_entry.place(x=230, y=195)
btnSaldo= Button(root, text="Saldo", command=Saldo, font=("verdana 10")).place(x=520, y=150, width=180, height=60)
btn_transactional = Button(root, text="Transaccional", command=Transaccional, font=("verdana 10")).place(x=400, y=400, width=180, height=30)
btn_non_transactional= Button(root, text="No Transaccional", command=NoTransaccional, font=("verdana 10")).place(x=100, y=400, width=180, height=30)

###################################################################################
m1 = Label(root, text="Nombre de la instancia MySQL: ")
m1.config(text="Nombre de la instancia MySQL:           " + instance_name, font=("verdana 10"))
m1.place(x=3,y=5)   
m2 = Label(root, text="Puerto de la instancia MYSQL SERVER: ")
m2.config(text="Puerto de la instancia MYSQL SERVER:           " + instance_port, font=("verdana 10"))
m2.place(x=3,y=55)        
###################################################################################
m3 = Label(root, text="Transacción de transferencia bancaria", font=("verdena 10"))
m3.place(x=190,y=110)    
###################################################################################
m6 = Label(root, text="ID de la cuenta origen: ", font=("verdena 10"))
m6.place(x=3,y=280)
m6_Entry = Entry(root, font=("verdana 15"))
m6_Entry.place(x=150,y=285,width=170, height=20)   
###################################################################################
m7 = Label(root, text="Valor a transferir: ", font=("verdena 10"))
m7.place(x=3,y=320)
m7_Entry = Entry(root, font=("verdana 15"))
m7_Entry.place(x=150,y=325,width=170, height=20) 
###################################################################################
m8 = Label(root, text="ID de la cuenta destino: ", font=("verdena 10"))
m8.place(x=380,y=280)
m8_Entry = Entry(root, font=("verdana 15"))
m8_Entry.place(x=520,y=280,width=170, height=20) 
###################################################################################
m9 = Label(root, text="Valor según su instalación", font=("verdena 10"))
m9.place(x=420,y=5)
###################################################################################
m10 = Label(root, text="Puerto típico de MySQL", font=("verdena 10"))
m10.place(x=420,y=55)
###################################################################################
root.mainloop()