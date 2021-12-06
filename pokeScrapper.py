import scrapy, json

class PokemonScrapper(scrapy.Spider):
  name = 'pokescrapper'
  domain = 'https://www.serebii.net'

  pokeInfo = []
  pokeDamage = []
  pokeStats = []

  start_urls = ["https://www.serebii.net/pokemon/nationalpokedex.shtml"]
  
  def parse(self, response):
    pokes = response.css('main table tr')
    for poke in pokes:
      self.parse_mainInfo(poke)
    

  def parse_mainInfo(self, response):
    pokeNumber = response.css('td::text').get()
    pokeName = response.css('td:nth-child(3)>a::text').get()
    hitPoints = response.css('td:nth-child(6)::text').get()
    attack = response.css('td:nth-child(7)::text').get()
    defense = response.css('td:nth-child(8)::text').get()
    specialAttack = response.css('td:nth-child(9)::text').get()
    specialDefense = response.css('td:nth-child(10)::text').get()
    speed = response.css('td:nth-child(11)::text').get()

    ability1 = response.css('td:nth-child(5)>a::text').get()
    ability2 = response.css('td:nth-child(5)>a:nth-child(3)::text').get()
    ability3 = response.css('td:nth-child(5)>a:nth-child(5)::text').get()

    type1 = response.css('td:nth-child(4)>a::attr(href)').get()
    type2 = response.css('td:nth-child(4)>a:nth-child(2)::attr(href)').get()

    
    if pokeName is not None:
        data = {
          "Num": pokeNumber,
          "Nome": pokeName,
          "HP": hitPoints,
          "Atk": attack,
          "Def": defense,
          "SAtk": specialAttack,
          "SDef": specialDefense,
          "Speed": speed,
          "Hab1": ability1,
          "Hab2": ability2,
          "Hab3": ability3,
          "Type1": type1,
          "Type2": type2
        }
        self.pokeStats.append(data)

    with open('pokemons_stats.json', 'w') as json_file:
      json.dump(self.pokeStats, json_file, indent = 2)