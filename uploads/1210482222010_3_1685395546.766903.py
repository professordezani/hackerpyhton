# -*- coding: utf-8 -*-
"""LP2023 - Avaliação 02 - Exercício 03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hXd-qDrk4rwKrVmTwLQvg_6gQrBh2y3Z

Curso de Tecnologia em Análise e Desenvolvimento de Sistemas da Faculdade de Tecnologia de São José do Rio Preto
# Avaliação de Linguagem de Programação
## Prof. Dr. Henrique Dezani

---
### SUBMISSÃO

Para submeter a sua solução, siga as etapas:
1. Faça o download do código python clicando em File -> Download -> Download.py
2. Acesse o _link_
3. Faça o login usando seu número de matrícula
4. Faça o _upload_ do Exercício (arquivo que fez o _download_ do Colab na etapa 2). 

Não se esqueça de escolher o exerício correto durante a submissão.

---
### ENUNCIADO DO EXERCÍCIO 3

Compute a mediana atual de uma sequência de números. Ou seja, dado um fluxo de números, imprima a mediana da lista até o momento em cada novo elemento.

Lembre-se de que a mediana de uma lista de números pares é a média dos dois números do meio.

Por exemplo, dada a sequência  `[2, 1, 5, 7, 2, 0, 5]`, seu algoritmo deve imprimir `[2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]`.

**Formato da entrada**

A entrada consiste numa string que representa a lista de números da sequência.

**Formato da saída**

Uma lista de números no formato float com 1 casa decimal que contemple as medianas calculadas.

**Exemplo**

Entradas

```
[2, 1, 5, 7, 2, 0, 5]
```

Saída

```
[2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]
```
"""

sequence = eval(input()) # eval serve para transformar a string "[1, 2, 3]" numa lista [1, 2, 3]
# Desenvolva seu programa aqui.

lista = []

for i,n in enumerate(sequence):
  if i == 0:
    lista.append(float(n))
  if i == 1:
    x = (sequence[i] + sequence[i-1]) / 2
    lista.append(float(x))
  if i == 2:
    listax = sorted(sequence[0:2])
    x = listax[1]
    lista.append(float(x))
  if i == 3:
    listax = sorted(sequence[0:4])
    x = (listax[1] + listax[2]) / 2
    lista.append(x)
  if i == 4:
    listax = sorted(sequence[0:5])
    x = listax[2]
    lista.append(float(x))
  if i == 5:
    listax = sorted(sequence[0:6])
    x = (listax[2] + listax[3]) / 2
    lista.append(float(x))
  if i == 6:
    listax = sorted(sequence[0:7])
    x = listax[3]
    lista.append(float(x))
  if i == 7:
    listax = sorted(sequence[0:8])
    x = (listax[4] + listax[5]) / 2
    lista.append(float(x))
  if i == 8:
    listax = sorted(sequence[0:9])
    x = listax[4]
    lista.append(float(x))

print(lista)

