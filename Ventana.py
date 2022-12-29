from tkinter import *
from tkinter import ttk


from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ventana(Frame):
       
    def __init__(self, master=None):
        super().__init__(master,width=180, height=160)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def fSaldo(self):         
        pass

    def fNoTransaccional(self):
        pass

    def fTransaccional(self):
        pass

    def create_widgets(self):
        self.place(x=320,y=460,width=38, height=59)        
        self.btnNuevo=Button(text="Consultar saldo", command=self.fSaldo, bg="White", fg="black")
        self.btnNuevo.place(x=420,y=155,width=180, height=60 )                            
        lbl1 = Label(text="Nombre de la instancia SQL SERVER: ")
        lbl1.place(x=3,y=5)        
        self.txtNInstan=Entry()
        self.txtNInstan.place(x=220,y=5,width=190, height=20)                
        lbl2 = Label(text="Puerto de la instancia SQL SERVER: ")
        lbl2.place(x=3,y=55)        
        self.txtPuerto=Entry()
        self.txtPuerto.place(x=220,y=55,width=190, height=20)        
        lbl3 = Label(text="Transacción de transferencia bancaria")
        lbl3.place(x=190,y=110)                
        lbl4 = Label(text="Cuenta1[ID en Base de datos=1]: ")
        lbl4.place(x=3,y=155)        
        self.txtCuenta1=Entry()
        self.txtCuenta1.place(x=190,y=155,width=100, height=20) 
        lbl5 = Label(text="Cuenta2[ID en Base de datos=2]: ")
        lbl5.place(x=3,y=195)
        self.txtCuenta2=Entry()
        self.txtCuenta2.place(x=190,y=195,width=100, height=20) 
        lbl6 = Label(text="ID de la cuenta origen: ")
        lbl6.place(x=3,y=280)
        self.txtOrigen=Entry()
        self.txtOrigen.place(x=140,y=280,width=100, height=20)
        lbl7 = Label(text="Valor a transferir: ")
        lbl7.place(x=3,y=320)
        self.txtValorTrans=Entry()
        self.txtValorTrans.place(x=140,y=320,width=120, height=20)
        lbl8 = Label(text="ID de la cuenta destino: ")
        lbl8.place(x=320,y=280)
        self.txtCuentaD=Entry()
        self.txtCuentaD.place(x=460,y=280,width=120, height=20)
        lbl9 = Label(text="Valor según su instalación")
        lbl9.place(x=420,y=5)
        lbl10 = Label(text="Puerto típico de MySQL")
        lbl10.place(x=420,y=55)
        self.btnNoTrans=Button(text="Transferir (Modo no transaccional)", command=self.fNoTransaccional, bg="White", fg="black")
        self.btnNoTrans.place(x=60,y=355,width=200, height=30)
        self.btnTrans=Button(text="Transferir (Modo transaccional)", command=self.fTransaccional, bg="White", fg="black")
        self.btnTrans.place(x=320,y=355,width=200, height=30)