# 🛒 Previsione Clienti Premium (Shop Analysis)

Progetto in Python per gestire i dati di acquisto dei clienti, pulire le informazioni e allenare due modelli di Machine Learning per capire chi acquisterà il piano Premium.

---

## 📌 Cosa fa il progetto

- Crea un primo elenco con informazioni sui clienti (genere, età, spesa e status Premium)
- Sistema i dati grezzi correggendo i testi diversi (M, Maschio, F, Femmina) e riempiendo le età mancanti
- Trasforma le categorie in numeri per renderle leggibili dagli algoritmi
- Addestra due modelli di Intelligenza Artificiale: un Albero Decisionale e una Random Forest
- Mostra con dei grafici quali caratteristiche contano di più nella scelta del cliente
- Salva i due modelli pronti all'uso in formato .pkl

---

## 📁 I tre file

* 1_ingestion.py: genera la tabella iniziale con i dati grezzi e la salva in shop_raw.csv
* 2_refinery.py: pulisce i valori del genere, aggiunge l'età mancante con la mediana e crea shop_cleaned.csv
* 3_brain.py: allena i due modelli di classificazione, mostra i grafici a barre e salva i modelli model.pkl e model2.pkl

---

## ⚙️️ Come si usa

1. Installa i pacchetti necessari:
pip install pandas numpy scikit-learn matplotlib joblib

2. Esegui i file nell'ordine corretto:
python 1_ingestion.py
python 2_refinery.py
python 3_brain.py

---

Autore: Mattia Dellanoce
