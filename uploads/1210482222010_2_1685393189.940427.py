# -*- coding: utf-8 -*-
"""LP2023 - Avaliação 02 - Exercício 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MV5SfATykuwB1i8UY-tFGcADj0Dbm-Rt

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
### ENUNCIADO DO EXERCÍCIO 2

Uma sequência de Collatz em matemática pode ser definida da seguinte forma. 

Começando com qualquer número `n` inteiro positivo:

- Se `n` for par, o próximo número na sequência é `n / 2`

- Se `n` for ímpar, o próximo número na sequência é `3n + 1`

É conjecturado que toda sequência desse tipo eventualmente atinge o número 1.

Crie um programa que, dada como entrada um número inteiro positivo `n`, este imprima a lista gerada pela sequência de Collatz.

**Formato da entrada**

A entrada consiste num número inteiro positivo.

**Formato da saída**

Uma lista contendo a sequência de Collatz.

**Exemplo**

Entradas

```
12
```

Saída

```
[12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
```
"""

n = int(input())
lista = []

# Desenvolva seu programa a partir daqui.
lista.append(n)

while k > 1:
  if k % 2 == 0:
    k = k / 2
    lista.append(n)
  else:
    k = 3 * k + 1
    lista.append(n)

print(lista)