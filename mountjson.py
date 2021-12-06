import os
import json
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_URL'])
db = client.data

top_n = 5
types = ["Geral", "Fire", "Water", "Ground", "Poison", "Fairy", "Normal", "Dragon", "Psychic", "Fighting", "Ghost", "Flying", "Rock", "Dark", "Electric", "Ice", "Bug", "Steel", "Grass"]

def top5poke(type):
  if type == "Geral":
    match = {"$match": {
      "HP": {"$gte": 0},
      "Atk": {"$gte": 0},
      "Def": {"$gte": 0},
      "Speed": {"$gte": 0}
    }}
  else:
    match = {"$match": {
      "Types": {"$in": [type]},
      "HP": {"$gte": 0},
      "Atk": {"$gte": 0},
      "Def": {"$gte": 0},
      "Speed": {"$gte": 0}
    }}

  project = {"$project": {
    "Name": "$Name",
    "Overall": {"$sum": ["$HP", "$Atk", "$Def", "$Speed"]},
    "HP": "$HP",
    "Atk": "$Atk",
    "Def": "$Def",
    "Speed": "$Speed",
    "SpecialAtk": "$SpecialAtk",
    "SpecialDef": "$SpecialDef"
  }}

  sort = {"$sort": {
    "Overall": -1
  }}

  limit = {"$limit": top_n}

  pipeline = [match, project, sort, limit]

  for pokemon in db.pokemons.aggregate(pipeline):
    infos["Top5Poke"][type].append({
      "Name": dict(pokemon)["Name"],
      "Overall": dict(pokemon)["Overall"],
      "HP": dict(pokemon)["HP"],
      "Atk": dict(pokemon)["Atk"],
      "Def": dict(pokemon)["Def"],
      "Speed": dict(pokemon)["Speed"],
      "SpecialAtk": dict(pokemon)["SpecialAtk"],
      "SpecialDef": dict(pokemon)["SpecialDef"]
    })  

def top5vida(type):
  if type == "Geral":
    match = {"$match": {
      "HP": {"$gte": 0}
    }}
  else:
    match = {"$match": {
      "Types": {"$in": [type]},
      "HP": {"$gte": 0}
    }}

  sort = {"$sort": {
    "HP": -1
  }}

  limit = {"$limit": top_n}
  
  pipeline = [match, sort, limit]

  for pokemon in db.pokemons.aggregate(pipeline):
    #print(pokemon, "\n")
    infos["Top5Vida"][type].append({
      "Name": dict(pokemon)["Name"],
      "HP": dict(pokemon)["HP"],
      "Atk": dict(pokemon)["Atk"],
      "Def": dict(pokemon)["Def"],
      "Speed": dict(pokemon)["Speed"],
      "SpecialAtk": dict(pokemon)["SpecialAtk"],
      "SpecialDef": dict(pokemon)["SpecialDef"]
    })

def top5ataque(type):
  if type == "Geral":
    match = {"$match": {
      "Atk": {"$gte": 0}
    }}
  else:
    match = {"$match": {
      "Types": {"$in": [type]},
      "Atk": {"$gte": 0}
    }}

  sort = {"$sort": {
    "Atk": -1
  }}

  limit = {"$limit": top_n}
  
  pipeline = [match, sort, limit]  

  for pokemon in db.pokemons.aggregate(pipeline):
    #print(pokemon, "\n")
    infos["Top5Ataque"][type].append({
      "Name": dict(pokemon)["Name"],
      "HP": dict(pokemon)["HP"],
      "Atk": dict(pokemon)["Atk"],
      "Def": dict(pokemon)["Def"],
      "Speed": dict(pokemon)["Speed"],
      "SpecialAtk": dict(pokemon)["SpecialAtk"],
      "SpecialDef": dict(pokemon)["SpecialDef"]
    })

def top5defesa(type):
  if type == "Geral":
    match = {"$match": {
      "Def": {"$gte": 0}
    }}
  else:
    match = {"$match": {
      "Types": {"$in": [type]},
      "Def": {"$gte": 0}
    }}
  
  sort = {"$sort": {
    "Def": -1
  }}

  limit = {"$limit": top_n}
  
  pipeline = [match, sort, limit]

  for pokemon in db.pokemons.aggregate(pipeline):
    #print(pokemon, "\n")
    infos["Top5Defesa"][type].append({
      "Name": dict(pokemon)["Name"],
      "HP": dict(pokemon)["HP"],
      "Atk": dict(pokemon)["Atk"],
      "Def": dict(pokemon)["Def"],
      "Speed": dict(pokemon)["Speed"],
      "SpecialAtk": dict(pokemon)["SpecialAtk"],
      "SpecialDef": dict(pokemon)["SpecialDef"]
    })

def top5speed(type):
  if type == "Geral":
    match = {"$match": {
      "Speed": {"$gte": 0}
    }}
  else:
    match = {"$match": {
      "Types": {"$in": [type]},
      "Speed": {"$gte": 0}
    }}

  sort = {"$sort": {
    "Speed": -1
  }}

  limit = {"$limit": top_n}
  
  pipeline = [match, sort, limit]

  for pokemon in db.pokemons.aggregate(pipeline):
    #print(pokemon, "\n")
    infos["Top5Speed"][type].append({
      "Name": dict(pokemon)["Name"],
      "HP": dict(pokemon)["HP"],
      "Atk": dict(pokemon)["Atk"],
      "Def": dict(pokemon)["Def"],
      "Speed": dict(pokemon)["Speed"],
      "SpecialAtk": dict(pokemon)["SpecialAtk"],
      "SpecialDef": dict(pokemon)["SpecialDef"]
    })

infos = {
  "QtdPorTipo": [],
  "Top5Poke": {
    "Geral": [],
    "Fire": [],
    "Water": [],
    "Ground": [],
    "Poison": [],
    "Fairy": [],
    "Normal": [],
    "Dragon": [],
    "Psychic": [],
    "Fighting": [],
    "Ghost": [],
    "Flying": [],
    "Rock": [],
    "Dark": [],
    "Electric": [],
    "Ice": [],
    "Bug": [],
    "Steel": [],
    "Grass": []
  },
  "Top5Vida": {
    "Geral": [],
    "Fire": [],
    "Water": [],
    "Ground": [],
    "Poison": [],
    "Fairy": [],
    "Normal": [],
    "Dragon": [],
    "Psychic": [],
    "Fighting": [],
    "Ghost": [],
    "Flying": [],
    "Rock": [],
    "Dark": [],
    "Electric": [],
    "Ice": [],
    "Bug": [],
    "Steel": [],
    "Grass": []
  },
  "Top5Ataque": {
    "Geral": [],
    "Fire": [],
    "Water": [],
    "Ground": [],
    "Poison": [],
    "Fairy": [],
    "Normal": [],
    "Dragon": [],
    "Psychic": [],
    "Fighting": [],
    "Ghost": [],
    "Flying": [],
    "Rock": [],
    "Dark": [],
    "Electric": [],
    "Ice": [],
    "Bug": [],
    "Steel": [],
    "Grass": []
  },
  "Top5Defesa": {
    "Geral": [],
    "Fire": [],
    "Water": [],
    "Ground": [],
    "Poison": [],
    "Fairy": [],
    "Normal": [],
    "Dragon": [],
    "Psychic": [],
    "Fighting": [],
    "Ghost": [],
    "Flying": [],
    "Rock": [],
    "Dark": [],
    "Electric": [],
    "Ice": [],
    "Bug": [],
    "Steel": [],
    "Grass": []
  },
  "Top5Speed": {
    "Geral": [],
    "Fire": [],
    "Water": [],
    "Ground": [],
    "Poison": [],
    "Fairy": [],
    "Normal": [],
    "Dragon": [],
    "Psychic": [],
    "Fighting": [],
    "Ghost": [],
    "Flying": [],
    "Rock": [],
    "Dark": [],
    "Electric": [],
    "Ice": [],
    "Bug": [],
    "Steel": [],
    "Grass": []
  }
}

##--- QtdPorTipo ---
unwind = {"$unwind": "$Types"}

group = {"$group": {
  "_id": "$Types", 
  "count": {"$sum": 1}
}}

pipeline = [unwind, group]

for pokemon in db.pokemons.aggregate(pipeline):
  #print(pokemon, "\n")
  infos["QtdPorTipo"].append({
    "Type": dict(pokemon)["_id"],
    "Count": dict(pokemon)["count"]
  })

##Os outros
for type in types:
  top5poke(type)   ##Top5Poke
  top5vida(type)   ##Top5Vida
  top5ataque(type) ##Top5Ataque
  top5defesa(type) ##Top5Defesa
  top5speed(type)  ##Top5Speed

with open('data.json', 'w') as json_file:
  json.dump(infos, json_file, indent = 2)