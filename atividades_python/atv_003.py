#função para verificar se uma palavra da frase é um palindromo
def palindromo(str):
    str_inversa = str[::-1]
    if (str == str_inversa):
        print(f'{str} é um palíndromo')
        return True
    elif (str != str_inversa):
        print(f'{str} não é um palíndromo')
        return False
    
str=(input("Coloque uma palavra para verificar se é um palídromo: "))
palindromo(str)    