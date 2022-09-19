
import mysql.connector


con = mysql.connector.connect(host='localhost', database='cadastro', user='root', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor ',db_info)
