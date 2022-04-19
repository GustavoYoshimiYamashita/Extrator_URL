
#url = 'https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
url = ''

#Sanitização da URL
url = url.strip()

if url == '':
    raise ValueError("Erro! A URL está vazia")

print(url)

#Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#Busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parameto = url_parametros.find(parametro_busca)
indice_valor = indice_parameto + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)

