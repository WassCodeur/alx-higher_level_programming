import dis

def ma_fonction():
    a = 5
    b = 10
    c = a + b
    print(c)

# Appelle la fonction dis pour afficher le bytecode de ma_fonction
dis.dis(ma_fonction)

