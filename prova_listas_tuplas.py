
#criando a variavel numeros como uma lista vazia para poder usar o append ao 
#usuario digitar o valor
numeros = []

#percorre uma range de 10 solicitando ao usuario digitar 10x um valor e adiciona
#a lista anteriormente criada numeros
for numero in range(10):
    valor = int(input(f'Digite o {numero+1} valor: '))
    numeros.append(valor)

#cria a lista vazia numeros_pares e numeros_impares para dar o append em cada,
#conforme a logica do if e else. Se sobrar resto da divisao do numero inserido
#por 2, quer dizer que o numero é impar e será alocado a lista numeros_impares,
#da mesma forma com os numeros pares.
numeros_pares = []
numeros_impares = []

for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

#criacao de variaveis para visualizacao das entradas em tuplas, "()".
tupla_numeros_pares = tuple(numeros_pares)
tupla_numeros_impares = tuple(numeros_impares)


print(tupla_numeros_pares, tupla_numeros_impares)

#contagem dos numeros inseridos na lista de numeros_pares e numeros_impares
qtd_numeros_pares = len(numeros_pares)
qtd_numeros_impares = len(numeros_impares)

print(f'A quantidade de numeros pares presentes na lista de numeros inseridos é de: {qtd_numeros_pares} e a quantidade de numeros impares presentes é de {qtd_numeros_impares} ')

#soma dos numeros pares e impares utilizando o sum
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)

print(f'A soma dos numeros pares é: {soma_pares}')
print(f'A soma de numeros impares é: {soma_impares}')