import random

carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%#&?.,0123456789"

numero = int(input("Quantas senhas você deseja gerar? "))
tamanho = int(input("Quantos caractéres sua senha deve ter? "))

print('\nSenhas geradas com sucesso: ')

for pwd in range(numero):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(carac)
    print(senhas)