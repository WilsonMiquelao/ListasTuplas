Lógica do Programa
Entrada de Dados
O programa começa criando uma lista vazia chamada numeros.
Em seguida, com um for de 0 a 9 (range(10)), o usuário é solicitado a digitar 10 números. Cada número digitado é adicionado à lista usando .append().

Classificação entre Pares e Ímpares
Duas listas vazias são criadas: numeros_pares e numeros_impares.
Com outro for, o programa percorre a lista numeros e usa o operador % para verificar se o número é par (num % 2 == 0) ou ímpar.
Conforme a verificação, o número é adicionado à lista correspondente.

Conversão para Tuplas
Após a separação, ambas as listas são convertidas em tuplas para apresentação visual no formato com parênteses.

Estatísticas
O programa calcula:

A quantidade de números pares e ímpares com len()
A soma dos números pares e ímpares com sum()
Saída Final
Todas as informações (tuplas, quantidades e somas) são exibidas para o usuário com print().

