import os
import json
import funciones.globales as gf
import modulos.corefiles as cf


def newproducto():
    title = """"
    ************************
    * REGISTRO DE PRODUCTOS *
    ************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input ("ingrese el nro de identificacion:")
    nombreproducto = input("ingrese  el nombre del producto: ")
    valorunitario = input("ingrese el valorunitario:")
    stockmin = input("ingrese el stockmin:")
    stockmax= input("ingrese el stockmax:")
    valorunitario = input("ingrese el valorunitario:") 
    

    producto = {
        "identificacion": identificacion,
        "nombreproducto": nombreproducto,
        "valorunitario": valorunitario,
        "stockmin": stockmin,
        "stockmax": stockmax,
        "valorunitario": valorunitario,
        
    }
    
    cf.AddData('data',identificacion,producto)
    gf.tienda.get('data').update({identificacion:producto})
    if(bool(input('Desea registrar otro medico S(Si) o Enter(No)'))):
        newproducto()
    else:
       uip.Menuproducto(0)
    
def SearchData():
     input('Ingrese el Nro Identificacion del medico: ')
     data=gf.tienda.get('data')
     return data
    

def ModifyData():
    dataproducto=SearchData()
    dataproducto= ()
    identificacion,nombreproducto,valorunitario,stockmin,stockmax,valorunitario = dataproducto.values()
    for key in dataproducto.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                dataproducto[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.tienda.get('data').update({identificacion:dataproducto})
    cf.UpdateFile(gf.tienda)
    uip.menuproductos