import os
import json
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_URL'])
db = client.data

#Quantidade de pokemons por tipo
"""
unwind = {"$unwind": "$Types"}

group = {"$group": {
  "_id": "$Types", 
  "Count": {"$sum": 1}
}}

pipeline = [unwind, group]
"""

#Quantidade de pokemons com dois tipos
"""
project = {"$project": {
  "Name": "$Name",
  "Num types": {"$size": "$Types"}
}}

group = {"$group": {
  "_id": "$Num types",
  "count": {"$sum": 1}
}}

sort = {"$sort": {
  "_id": -1
}}

limit = {"$limit": 1}

pipeline = [project, group, sort, limit]
"""

#Top 5 pokemons com mais vida
"""
sort = {"$sort": {
  "HP": -1
}}

limit = {"$limit": 5}
 
pipeline = [sort, limit]
"""

#Top 5 pokemons com maior ataque
"""
sort = {"$sort": {
  "Atk": -1
}}

limit = {"$limit": 5}
 
pipeline = [sort, limit]
"""

#Top 5 pokemons com maior defesa
"""
sort = {"$sort": {
  "Def": -1
}}

limit = {"$limit": 5}
 
pipeline = [sort, limit]
"""

#Top 5 pokemons mais rapidos
"""
sort = {"$sort": {
  "Speed": -1
}}

limit = {"$limit": 5}
 
pipeline = [sort, limit]
"""

#Media de pesos por tipo
"""
unwind = {"$unwind": "$Types"}

group = {"$group": {
  "_id": "$Types",
  "Average weight (kg)": {"$avg": "$Weight(kg)"},
  "Average weight (lb)": {"$avg": "$Weight(lb)"}
}}

pipeline = [unwind, group]
"""

#Top(20?) melhores pokemons por tipo(sum -> vida, ataque, defesa e velocidade)
"""
project = {"$project": {
  "Name": "$Name",
  "Overall": {"$sum": ["$HP", "$Atk", "$Def", "$Speed"]}
}}

sort = {"$sort": {
  "Overall": -1
}}

limit = {"$limit": 20}

pipeline = [project, sort, limit]
"""

#for pokemon in db.pokemons.aggregate(pipeline):
#  print(pokemon, "\n")


### tests ###

top_n = 5

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
    print(pokemon, "\n")

top5poke("Geral")