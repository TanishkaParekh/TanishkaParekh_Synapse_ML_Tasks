from itertools import *

Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}
k = int(input("Enter number of Pokemons you can use "))
# what we do :
#IITERATION 1
"""
    1)  make combinations of k pokemons  
    2)  make set of their powers  // so that no pwer is repeated
    3)  check the set with maximum power and that is our strongest pokemon team 
"""
#ITTERATION 2 using greedy algorithm for optimisation 
"""
    1)  we choose the best pokemon , add it to a list and count & store its powers into a set 
    2)  we will iterate through the list again to find another pokemon that will add maximum number of unique powers and add those into the set as well ( x this process will be done k-1 times
"""
dream_team = []
total_powers = set()
#number of pokemon to be selected
for i in range(k):
    best_pokemon = ""
    num_powers = 0
    
    #checking for the best pokemon
    for pokemon,powers in Pokedex.items():
        if pokemon in dream_team:
            continue
        poke_pwr = len(set(powers) - total_powers)
        if num_powers < poke_pwr:
            num_powers = poke_pwr
            best_pokemon = pokemon
            
    #adding it to our team
    dream_team.append(best_pokemon)
    total_powers.update(Pokedex[best_pokemon])
print(f"The one of the strongest team of {k} pokemons have {len(total_powers)} powers")
print(f"Optimised Team for best performance : {dream_team}")




