def eliminandoCaracteres(str1, str2):
    out1 = ""
    out2 = ""
    for caracter in str1.lower():
        if caracter not in str2.lower():
            out1 += caracter
    for char in str2.lower():
        if char not in str1.lower():
            out2 += char
    print(f"out1: {out1}")
    print(f"out2: {out2}")


string1 = input("Ingrese una cadena de caracteres: ")
string2 = input("Ingrese otra cadena de caracteres: ")
eliminandoCaracteres(string1, string2)
