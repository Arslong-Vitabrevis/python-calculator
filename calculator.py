
while True:
    expresion = input(">> ")

    if expresion == "exit": 
        break
    
    if expresion.isalpha() == False:
        
        x = expresion.split(" ")
        operandos = []
    
        for i in x:
            try:
                operandos.append(int(i))
            except:
                operandos.append(i)
    
        if "*" in operandos:
            l = operandos.index("*")
            resultado = operandos[l-1] * operandos[l+1]
            print(resultado)
        elif "+" in operandos:
            l = operandos.index("+")
            resultado = operandos[l-1] + operandos[l+1]
            print(resultado)

        if "/" in operandos:
            l = operandos.index("/")
            resultado = operandos[l-1] / operandos[l+1]
            print(resultado)
        elif "-" in operandos:
            l = operandos.index("-")
            resultado = operandos[l-1] - operandos[l+1]
            print(resultado)