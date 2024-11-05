#1. Desarrolle el código fuente de un programa que permita ingresar cinco voltajes
# , obtener su promedio y visualizar `"ALTO VOLTAJE"`, si su promedio es mayor a 220,
#  caso contrario sea menor mostrar `"VOLTAJE CORRECTO"`.
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
        Welcome back Mr/Ms {name}, this is a program to calculate the voltage average for 5 values of voltage: \n 
        """) 
    try :    
            
        vOne =   float(input("        V1 =: "))
        vTwo =   float(input("        V2 =: "))
        vThree = float(input("        V3 =: "))
        vFour =  float(input("        V4 =: "))
        vFive =  float(input("        V5 =: "))
        
        
        totalV = (vOne + vTwo + vThree + vFour + vFive)/5
        print(f"""        Your final average voltage is: {totalV}\n""")
        if totalV > 220:
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