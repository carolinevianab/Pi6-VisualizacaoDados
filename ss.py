import scrapy, json

class PokemonScrapper(scrapy.Spider):
  name = 'pokescrapper'
  domain = 'https://www.serebii.net'

  pokeInfo = []

  start_urls = ["https://www.serebii.net/pokemon/nationalpokedex.shtml"]
  
  def parse(self, response):
    pokes = response.css('main table tr')
    limit = 0
    for poke in pokes:
      if limit == 20: break
      pokeName = poke.css('td:nth-child(3)>a::text').get()
      hitPoints = poke.css('td:nth-child(6)::text').get()
      attack = poke.css('td:nth-child(7)::text').get()
      defense = poke.css('td:nth-child(8)::text').get()
      specialAttack = poke.css('td:nth-child(9)::text').get()
      specialDefense = poke.css('td:nth-child(9)::text').get()

      ability1 = poke.css('td:nth-child(5)>a::text').get()
      ability2 = poke.css('td:nth-child(5)>a:nth-child(3)::text').get()
      ability3 = poke.css('td:nth-child(5)>a:nth-child(5)::text').get()

      #pokemonURL = poke.css('td:nth-child(3)>a').get()
      if pokeName is not None:
    #    yield {
    #      "Nome": pokeName,
    #      "HP": hitPoints,
    #      "atk": attack,
    #      "def": defense,
    #      "sAtk": specialAttack,
    #      "sDef": specialDefense,
    #      "hab1": ability1,
    #      "hab2": ability2,
    #      "hab3": ability3
    #      }
        data = {
          "Nome": pokeName,
          "HP": hitPoints,
          "Atk": attack,
          "Def": defense,
          "SAtk": specialAttack,
          "SDef": specialDefense,
          "Hab1": ability1,
          "Hab2": ability2,
          "Hab3": ability3
        }
        self.pokeInfo.append(data)
        limit += 1

    with open('pokemons_stats_serebii.json', 'w') as json_file:
      json.dump(self.pokeInfo, json_file, indent = 2)
        

        #ground = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(9)::text').get()
    
  # Pokedano por pokecada poketipo
  #def parse_damage(self,response):

    #with open('pokemons_dano_fraqueza_serebii.json', 'w') as json_file:
    #  json.dump(self.pokeDamage, json_file, indent = 2)

# scrapy runspider ss.py