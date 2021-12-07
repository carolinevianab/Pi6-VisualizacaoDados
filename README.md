# Pokémon Dashboard
### Projeto Integrador do 6° Semestre de Ciência da Computação

### Por Caroline Viana e Richard Santino

### Visualização de dados: [https://visualizacaodados.carolineviana.repl.co](https://visualizacaodados.carolineviana.repl.co)
---

## Descrição
O projeto consiste em um dashboard para a visualização de informações relacionadas a tipos de Pokémon, coletadas com o uso de um scrapper da pokedéx [Serebii.net](https://www.serebii.net) e tratadas utilizando Pandas e agregações do MongoDB.

Foi utilizada a biblioteca Scrapy para a extração desses dados.

## Conteúdo do repositório e execução

### Scrapper

O repositório já possui o CSV com as informações já extraidas, podendo ser vistas nos arquivos `pokemonData.csv`.

Mas caso deseje executar o Scrapper desde o começo, siga as etapas:

O Scrapper possui dois arquivos necessários para sua execução:
- `main.py`: arquivo principal, de tratamento e salvamento;
- `pokeScrapper.py`: Scrapper para a pokedex [Serebii](https://www.serebii.net/pokemon/nationalpokedex.shtml);

A partir do Terminal, execute o scrapper a partir do comando `scrapy runspider pokeScrapper.py`. O processo pode demorar um pouco para finalizar, pois estamos lidando com uma base com mais de 800 dados. É importante que todos os arquivos estejam na mesma pasta

Ao final da execução, o arquivo `pokemons_stats.json` haverá sido gerado no diretório. Após isso, deve-se executar o arquivo `main.py`, para que as informações do arquivo json sejam tratadas. Ao final da execução, o arquivo `pokemonData.csv` será gerado no diretório.

### Processamento

O processamento dos dados foi feito a partir do mongodb,e pode ser visto no arquivo `data.json`. Caso deseje executá-los, é necessário inserir suas própria credenciais do mongodb.

- `insert.py`: arquivo responsável por adicionar os dados do CSV ao banco de dados.
- `consult.py`: arquivo em que foram feitos testes para consultas no banco.
- `mountjson.py`: arquivo responsável por gerar o json com dados agregados.

Para gerar o JSON, basta executar o arquivo `mountjson.py`. Após a execução, o arquivo `data.json` será gerado no diretório.

### Visualização

A visualização dos dados extraídos e agregados pode ser visto no [Pokémon Dash](https://visualizacaodados.carolineviana.repl.co).

A visualização foi construida utilizando javascript e jQuery, utilizando a biblioteca Charts.js.

O código HTML, CSS e JS da página pode ser visto [no repl do projeto](https://replit.com/@CarolineViana/VisualizacaoDados#index.html).
