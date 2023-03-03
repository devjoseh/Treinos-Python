def contador_caracteres(texto):
    contador = {}
    for caractere in texto:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1
    return contador

texto = input("Digite o texto a ser contado: ")
resultado = contador_caracteres(texto)
print(resultado)
