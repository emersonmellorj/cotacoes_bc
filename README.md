# Projeto para obter a moeda de melhor cotação frente ao dólar à partir do site do Banco Central:

Neste projeto iremos, através de um webservice, consultar a moeda de melhor cotação em uma determinada data frente ao dólar americano.

## Problema a ser resolvido:

Todos os dias a empresa precisa saber qual moeda possui a menor cotação frente ao dólar. Essa informação é importante para uma outra aplicação de ranking de moedas que eles irão desenvolver.

## Solução:

Procurei pensar em uma solução que já esteja preparada para a sua utilização por outro aplicativo futuramente. Esta informação foi muito importante para que o aplicativo fosse planejado e desenvolvido da forma como pensei. O projeto está estruturado da seguinte forma:

- Na camada mais alta foi desenvolvida uma API que possui um endpoint para, ao ser chamado, realizar o download do arquivo de cotações na data solicitada através do site do Banco Central. No momento esta API está aceitando apenas requisições do método get para o endpoint /api/v1/get_cotation/. Sendo assim, obterá a melhor cotação frente ao dólar americano e retornará as informações solicitadas;

- Para este primeiro momento foi criado um script que é um comando personalizado do django-admin chamado 'get_cotation.py'. Conforme solicitado, ele possui uma interface com o usuario via terminal. O mesmo é o responsável por chamar o endpoint da API e obter a melhor cotação, retornando a informação na tela para o usuário;

- Criada também uma tabela de lookup, aonde o script acima irá pegar os dados de símbolo da moeda e nome do país no qual esta moeda pertence. Esta tabela é uma função que está no arquivo get_file.py;

- Foram criados dois modelos de dados, que neste primeiro momento não estão sendo utilizados. Eles servirão quando for necessário armazenar os dados adquiridos. O primeiro modelo serve para armazenar a melhor cotação diária e o segundo modelo serve para armazenar todas as cotações obtidas de uma determinada data. Com isso, o processo de consulta fica muito mais rápido visto que, caso a informação que o usuário quer consultar já esteja na base, não é necessário pegar os dados novamente no site do Banco Central.

## Como utilizar este projeto:

Primeiramente, crie um ambiente virtual. Logo após, faça um clone deste projeto na pasta do ambiente virtual criado. Todas as bibliotecas necessárias para a utilização do projeto estão no arquivo requirements.txt

O segundo passo é instalar as bibliotecas que estao no arquivo citado acima, através do comando:
- pip install -r requirements.txt

Logo após, em um terminal, suba o servidor web Gunicorn: 
- gunicorn cotacoes_bc.wsgi

Após isso, para executar o script via terminal, basta abrir uma nova janela do terminal e acessar a pasta do ambiente virtual. Após, executar o comando abaixo:
-python manage.py get_cotation

Se quiser fazer uma requisição via Get na API, segue abaixo o endpoint criado:

- Endpoint: http://127.0.0.1:8000/api/v1/get_cotation/{data para pesquisa}
- Ex: http://127.0.0.1:8000/api/v1/get_cotation/20200706

## Servidor web que irá suportar a solução:

Escolhi o Gunicorn para receber as requisições. Para iniciar o serviço, basta executar o comando abaixo:
- gunicorn cotacoes_bc.wsgi


## Base de dados para armazenamento das informações:

Visto que os modelos foram apenas criados, sem utilização neste momento, deixei o SQLite mesmo como padrão. Quando o projeto for para produção, minha sugestão seria integrar com o Postgres.

## Testes automáticos com o coverage:

<img src='api/static/images/coverage_tests_api.png' />

### Para executar os testes automatizados:
- coverage run manage.py test
- coverage report

## Autenticação no acesso à API:

Neste primeiro momento não vi necessidade de colocar acesso autenticado à API.