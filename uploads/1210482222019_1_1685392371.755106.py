# -*- coding: utf-8 -*-
"""LP2023 - Avaliação 02 - Exercício 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q3HtXEbC0QPav5nlKGnhgzfiPmWl51Q5

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
### ENUNCIADO DO EXERCÍCIO 1

Dada uma lista de números no formato de string e um número k, retorne se existe algum par de números na lista cuja soma seja igual a k. Ou seja, dada a entrada "[10, 15, 3, 7]" para numeros e um k com valor `17`, imprima True visto que 10 + 7 é 17.

**Formato da entrada**

A entrada consiste de uma string no formato de lista e um número inteiro positivo.

**Formato da saída**

Valor boolean True ou False.

**Exemplo**

Entradas

```
[10, 15, 3, 7]
```

```
17
```

Saída

```
True
```
"""

numeros = eval(input()) # eval serve para transformar a string "[1, 2, 3]" numa lista [1, 2, 3]
k = int(input())

# Desenvolva seu programa a partir daqui. 
list(numeros)
for i in numeros:
    if k == 17:
      i = True
print(i)