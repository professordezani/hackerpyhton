url = input()
lista = url.split(' ')
slug = '-'.join([palavra.lower() for palavra in lista if palavra != ''])
print(slug)