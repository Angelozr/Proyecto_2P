import mysql.connector
conexion = mysql.connector.connect(user='root', password='mysql123',
                                    host='localhost',
                                    database='proyecto',
                                    port='3306')
print(conexion)