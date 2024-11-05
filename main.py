#2. Desarrolle el código fuente de un programa que permita calcular el área de un triángulo equilátero,
#  adicional visualizar `"DATOS NO VÁLIDOS"`, # si el área es mayor a 1000.
#
#   La fórmula para calcular el área `A` de un triángulo equilátero de lado `a` es:
#
#
#   ![](https://i.ibb.co/PTy9hV9/image.png)
#
#   **Explicación**:
#
#   - Un triángulo equilátero tiene todos sus lados iguales, y sus ángulos interiores son todos de 60 grados.
#   - Esta fórmula se deriva usando trigonometría y geometría básica aplicadas a un triángulo equilátero.
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
        Welcome back Mr/Ms {name}, this is a program to calculate the area of a equilateral triangle based on 1 side: \n
        """) 
    try :    
        side =   float(input("        Enter the side of the triangle = "))

        if side > 0:
            
            area = ((math.sqrt(3))/4) * (math.pow(side,2))

            if area > 1000: 
                print("        NO VALID DATA")
            else:
                print(f"        {round(area,4)}") 

        else:
            print("\n        Positive numbers only")

        
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