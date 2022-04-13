def multiply(x):
    p = x.index("*")
    r = x[p-1] * x[p+1]
    
    del x[p+1]
    x[p] = r
    del x[p-1]

def division(x):
    p = x.index("/")
    r = x[p-1] / x[p+1]

    del x[p+1]
    x[p] = r
    del x[p-1]

def adition(x):
    p = x.index("+")
    r = x[p-1] + x[p+1]

    del x[p+1]
    x[p] = r
    del x[p-1]

def substraction(x):
    p = x.index("-")
    r = x[p-1] - x[p+1]

    del x[p+1]
    x[p] = r
    del x[p-1]


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
            
        while True:
            
            if   "/" in operandos: division(operandos)
            elif "*" in operandos: multiply(operandos) 
            elif "-" in operandos: substraction(operandos)
            elif "+" in operandos: adition(operandos)
            else:
                break


        print(operandos[0])
        
        
        
