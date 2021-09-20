lista = []
n = int(input())

for i in range(n):
  comando = input()

  params = comando.split(' ')

  if params[0] == 'anexar':
    lista.append(int(params[1]))
  elif params[0] == 'inserir':
    lista.insert(int(params[1]), int(params[2]))
  elif params[0] == 'imprimir':
    print(lista)
  elif params[0] == 'remover':
    lista.remove(int(params[1]))
  elif params[0] == 'ordenar':
    lista.sort()
  elif params[0] == 'inverter':
    lista.sort(reverse=True)
