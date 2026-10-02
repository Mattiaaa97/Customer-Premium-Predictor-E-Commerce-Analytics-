import pandas as pd
import numpy as np

dati = {"ID" :  [7,4,9,3,7,4],
        "GENERE" : ["M", "Maschio", "f", "Femmina", "m","F"],
        "ETA" : [4, 4, np.nan, 9, np.nan, 2],
        "SPESA_ANNUA" : [59, 76, 89, 51, 70, 99],
        "PREMIUM" : [0, 1, 0, 0, 1, 1]
        }

df = pd.DataFrame(data=dati)
new = df.to_csv("shop_raw.csv")

print("File creato con successo!")