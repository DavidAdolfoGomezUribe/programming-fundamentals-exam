#Desarrolle el código fuente de un programa que permita ingresar y
#leer el valor correspondiente a una distancia en metros y la visualice expresadas en km.
#
#Para convertir `metros` a `kilómetros`, puedes usar la siguiente fórmula:
#

import math     

print(f""" 
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝                                                        
                                """) 
name = input("    Hello, please enter your full name:  ")
while True:

    print(f""" \n
        Welcome back Mr/Ms {name}, this is a program to convert meters to kilometers: \n 
         """) 
    try :    

        meters =   float(input("        Please enter the amount of meters : "))
        
        
        kilometers = meters/1000
        print(f"""\n        For this amount of {meters} meters, the kilometers are: {kilometers} Km""")


        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye!")
                break
    except :            

        print("        Error: Enter the correct data")
        continueAsk = input( "\n    Do you want to calculate again? (yes/no): " ).strip().lower()

        if continueAsk != "yes" :
                print("    Thaks for using the program. Goodbye!")
                break                  
       
      
      
        #last line of code  