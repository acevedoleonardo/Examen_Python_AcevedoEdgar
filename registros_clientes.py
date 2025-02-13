#Registro y Gestión de Usuarios 

import json 

def abrirJSON(): 
    dicFinal={}
    with open("./registros.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./registros.json","w") as outFile:
        json.dump("dic",outFile)
    
registros={}



def registros_mov():
    print("---------------------------------------------------------")
    print("Registro de Clientes")
    print("---------------------------------------------------------")
    nombre=input("Ingrese su Nombre: ")
    direccion=input("Ingrese su Direccion: ")
    telefono=input("Ingrese su Telefono: ")
    tiempo=input("¿Cuantos años tiene con la compañia movistar?: ")
    registros=abrirJSON()
    if (tiempo<="1"):
        print("==Categorias==")
        print("Nuevos Clientes")
    elif (tiempo>"1" and tiempo <="3"):
        print("==Categorias==")
        print("Clientes Regulares")
    else:
        print("==Categorias==")
        print("Clientes Leales")


#Abrir Json

registros=abrirJSON()

registros["clientes"].append({"nombre":nombre,
                            "direccion":direccion,
                           "telefono":telefono,
                           "tiempo":tiempo
                            })

#Guardar diccionario en el archivo JSON
guardarJSON(registros)
print("Usuario Agregado Exitosamente")

