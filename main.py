import pandas as pd

pokeData = pd.read_json('pokemons_stats.json')

## -- Tratando os números -- ##
# Tirando o # e colocando None em valores invalidos
pokeData['Num'] = pokeData['Num'].str.replace('\r\n\t\t', '')
pokeData['Num'] = pokeData['Num'].str.replace('#', '')
pokeData['Num'] = pokeData['Num'].replace('TBD', None)
# Transformando em Int
pokeData['Num'] = pokeData['Num'].astype(int)

pokeData['Type1'] = pokeData['Type1'].str.replace('/pokemon/type/', '')
pokeData['Type2'] = pokeData['Type2'].str.replace('/pokemon/type/', '')

columnNames = ['Number', 'Name', 'HP','Atk','Def','S.Atk','S.Def', "Speed", "Ability1", "Ability2", "Ability3", 'Type1', 'Type2']

pokeData.columns = columnNames

pokeData.sort_values(by='Number', inplace=True)
pokeData.set_index('Number', inplace=True)

pokeData.to_csv('pokemonData.csv')

a = pd.read_csv('pokemonData.csv')
print(a)