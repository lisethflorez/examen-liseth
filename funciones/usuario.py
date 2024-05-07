import os

def usuario():
    title:"""
***************************
* INFORMACION DEL USUARIO *
***************************
"""" 
    
print("ingrese la informacion del usuario")
id=input("ingrese la identidada del usuario")
nombre= input("ingrese el nombre del usuario")
apellido= input("ingrese el apellido del usuario")
ubicacion= input("ingrese la ubicacion del usuario")
direccion=input("ingrese la direccion del usuario")
ciudad=input("ingrese la ciudad del usuario")
longitud=input("ingrse la longitud del usuario")
latitud=input("ingrese la latitud del usuario")
email=input("ingrese el email del usuario")
edad=input("ingrese la edad del usuario")
ocupacion=print("ingrese la ocupacion del usuario")
usuario={
    id:"id",
    nombre:"nombre",
    apellido:"apellido",
    ubicacion:"ubicacion",
    direccion:"direccion",
    ciudad:"ciudad",
    longitud:"longitud",
    latitud:"latitud",
    email:"email",
    edad:"edad",
    ocupacion:"ocupacion"
}
if __name__ =="_main_":
  usuario 

