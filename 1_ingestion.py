import pandas as pd
import numpy as np

def genera_dati_raw() -> pd.DataFrame:
    dati = {
        "ID": [7, 4, 9, 3, 7, 4],
        "GENERE": ["M", "Maschio", "f", "Femmina", "m", "F"],
        "ETA": [4, 4, np.nan, 9, np.nan, 2],
        "SPESA_ANNUA": [59, 76, 89, 51, 70, 99],
        "PREMIUM": [0, 1, 0, 0, 1, 1]
    }
    return pd.DataFrame(data=dati)

def salva_dataset(df: pd.DataFrame, percorso_file: str) -> None:
    df.to_csv(percorso_file, index=False)
    print("File creato con successo!")

if __name__ == '__main__':
    df_raw = genera_dati_raw()
    salva_dataset(df_raw, "shop_raw.csv")
