#Contador de caracteres simples. Ele faz a conta de quantas letras existem numa mesma frase. Exemplo:
# A mensagem foi: Bom Dia a todos. Resultado:
# 'B': 1, 'o': 3, 'm': 1, ' ': 4, 'd': 2, 'i': 1, 'a': 2, 't': 1, 's': 1

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
