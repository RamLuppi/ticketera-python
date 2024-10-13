import pickle, sys, os, random

os.system("cls")


numero_ticket=""
nombre=""
sector=""
asunto=""
mensaje=""

confirmacion=""
otro_ticket=""
#--------------------------------------FUNCION NUMERO DE TICKET ALEATORIO--------------------------------------------------------
def generar_numero_ticket():
      return random.randrange(1000, 9999)

       
#--------------------------------------FUNCION ALTA TICKET------------------------------------------------------------------------------
def generar_ticket():
      numero_ticket=""
      nombre=""
      sector=""
      asunto=""
      mensaje=""
      print("Ingrese los datos para Generar un nuevo Ticket:")
      numero_ticket=generar_numero_ticket()
      nombre=input("Ingrese su Nombre:")
      sector=input("Ingrese su Sector:")
      asunto=input("Ingrese Asunto:")
      mensaje=input("Ingrese un Mensaje:")
      ticket = {
        "Nombre": nombre,
        "Sector": sector,
        "Asunto": asunto,
        "Mensaje": mensaje
      }
      

      archivo_ticket = f"ticket_{numero_ticket}.pkl"
      
      with open(archivo_ticket, "wb") as f:
            pickle.dump(ticket, f)
      
      

      print(f"""
                  ==========================================================
                        Se genero un nuevo ticket
                  ==========================================================
            
                  Su nombre:{nombre}          Nº de ticket:{numero_ticket}
                  Sector:{sector}
                  Asunto:{asunto}

                  Mensaje:{mensaje}

                  Recordar su numero de ticket!!({numero_ticket})
            """)
      otro_ticket= input("Desea generar un nuevo ticket? (s/n): ")
                  
      if otro_ticket == 's':
            generar_ticket()
      elif otro_ticket == 'n':
            menu_principal()
      else:
            print("Opción no válida. Intente de nuevo.")
            menu_principal()
       

#--------------------------------------FUNCION LEER TICKET------------------------------------------------------------------------------
def leer_ticket():
      numero_ticket=input("Ingrese el numero de ticket:")
      
      archivo_ticket = f"ticket_{numero_ticket}.pkl"
      
      if os.path.isfile(archivo_ticket) == True:
            with open(archivo_ticket, "rb") as f:
                  ticket = pickle.load(f)


            print(f"""
                        ==========================================================
                              Nº de ticket:{numero_ticket}
                        ==========================================================
            
                        Su nombre: {ticket['Nombre']}        
                        Sector: {ticket['Sector']}   
                        Asunto: {ticket['Asunto']}   

                        Mensaje: {ticket['Mensaje']}   
                  """)
            otro_ticket= input("Desea ver otro ticket? (s/n): ")
                  
            if otro_ticket == 's':
                  leer_ticket()
            elif otro_ticket == 'n':
                  menu_principal()
            else:
                  print("Opción no válida. Intente de nuevo.")
                  menu_principal()
      else:
            print("Numero de ticket no encontrado. Intente de nuevo.")
            menu_principal()
        

#--------------------------------------FUNCION OPCIONES MENU PRINCIPAL------------------------------------------------------


def menu_principal():
      print(f"""
                  ==========================================================
                  "Hola bienvenido al sistema de Tickets"
            
                  "1 - Generar un nuevo ticket"
                  "2 - Leer un Ticket"
                  "3 - Salir"
                  ==========================================================
            """)
      menu_principal_opciones= input("Seleccione(1,2,3): ")
      if menu_principal_opciones == '1':
                  generar_ticket()
      if menu_principal_opciones == '2':
                  leer_ticket()
      if menu_principal_opciones == '3':
            confirmacion = input("¿Está seguro de que desea salir? (s/n): ")
            if confirmacion == 's':
                  sys.exit()
            elif confirmacion=='n':
                  menu_principal()
            else:
                  print("Opción no válida. Intente de nuevo.")
                  menu_principal()

#--------------------------------------EJECUCION DEL PROGRAMA-------------------------------------------------------
menu_principal()