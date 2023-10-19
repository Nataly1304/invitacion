import time

#Imprimimos un mensaje acerca de la invitación de la fiesta y usamos un time.sleep para que se pueda leer primero antes de llenar el formulario
print("Hola te invitamos a la fiesta de disfraces que realizaremos el dia 31 de octubre del 2023 en el salon juan calle 5 avenida sur a las 6:00 pm\nPara que puedas asistir deberas llenar el siguiente formulario para saber si cumples con los requisitos para ingresar")
time.sleep(2)

#Esta variable inicia en cero para ir añadiendo los invitados aceptados con el ciclo
ingresados = 0

while True:

#Solicitamos el nombre de la persona que va a asistir
  nombre=input("Ingresa tu nombre ('terminar' para finalizar formulario): ")

#Esto es para romper el ciclo y mostrar las personar que llenaron el formuario
  if nombre.lower() == 'terminar':
       break

#Solicitamos la edad de la persona ya que necesitamos que sea mayor de edad para poder ingresar
  edad = int(input("Escribe tu edad: "))

#Empezaremos a comprobar si la persona cumple con los requisitos para poder asistir a la fiesta
  if edad >= 18:
    disfraz=input("¿Cuentas con un disfraz sobre la tematica de la fiesta? Si/No: ")

    if disfraz.lower() == "si":
      formulario=input("¿Llenaste antes el formulario para ingresar? Si/No: ")
    
      if formulario.lower() == "no":
         acompañantes=input("¿Asistiras con alguien mayor de edad? Si/No: ")

         if acompañantes.lower() == "si":
           ingresados += 1
           print("Cumples con todos los requisitos para ingresar ¡Bienvenido!")
           continue
#Si la persona no llega a cumplir con un requisito se rechazara el formulario
  print("No cumples con los requisitos para ingresar")

#Al romper el ciclo mostrara la cantidad de personas que cumplieron con los requisitios del formulario
print(f"Personas que cumplen con el ingreso: {ingresados}")
