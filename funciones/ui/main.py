import funciones.globales as fg
import modulos.corefiles as mf
import ui.uiproductos as uip
import os 

def mainmenu(op):
    title:"""
*************************
* MENU DE LA TIENDA*
*************************
""""
mainmenuOp: "1.registrar productos/n2. salir"
if(op ¡=2)
    print(title):
    print(mainmenuOp)
    try:
       opcion=in(input(":)"))
    except ValueError:
       print("opcion no valida")
       gf.pausar_pantalla
       mainmenu()

    else:
    match(opcion):
    case 1: 
      uip.menuproductos()
    case _:
       print()
       gf.pausar_pantalla

       mainmenu()

if _name_=="_main_":
cf.MI_DATABASE="data/productos.json"
cf.checkfile(gf.tienda)
mainmenu(0) 


    