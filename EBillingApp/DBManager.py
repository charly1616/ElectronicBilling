import sqlite3
from Models import BillingModel as bm

userLogged = -1
empresa_id = -1
inventario = []

TIPOS_USUARIOS = ["MANAGER","EMPLOYEE"]

#DEVUELVE LA IDE DEL USUARIO CON LOS PARAMETROS Y -1 SI NO SE ENCUENTRA
def findUser(email,password):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()    
    cursor.execute("""SELECT USUARIO_ID FROM USUARIOS WHERE CORREO = ? AND CONTRASENA = ?"""
                   ,(email,password))
    fetch = cursor.fetchall().copy()
    connection.close()
    if len(fetch) == 0: return -1
    else: return fetch[0][0]

#DEVUELVE LA ID DEL USUARIO CON ESA ID Y SI NO EXISTE DEVUELVE -1
def findUserCompany(id):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""SELECT EMPRESA_ID FROM USUARIOS WHERE USUARIO_ID = ?""", (id,))
    fetch = cursor.fetchall().copy()
    connection.close()
    if len(fetch) != 0:
        return fetch[0][0]
    else: return -1
    
#ULTIMO USUARIO
def getLastUserID():
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""SELECT MAX(USUARIO_ID) FROM USUARIOS""")
    fetch = cursor.fetchall().copy()
    connection.close()
    if len(fetch) != 0:
        return int(fetch[0][0])
    else:
        return -1

#SI UN USUARIO CON ID ES MANAGER
def isUserManager(id):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""SELECT TIPO_USUARIO FROM USUARIOS WHERE USUARIO_ID = ?""",(id,))
    fetch = cursor.fetchall().copy()
    connection.close()
    if fetch[0][0] != None:
        return fetch[0][0] == TIPOS_USUARIOS[0]

#COLOCA UN NUEVO USUARIO EN LA BASE DE DATOS
def registerUser(email,password, name):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""INSERT INTO USUARIOS(USUARIO_ID, CONTRASENA, NOMBRE, CORREO, EMPRESA_ID) VALUES(?,?,?,?,?)""", (getLastUserID()+1,password,name,email,0))
    connection.commit()
    connection.close()

#OBTENER LOS PRODUCTOS DEVUELVE UN ARRAY CON OBJETOS DE TIPO ITEM
def getProducts(company_id):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""SELECT * FROM PRODUCTOS WHERE EMPRESA_ID = ?""",(company_id,))
    fetch = cursor.fetchall().copy()
    items = []
    connection.close()
    for eid, name, amount, price, company in fetch:
        items.append(bm.Item(id=eid,name=name,quantity=amount,unitPrice=price))
    return items

#ID ULTIMA DE LOS PRODUCTOS
def getLastProductId():
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""SELECT MAX(PRODUCTO_ID) FROM PRODUCTOS""")
    fetch = cursor.fetchall().copy()
    connection.close()
    if fetch[0][0] != None:
        return int(fetch[0][0])
    else:
        return -1

#SI EXISTE EL PRODUCTO LO ACTUALIZA SINO LO CREA
def UpdateOrInsertProduct(iid, name,amount,price):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""SELECT * FROM PRODUCTOS WHERE PRODUCTO_ID = ?""",(iid,))
    fetch = cursor.fetchall().copy()
    if fetch[0][0] != None:
        cursor.execute("""UPDATE PRODUCTOS SET NOMBRE = ?, CANTIDAD = ?, PRECIO = ? WHERE PRODUCTO_ID = ?""",(name,amount,price,iid))
    else:
        cursor.execute("""INSERT INTO PRODUCTOS(PRODUCTO_ID, NOMBRE, CANTIDAD, PRECIO) VALUES(?,?,?,?)""",(iid,name,amount,price))
    connection.commit()
    connection.close()
    
# BORRA PRODUCTO 
def DeleteProduct(iid):
    connection = sqlite3.connect('ebilling.db')
    cursor = connection.cursor()  
    cursor.execute("""DELETE FROM PRODUCTOS WHERE PRODUCTO_ID = ?""",(iid,))
    connection.commit()
    connection.close()