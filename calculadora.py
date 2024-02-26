

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Evita a divisão por zero
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return 0

# Exemplo de uso:
numero1 = 10
numero2 = 5
operacao = 3  # Multiplicação

resultado = calculadora(numero1, numero2, operacao)
print("Resultado da operação:", resultado)