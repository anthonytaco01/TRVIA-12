import time
import random
for x in range(1,4) :
 print('hola inicia en:', x)
time.sleep(1)
puntaje = random.randint(0, 10)
iniciar_trivia = True
intentos = 0
from colorama import Fore, Back
print(Fore.RED+'Hola guapisimo!''\U0001F60A \n')
print('bienvenido a mi trivia sobre cultura general!''\U0001F4AC')
print('tienes', puntaje,'puntos llega a los maximos puntos posibles :)\n')
nombre = input('ingrese su nombre: ')
while iniciar_trivia == True:
 intentos +=1
 puntaje = random.randint(0, 10)  
 print(Fore.WHITE+'numero de intentos: ', intentos)
 input('presiona enter para empezar')
 from colorama import Fore, Back
 print(Fore.RED+"\n Hola", nombre, "'\U0001F9D0''responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
 time.sleep(2)
 from colorama import Fore, Back
 print (Fore.YELLOW+'primera pregunta\n')
 print('1) ¿Cuál es el océano más grande del mundo?''\U0001F3C4')
 print('a)pacifico')
 print('b)indico')
 print('c)atlantico')
 print('d)artico')
 print('e)antartico')
 print('tienes 5 segundos para pensar tu alternativa')
 time.sleep(5)
 respuesta = input("Enter respuesta: ")
 while respuesta not in ("a", "b", "c", "d","e"):
  respuesta = input("Debes responder a,b,c,d o e Ingresa nuevamente tu respuesta: ")
 if respuesta == "b":
  print("Incorrecto!", nombre, "su grandesa de indico es de 73.556.000 km2")
  puntaje = puntaje * 3
 elif respuesta == "c":
  print("Incorrecto!", nombre, "su grandesa de atlantico es de 106.400.000 km2")
  puntaje = puntaje + 2
 elif respuesta == "d":
  print("Incorrecto!", nombre, "su grandesa de artico es de 14.090.000 km2")
  puntaje = puntaje / 2
 elif respuesta == "e":
  print("Incorrecto!", nombre, "su grandesa de antartico es de 20.327.000 km2")
  puntaje = puntaje - 3
 else:
  puntaje *= 15
  print("Muy bien compañero ", nombre, "exactamente la grandeza de el oceano pacifico es de 200.700.000 km2 !\n")
 lista = (puntaje)
 print(lista)
 from colorama import Fore, Back
 print(Fore.GREEN+'-siguiente pregunta:\n')
 print('2) ¿Cuál es el libro más vendido de la historia?''\U0001F4D6')
 print('a)citas del presidente mao tse-tung')
 print('b)harry potter')
 print('c)señor de los anillos')
 print('d)la biblia')
 print('e)crepusculo') 
 print('tienes 5 segundos para pensar tu alternativa')
 time.sleep(5)
 respuesta = input("Enter respuesta: ")
 while respuesta not in ("a", "b", "c", "d","e"):
  respuesta = input("Debes responder a,b,c,d o e Ingresa nuevamente tu respuesta: ")
 while respuesta not in ("a", "b", "c", "d","e"):
  respuesta = input("Debes responder a,b,c,d o e Ingresa nuevamente tu respuesta: ")
 if respuesta == "b":
  print("Incorrecto!", nombre, "las copias vendidas de harry potter fueron 400 millones")
  puntaje = puntaje * 3
 elif respuesta == "c":
  print("Incorrecto!", nombre, "las copias vendidas del señor de los anillos fueron 103 millones")
  puntaje = puntaje + 2
 elif respuesta == "a":
  print("Incorrecto!", nombre, "las copias vendidas de citas del presidente mao tse-tung fueron 828 millones")
  puntaje = puntaje / 3
 elif respuesta == "e":
  print("Incorrecto!", nombre, "las copias vendidas de crepusculo fueron de 43 millones")
  puntaje = puntaje + 3
 else:
  puntaje *= 20
  print("Muy bien compañero ", nombre, "exactamente el libro mas vendido es la biblia con 3900millones de copias!\n")
 lista = (puntaje)
 print(lista)
 from colorama import Fore, Back
 print(Fore.BLUE+'-siguiente pregunta:\n')
 print('3) ¿Cuánto vale el valor de pi?''\U0001F202')
 print('a)2.1416')
 print('b)3.1416')
 print('c)3.1614')
 print('d)2,1512')
 print('e)3,1816')  
 print('tienes 5 segundos para pensar tu alternativa')
 time.sleep(5)
 respuesta = input("Enter respuesta: ")
 while respuesta not in ("a", "b", "c", "d","e"):
  respuesta = input("Debes responder a,b,c,d o e Ingresa nuevamente tu respuesta: ")
 while respuesta not in ("a", "b", "c", "d","e"):
  respuesta = input("Debes responder a,b,c,d o e Ingresa nuevamente tu respuesta: ")
 if respuesta == "a":
  print("Incorrecto!", nombre, "no es 2 en vez de 3")
  puntaje = puntaje - 3
 elif respuesta == "c":
  print("Incorrecto!", nombre, "no es 3,1614 el 16 no es antes q el 14")
  puntaje = puntaje / 3
 elif respuesta == "d":
  print("Incorrecto!", nombre, "no podria salir este resultado")
  puntaje = puntaje * 3
 elif respuesta == "e":
  print("Incorrecto!", nombre, "es un resultado erroneo")
  puntaje = puntaje - 5
 else:
  puntaje *= 5
  print("Muy bien compañero ", nombre, "exactamente el valor de pi es 3,1416 !\n")
  lista = (puntaje)
  print(lista)
  from colorama import Fore, Back
  print(Fore.WHITE+'vamos a ver cuanto puntaje sacaste espera 5 segundos para verificar \n')
  time.sleep(5)
  print ("¡Gracias!", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"'\U0001F44D')
  from colorama import Fore, Back
 print(Fore.WHITE+"\n¿Deseas intentar la trivia nuevamente?")
 repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
 if repetir_trivia != "si":  
  print("\nEspero ",nombre , "que lo hayas pasado bien, hasta pronto!")
  iniciar_trivia = False
  lista = (intentos,puntaje)
  print(lista)
  