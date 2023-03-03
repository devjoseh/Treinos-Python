# Definir a função da calculadora
def calculadora():
    print("Escolha a operação que deseja realizar.")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Obter entrada do usuário para a escolha da operação
    escolha = input("Digite a sua escolha (1/2/3/4): ")

    # Obter entrada do usuário para os operandos
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Realizar operação com base na escolha do usuário
    if escolha == '1':
        resultado = num1 + num2
        print("O resultado da adição é:", resultado)
    elif escolha == '2':
        resultado = num1 - num2
        print("O resultado da subtração é:", resultado)
    elif escolha == '3':
        resultado = num1 * num2
        print("O resultado da multiplicação é:", resultado)
    elif escolha == '4':
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    else:
        print("Opção inválida.")

# Chamar a função da calculadora
calculadora()