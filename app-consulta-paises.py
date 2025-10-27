import requests
import json

while True:

    url_base = "https://restcountries.com/v3.1/name/"
    pais = input("Digite o nome do país que você deseja informações (ou 'sair' para encerrar): ")
    if pais.lower() == 'sair':
        print("Encerrando o programa. Até mais!")
        break
    print(f"Buscando informações sobre {pais}...")

    url_completa = url_base + pais
    response = requests.get(url_completa)

    if response.status_code == 200:
        capital = response.json()[0]['capital'][0]
        populacao = response.json()[0]['population']
        regiao = response.json()[0]['region']
        idiomas = response.json()[0]['languages']
        moeda = response.json()[0]['currencies']

        print ("-------------------------------------------")
        print (f"País: {pais}")
        print (f"Capital: {capital}")
        print (f"População: {populacao}")
        print (f"Região: {regiao}")
        print ("Idiomas:")
        for idioma in idiomas.values():
            print (f"- {idioma}")
        print ("Moeda(s):")
        for moeda_info in moeda.values():
            print (f"- {moeda_info['name']} ({moeda_info['symbol']})")
        print ("-------------------------------------------")

    elif response.status_code == 404:
        print (f"País {pais} não encontrado. Verifique o nome e tente novamente.")
    else:
        print (f"Opa, algo deu errado! Código de status: {response.status_code} ")



