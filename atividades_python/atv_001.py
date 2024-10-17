# criar uma função que calcule o fatorial de um numero dado pelo usuario

# def fatorial(n):
#     if n < 0:
#         print("Número Ngativo!")
#     else :
#         mult=1
#         for i in (1,n+1):
#              mult *=i
#              return mult
# n = int(input("Digite um número: "))
# print(f'O fatorial do número {n} é: {fatorial(n)}')        

#### outra forma mostrando só a multplicação fatorial

def fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    
    resultado = 1
    multiplicacao = ""

    for i in range(1, n + 1):
        resultado *= i
        multiplicacao += str(i)
        if i < n:
            multiplicacao += " x "  # Adiciona " x " somente se não for o último número
    
    multiplicacao += f" = {resultado}"  # Adiciona o resultado final
    
    return resultado, multiplicacao

numero = int(input("Digite um número para calcular o fatorial: "))
resultado_fatorial, multiplicacao_str = fatorial(numero)

if resultado_fatorial is not None:
    print(f"O fatorial de {numero} é: {resultado_fatorial}")
    print(f"A multiplicação dos números é: {multiplicacao_str}")