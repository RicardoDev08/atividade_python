#mostrar a tabuada de um numero informado pelo usuario

def tabuada(n):
    for i in range(1,11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
n = int(input("Digite um número para descobrir sua tabuada: "))
tabuada(n) # CHAMA A FUNÇÃO
