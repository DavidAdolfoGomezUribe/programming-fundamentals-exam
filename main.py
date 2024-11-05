#Desarrolle un programa que solicite ingrese tres voltajes 
#distintos e indique si el promedio de los voltajes ingresados 
#es menor a 115 visualice `"VOLTAJE CORRECTO"`, caso contrario sea
#mayor a 115 y menor a 220 visualice `"ALTO VOLTAJE"`, y si es mayor 
#a 220 visualice `"PELIGRO"`.
   
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
        Welcome back Mr/Ms {name}, this is a program to calculate danger for the voltage average for 3 values of voltage: \n 
         """) 
    try :    

        vOne =   float(input("        V1 =: "))
        vTwo =   float(input("        V2 =: "))
        vThree = float(input("        V3 =: "))
        

        totalV = (vOne + vTwo + vThree )/3
        print(f"""\n        Your final average voltage is: {totalV}""")
        if totalV >= 220:
            print("\n        DANGER")
        elif totalV > 115 and totalV < 220:
            print("\n        HIGH VOLTAGE")
        else:
            print("\n        Correct Voltage")
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