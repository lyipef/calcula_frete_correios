def buscar_cep(lista):
    for uf, cidade, logradouro in lista:
        url = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 400:
            print('Error 400')

        if response.status_code == 200:
        
            results = []
            if "erro" not in data:
                cep = data[0]["cep"]
                localidade = data[0]['localidade']
                results.append(f"{localidade}: {cep}")
            else:
                results.append(None)
    return results
