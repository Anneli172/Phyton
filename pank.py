# Kui peaksid lisama võimaluse. et inimene saab ise valida tegevuse ja summa, siis kuhu sa selle lisaksid?

def konto_haldur(algsaldo, toiming, summa):
    if toiming == "deposiit":
        algsaldo += summa
    elif toiming == "valjavote":
        if summa <= algsaldo:
            algsaldo -= summa  # Indented correctly
        else:
            print("Ei ole piisavalt raha kontol.")
    else:
        print("Makse ei õnnestunud.")
    
    return algsaldo

# Test the function
saldo = 200
print("Algsaldo:", saldo)



saldo = konto_haldur(saldo, "deposiit", 50)
print("Uus saldo pärast deposiiti:", saldo)

saldo = konto_haldur(saldo, "valjavote", 80)
print("Uus saldo pärast väljavõtet:", saldo)

saldo = konto_haldur(saldo, "valjavote", 150)
print("Uus saldo peale raha liikumist:", saldo)
