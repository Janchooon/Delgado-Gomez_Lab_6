# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:58:45 2020

@author: janso
"""
Letras_Ascii = []
Mensaje_Cifrado = []
Mensaje_Decifrado = []

Entrada = open('mensajeentrada.txt','r') #Txt que contiene el texto plano

for i in Entrada.read():
    Letras_Ascii.append(ord(i))
#TextoPlano = Entrada.readlines()[0] #Extrae el texto plano del archivo
Entrada.close()

print(Letras_Ascii,"\n")
    
#Público
P=199
G=70 #Alpha, raíz primitiva de P 

A=13 #Clave Privada Emisor

k = pow(G,A) % P #Clave pública

print("clave pública: (G,P,k) =(", G,",", P,",", k,")\n")

Cifrado =  ""

#Cifrado
B=45 #Clave Privada Receptor
y1 = pow(G,B) % P

for i in Letras_Ascii:
    m = i
    y2 = pow(k,B)*m % P
    Mensaje_Cifrado.append(y2)
    Cifrado += chr(y2)
    
print("Cifrado ELGAMAL:", Mensaje_Cifrado,"\n")

print("Cifrado:", Cifrado, "\n")

print("Cb(",Letras_Ascii,",",B,") = (",y1,",",Mensaje_Cifrado,")\n") #Respuesta

#Decifrado
for i in Mensaje_Cifrado:
    y2 = i
    m = (pow(y1,(P-1-A))*y2) % P
    Mensaje_Decifrado.append(m)

print("Decifrado en ASCII:", Mensaje_Decifrado, "\n")

Decifrado = ""

for i in Mensaje_Decifrado:
    Decifrado += chr(i)
    
print("Decifrado:", Decifrado)






