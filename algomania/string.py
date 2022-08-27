msg = 'primeira string'
print(msg)

msg = 'teste ' * 5
print(msg)                  # teste teste teste teste teste

msg = 'A' * 1024
print(msg)

msg = 'primeira string'
print(msg.replace('string', 'mensagem'))    # primeira mensagem

print(msg.lower())
print(msg.upper())
print(msg.startswith('pri'))
print(msg.endswith('ing'))

dados = 'teste1, teste2, teste3'
print(dados.split(','))  # ['teste1', ' teste2', ' teste3']

dados = ' teste   '
print(dados.strip())

dados = ' teste   123'
print(dados.lstrip())   # teste   123 | tira o espaco do lado esquerdo

dados = ' teste   123'
print(dados.rstrip())   # teste   123 | tira o espaco do lado direito

print(dados.title())    # Teste   123 | primeira letra em maiusculo

numeros = '0123456789'
print(numeros[0])       # '0'
print(numeros[0:5])     # 01234 |  da posicao 0 ate a posicao 5

print(numeros[::-1])    # 9876543210 | inverte a ordem