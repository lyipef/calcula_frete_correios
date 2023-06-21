import requests
import xml.etree.ElementTree as ET


ef obter_valor_envio(cep_origem, lista_cep_destino):
    valores_envio = []
    
    url_template = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx'

    for cep_destino in lista_cep_destino:
        params = {
            'nCdEmpresa': '11109378',
            'sDsSenha': '00000',
            'sCepOrigem': cep_origem,
            'sCepDestino': cep_destino,
            'nVlPeso': '0.3',
            'nCdFormato': '1',
            'nVlComprimento': '15',
            'nVlAltura': '15',
            'nVlLargura': '15',
            'sCdMaoPropria': 'n',
            'nVlValorDeclarado': '0',
            'sCdAvisoRecebimento': 'n',
            'nCdServico': '41106',
            'nVlDiametro': '9',
            'StrRetorno': 'xml',
            'nIndicaCalculo': '3'
        }

        response = requests.get(url_template, params=params)
        
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            valor_element = root.find('.//Valor')
            valor = valor_element.text

            valores_envio.append(f"{cep_destino}: {valor}")

    return valores_envio


 # Exemplo de uso
cep_origem = '12231-030'
lista_cep_destino = ['35060970', '12327380', '12329016']
valores = obter_valor_envio(cep_origem, lista_cep_destino)
print(valores)
