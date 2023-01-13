from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import socket

root = Tk()
root.geometry("750x450")
root.title("MySQL CRUD Operations")

dato1=StringVar()
dato2=StringVar()
dato3=StringVar()

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

# SALDO function
def Select():
    con = mysql.connect(host="localhost", user="root", password="123456", database="proyecto")
    cursor = con.cursor()
    cursor.execute("select * from cuenta")
    
    rows = cursor.fetchmany()
    for row in rows:
      saldo_entry.insert(6, row[1])
      row = cursor.fetchone()
      print(row);  
      phone_entry.insert(6, row[1])
      con.close();


insert_stmt = (
    "CALL PA_INSERTAR_TRANSACCIONAL(%s,%s,%s)"
)

def Transaccional():
    con = mysql.connect(host="localhost", user="root", password="123456", database="proyecto")
    cursor = con.cursor()
    try:
        datos1= (dato1.get(), dato2.get(), dato3.get())
        cursor.execute(insert_stmt,datos1)
        row = cursor.fetchone()
        print(row);
        cursor.close()
        MessageBox.showinfo(message="Transaccion Exitosa",title="Felicidades!")
    except:
       MessageBox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
       pass

llamada = (
    "CALL PA_INSERTAR_NO_TRANSACCIONAL(%s,%s,%s)"
)
def NoTransaccional():
    con = mysql.connect(host="localhost", user="root", password="123456", database="proyecto")
    cursor = con.cursor()
    try:
        datos1= (dato1.get(), dato2.get(), dato3.get())
        cursor.execute(llamada,datos1)
        n=cursor.rowcount
        con.commit()
        row = cursor.fetchone()
        print(row);
        cursor.close()
        MessageBox.showinfo(message="Transaccion Exitosa",title="Felicidades!")
    except:
        MessageBox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
        pass
        

###################################################################################
saldo = Label(root, text="Cuenta1[ID en Base de datos=1]: ", font=("verdana 10"))
saldo.place(x=3, y=155)
saldo_entry = Entry(root, font=("verdana 10"))
saldo_entry.place(x=230, y=155)
phone = Label(root, text="Cuenta2[ID en Base de datos=2]: ", font=("verdana 10"))
phone.place(x=3, y=195)
phone_entry= Entry(root, font=("verdana 10"))
phone_entry.place(x=230, y=195)
btnSelect= Button(root, text="Consultar Saldo", command=Select, font=("verdana 10")).place(x=520, y=150, width=180, height=60)
btnTran= Button(root, text="Transaccional", command=Transaccional, font=("verdana 10")).place(x=400, y=400, width=180, height=30)
btnNoTran= Button(root, text="No Transaccional", command=NoTransaccional, font=("verdana 10")).place(x=100, y=400, width=180, height=30)

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
m6_Entry = Entry(root, font=("verdana 15"), textvariable=dato1)
m6_Entry.place(x=150,y=285,width=170, height=20)   
###################################################################################
m7 = Label(root, text="Valor a transferir: ", font=("verdena 10"))
m7.place(x=3,y=320)
m7_Entry = Entry(root, font=("verdana 15"), textvariable=dato3)
m7_Entry.place(x=150,y=325,width=170, height=20) 
###################################################################################
m8 = Label(root, text="ID de la cuenta destino: ", font=("verdena 10"))
m8.place(x=380,y=280)
m8_Entry = Entry(root, font=("verdana 15"), textvariable=dato2)
m8_Entry.place(x=520,y=280,width=170, height=20) 
###################################################################################
m9 = Label(root, text="Valor según su instalación", font=("verdena 10"))
m9.place(x=420,y=5)
###################################################################################
m10 = Label(root, text="Puerto típico de MySQL", font=("verdena 10"))
m10.place(x=420,y=55)
###################################################################################
root.mainloop()