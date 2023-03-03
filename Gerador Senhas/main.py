#Faz a importação do random, do próprio python. Não precisa baixar nada
import random

#Caracteres que serão usados para gerar a senha. você pode colocar mais se quiser
carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%#&?.,0123456789"

#Inputs para perguntar sobre quantas senhas a pessoa quer gerar e com quantos caracteres
numero = int(input("Quantas senhas você deseja gerar? "))
tamanho = int(input("Quantos caractéres sua senha deve ter? "))

#Só envia um print pra deixar mais bonito o console.
print('\nSenhas geradas com sucesso: ')

#Função que cria as senhas
for pwd in range(numero):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(carac)
    print(senhas)