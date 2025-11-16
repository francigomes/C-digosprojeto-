# ======== CÓDIGO DA CALCULADORA SIMPLES ========

# Função de soma
def somar(a, b):
    return a + b  # retorna a soma dos dois valores

# Função de subtração
def subtrair(a, b):
    return a - b  # retorna a diferença entre os dois valores

# Função de multiplicação
def multiplicar(a, b):
    return a * b  # retorna o produto dos dois valores

# Função de divisão
def dividir(a, b):
    if b != 0:  # verifica se o divisor NÃO é zero
        return a / b  # realiza a divisão normalmente
    else:
        return "Erro: divisão por zero não é permitida!"  # evita erro no programa

# Exibe um título no terminal
print("=== Calculadora Simples ===")

# Mostra as operações disponíveis
print("Operações disponíveis:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recebe a escolha da operação do usuário
opcao = input("Escolha uma operação (1/2/3/4): ")

# Pede o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Pede o segundo número
num2 = float(input("Digite o segundo número: "))

# Verifica qual operação o usuário escolheu
if opcao == "1":
    print("Resultado:", somar(num1, num2))  # chama a função de soma

elif opcao == "2":
    print("Resultado:", subtrair(num1, num2))  # chama a função de subtração

elif opcao == "3":
    print("Resultado:", multiplicar(num1, num2))  # chama a função de multiplicação

elif opcao == "4":
    print("Resultado:", dividir(num1, num2))  # chama a função de divisão

else:
    print("Opção inválida!")  # caso o usuário digite algo que não existe
