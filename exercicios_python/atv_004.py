#algoritmo que receba 10 numeros e exiba a soma dos numeros pares


# soma=0
# cont=0
# def algoritmo(num):
#     soma=0
#     cont=0
#     for i in range (1,6):
#         if num %2 == 0:
#             soma+= num
#             cont+= 1
#             return soma, cont
# num =(input("Digite um número para somar os pares deles: ")) 
# algoritmo(num)
# print(f"{num}, tendo informado {cont} números pares, a soma dos pares é igual a: {soma}")
######## num dei conta , depois mexo
soma=0
cont=0
for i in range (6):
    num =int(input("Digite um número para somar os pares deles: ")) 
    if num % 2 == 0:         
            soma+= num
            cont+= 1
print(f" {cont} números pares, a soma dos pares é igual a: {soma}")