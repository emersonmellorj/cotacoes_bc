# Projeto para obter a cotação da moeda a partir do site do Banco Central

Neste projeto iremos, através de um webservice, consultar a moeda de melhor cotação em uma determinada frente ao dólar americano.

## Problema:

Todos os dias a empresa precisa saber qual moeda possui a menor cotação frente ao dólar. Essa informação é importante para uma outra aplicação de ranking de moedas que eles irão desenvolver.

## Solução:

Visto que esta aplicação desenvolvida será utilizada por outra aplicação no futuro, procurei desenvolver de forma que ela já esteja preparada para a integração futura. O projeto está estruturado da seguinte forma:

- Na camada mais alta existe uma API que possui um endpoint que, ao ser chamado, fará o download do arquivo de cotações da data solicitada através do site do Banco Central, obterá a melhor cotação frente ao dólar americano e retornará as informações solicitadas;

- Para este primeiro momento, foi criado um script chamado 'get_file.py', no qual possui uma interface com o usuario. Ele será o responsável por chamar o endpoint da API e obter a melhor cotação, retornando a informação na tela para o usuário;

- Uma tabela de lookup, aonde o script acima irá pegar os dados de símbolo da moeda e nome do país no qual esta moeda pertence;