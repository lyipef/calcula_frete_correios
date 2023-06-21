# Calcular Frete

Recentemente, tive um projeto no meu local de trabalho que envolvia a obtenção de informações da API dos Correios Brasil. No entanto, enfrentei dificuldades para obter os materiais necessários para essa integração. A API dos Correios é um serviço de aplicação que pode ser acessado utilizando protocolos padrão da Web, como HTTP, HTTPS, entre outros. Como resultado disso, decidi criar meu próprio script em Python para calcular o frete, possibilitando sua integração com o seu sistema ERP.


Além disso conta com um script adicional que te retorna o cep, passando os parametros da função, sendo: UF, Cidade e Logradouro.

## Como Funciona?

Utilizar o script é bastante simples. Basta definir o CEP de origem e fornecer uma lista contendo os CEPs de destino para os quais deseja saber o preço do frete.

## Leitura complementar

| Nome | Link de acesso | 
|------|-----------------|
| Documentações do Projeto | [Correios PDF](https://www.correios.com.br/atendimento/developers/arquivos/manual-de-integracao-cliente-contrato-apis.pdf) |

## Resultados
![image](https://github.com/lyipef/calcula_frete_correios/assets/120730541/3553156b-d705-41cd-8cf0-cdf88fd39452)


O script retornará uma lista formatada, pronta para ser mapeada em um dataframe.

