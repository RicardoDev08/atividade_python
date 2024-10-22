#uma função que mostre os n primeiros termos de uma sequencia de fibonacci, sendo n informado pelo usuario 

# n = int(input("Que termo deseja encontrar: "))
# ultimo=1
# penultimo=1

# if (n==1) or (n==2):
#     print("1")
# else:
#     for count in range(2,n):
#         termo = ultimo + penultimo
#         penultimo = ultimo
#         ultimo = termo
#         count += 1
#     print(termo)
def Fib(n):
    for i in range(n):
        if (n <=1):
            return n
    return (Fib(n - 2) + Fib(n - 1))
print(Fib(n))