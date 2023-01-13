import mysql.connector
conexion = mysql.connector.connect(host ='localhost',
                                            database ='proyecto',
                                            user ='root', 
                                            password ='123456')
                                        
print(conexion)

                