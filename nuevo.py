from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry("750x450")
root.title("MySQL CRUD Operations")
# Select function
def Select():
    con = mysql.connect(host ='localhost',
                        database ='proyecto',
                        user ='root', 
                        password ='123456')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM CUENTA")
    rows = cursor.fetchall()

    for row in rows:
      saldo_entry.insert(6, row[1])
      phone_entry.insert(0, row[1])
      con.close();

def Insert():
   saldo = saldo_entry.get()
   phone = phone_entry.get()
  
   if(id == "" or saldo == "" or phone == ""):
       MessageBox.showinfo("ALERT", "Please enter all fields")
   else:
       con = mysql.connect(host="localhost", user="root", password="123456", database="proyecto")
       cursor = con.cursor()
       cursor.execute("insert into Cuenta values('"+ saldo +"', '" + phone +"')")
       cursor.execute("commit")
  
       MessageBox.showinfo("Status", "Successfully Inserted")
       con.close();


###################################################################################
saldo = Label(root, text="Cuenta1[ID en Base de datos=1]: ", font=("verdana 10"))
saldo.place(x=3, y=155)
saldo_entry = Entry(root, font=("verdana 10"))
saldo_entry.place(x=230, y=155)
phone = Label(root, text="Cuenta2[ID en Base de datos=2]: ", font=("verdana 10"))
phone.place(x=3, y=195)
phone_entry= Entry(root, font=("verdana 10"))
phone_entry.place(x=230, y=195)
btnSelect= Button(root, text="Select", command=Select, font=("verdana 10")).place(x=520, y=150, width=180, height=60)
btnTran= Button(root, text="Transaccional", command=Insert, font=("verdana 10")).place(x=400, y=400, width=180, height=30)
btnNoTran= Button(root, text="No Transaccional", command=Select, font=("verdana 10")).place(x=100, y=400, width=180, height=30)

###################################################################################
m1 = Label(root, text="Nombre de la instancia SQL SERVER: ", font=("verdena 10"))
m1.place(x=3,y=5) 
m1_Entry = Entry(root, font=("verdana 15"))
m1_Entry.place(x=240,y=10,width=170, height=20)    
###################################################################################
m2 = Label(root, text="Puerto de la instancia SQL SERVER: ", font=("verdena 10"))
m2.place(x=3,y=55) 
m2_Entry = Entry(root, font=("verdana 15"))
m2_Entry.place(x=240,y=55,width=170, height=20)    
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