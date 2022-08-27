from bisect import bisect
from bisect import insort
from copy import  deepcopy
from copy import copy

# bisect faz busca binaria O(log n), mais rapido
# em geral, os algoritmos de buscas de dados e ordenacao em Python sao O(n log n)

my_array = [1, 2, 3, 4, 'teste', False, True, 0.1] # array tipo misto

print(my_array)
print(my_array[0])   # [1]
print(my_array[-1])  # acessar ao ultimo elemento do array [0.1]
print(my_array[1:3]) # acessar o segundo elemento ate o quarto exclusivo [2, 3]
# print(my_array[150]) # acessar fora do range [list index out of range]

print(len(my_array))   # 8
print(my_array[len(my_array) - 1])  # acessar o ultimo elemento [0.1]
print(my_array[-2])                 # acessar o penultimo elemento [True]
print(my_array[-3])                 # acessar o antepenultimo elemento [False]

my_array = [8, 20, 34, 100, 2, 67, 35, 77, 100]
my_array.sort()
print(my_array)                     # [2, 8, 20, 34, 35, 67, 77, 100, 100]

my_array.insert(0, 999)             # tem um custo de processamento colocar um item num index
print(my_array)                     # [999, 2, 8, 20, 34, 35, 67, 77, 100, 100] tem que realocar todos os outros elementos

my_array.append(123)                # melhor forma pra inserir um item no array
print(my_array)                     # [999, 2, 8, 20, 34, 35, 67, 77, 100, 100, 123]

my_array.remove(999)                # remove direto o item

print(my_array)                     # [2, 8, 20, 34, 35, 67, 77, 100, 100, 123]

my_array[1] = None                  # melhor setar None em um item do que remover e ter que indexar todos os itens do array
del my_array[1]                     # remove o item na posicao 1 (com custo de processamento)
print(my_array)

print(min(my_array))                # [2]
print(max(my_array))                # [123]

print(bisect(my_array, 77))         # busque a posicao do item 77 [6]

insort(my_array, 62)                # inseriu e ordernou de forma mais rapida
print(my_array)                     # 2, 20, 34, 35, 62, 67, 77, 100, 100, 123]

my_array = range(0, 100)
print(list(my_array))               # [0, 1 .. 99]

matriz = [[123, 456], [789, 321]]
print(matriz)                       # [[123, 456], [789, 321]]
print(matriz[0])                    # [123, 456]
print(matriz[0][1])                 # 456

# tudo que tem em A tem em B e vice-versa | criou um ponteiro de A em B
A = [1, 2, 3]
B = A

print(A)                            # [1, 2, 3]
print(B)                            # [1, 2, 3]

B[0] = 187
print(B)                            # [187, 2, 3]
print(A)                            # [187, 2, 3]

# tudo que tem em a tem em b, se altero b, a esta intacto
a = [1, 2, 3]
b = list(a) # cria uma copia de a

b[0] = 29
print(b)                            # [29, 2, 3]
print(a)                            # [1, 2, 3]

# copy

a = [{'test': 123, 'bbb': 456}]     # dicionarios
b = copy(a)

b[0]['test'] = 77
print(a)                            # [{'test': 77, 'bbb': 456}] alterou 'a' tmb

# deep copy | nao altera a fonte

a = [{'test': 123, 'bbb': 456}]
b = deepcopy(a)

b[0]['test'] = 77
print(a)                            # [{'test': 123, 'bbb': 456}] nao alterou 'a'

# alterar as posicoes de 2 itens do array

c = [11, 34, 5, 88, 10]
print(c)                            # [11, 34, 5, 88, 10]
c[1], c[2] = c[2], c[1]             # troca o item da posicao 1 com 2 e vice-versa
print(c)                            # [11, 5, 34, 88, 10]


