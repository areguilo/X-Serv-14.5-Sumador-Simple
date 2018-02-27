#/usr/bin/python3
import sys



def suma(num1, num2):
    return num1+num2
    
def resta(num1, num2):
    return num1-num2
 
def multiplicacion(num1, num2):
    return num1*num2
    
def division(num1, num2):
    return num1/num2
      
diccionario = {"sum":suma, "res":resta, "mul":multiplicacion, "div":division}
     
#op = diccionario[op]  

#op(num1, num2)
    
#def suma(1,2)
#    return 1+2

