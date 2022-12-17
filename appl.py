import os 
import json

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

for letter in letters:
    try:
        os.mkdir(letter)
    except FileExistsError:
        pass

with open("thing.json", "r") as file:
    dict = json.load(file)
    
for name in dict:
    first = name[0]
    
    for letter in letters:
        if first == letter:
            with open(f"{letter}/{name}", "w") as file:
                file.write(str(dict[name]))