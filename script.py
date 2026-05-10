import pandas as pd
import json

# Extraire

with open("donnees.json") as donnee:
    data = json.load(donnee)
    df = pd.DataFrame(data)
    
    
# Transformer

df["engagement"] = df["likes"] + df["commentaires"]

# Charger

df.to_csv("donnees_propres.csv", index=False)
print("L'operation est un succes !")
