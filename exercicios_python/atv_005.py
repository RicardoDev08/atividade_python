#função para verificar se um numero é primo

# verifica os números primos até o número mostrado pelo usuário

# num = int(input("Digite um número: "))
# for i in range (1,num + 1):
#     if num  % i == 0:
#         print('yes')
#     else:
#         print('no')    
#     print(f'{i}' ,end=' ')

#função para verificar se um numero é primo

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero=int(input("Digite um número: ")) 
if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

     