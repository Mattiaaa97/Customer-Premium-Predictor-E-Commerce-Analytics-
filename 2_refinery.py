import pandas as pd

def carica_dataset(percorso_file: str) -> pd.DataFrame:
    return pd.read_csv(percorso_file)

def pulisci_dati(df: pd.DataFrame) -> pd.DataFrame:
    df_pulito = df.copy()
    mappa_genere = {'Maschio': 'M', 'm': 'M', 'Femmina': 'F', 'f': 'F'}
    df_pulito['GENERE'] = df_pulito['GENERE'].replace(mappa_genere)
    df_pulito['ETA'] = df_pulito['ETA'].fillna(df_pulito['ETA'].median())
    df_pulito['GENERE'] = df_pulito['GENERE'].astype('category').cat.codes
    return df_pulito

def salva_dataset_pulito(df: pd.DataFrame, percorso_file: str) -> None:
    df.to_csv(percorso_file, index=False)
    print("File creato con successo")

if __name__ == '__main__':
    df_grezzo = carica_dataset("shop_raw.csv")
    df_raffinato = pulisci_dati(df_grezzo)
    salva_dataset_pulito(df_raffinato, "shop_cleaned.csv")
