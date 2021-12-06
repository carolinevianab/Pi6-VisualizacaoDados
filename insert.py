import os, csv
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_URL'])
db = client.data

n_pokemons = 0
with open('pokemonData.csv', newline='') as data:
    #lê os headers do csv
    reader = csv.DictReader(data)
    headers = reader.fieldnames

    #lê cada pokemon do csv, e insere no banco
    reader = csv.reader(data)
    for pokemon in reader:
        pokemon_dict = {} 
      
        pokemon_dict[headers[0]] = pokemon[0] #numero
        
        pokemon_dict[headers[1]] = pokemon[1] #nome

        if pokemon[2]: #se tiver
            pokemon_dict[headers[2]] = float(pokemon[2]) #HP

        if pokemon[3]: #se tiver
            pokemon_dict[headers[3]] = float(pokemon[3]) #Atk

        if pokemon[4]: #se tiver
            pokemon_dict[headers[4]] = float(pokemon[4]) #Def

        if pokemon[5]: #se tiver
            pokemon_dict["SpecialAtk"] = float(pokemon[5]) #S.Atk

        if pokemon[6]: #se tiver
            pokemon_dict["SpecialDef"] = float(pokemon[6]) #S.Def
        
        if pokemon[7]: #se tiver
            pokemon_dict[headers[7]] = float(pokemon[7]) #Speed

        habilidades = [] #lista de habilidades
        if pokemon[8]: #se tiver
            habilidades.append(pokemon[8]) #Ability1
        if pokemon[9]: #se tiver
            habilidades.append(pokemon[9]) #Ability2
        if pokemon[10]: #se tiver
            habilidades.append(pokemon[10]) #Ability3

        if habilidades: #se a lista tiver alguma habilidade
            pokemon_dict["Abilities"] = habilidades

        tipos = [] #lista de tipos
        if pokemon[11]: #se tiver
            tipos.append(pokemon[11].capitalize()) #Type1
        if pokemon[12]: #se tiver
            tipos.append(pokemon[12].capitalize()) #Type2

        if tipos: #se a lista tiver algum tipo
            pokemon_dict["Types"] = tipos
      
        db.pokemons.insert_one(pokemon_dict).inserted_id
        print(pokemon_dict[headers[1]], "Added.")
        n_pokemons += 1

print("\na total of", n_pokemons, "added.")