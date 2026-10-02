import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier

def carica_features_target(percorso_file: str):
    df = pd.read_csv(percorso_file)
    X = df[['GENERE', 'ETA', 'SPESA_ANNUA']]
    Y = df['PREMIUM']
    return X, Y

def esegui_random_forest(X: pd.DataFrame, Y: pd.Series) -> RandomForestClassifier:
    print("------------------------------RandomForrestClassifier-----------------------------")
    modello = RandomForestClassifier()
    modello.fit(X, Y)
    score = modello.score(X, Y)
    predizioni = modello.predict(X)
    print("Lo score dell' algoritmo Random Forest è -> ", score)
    print("La prediction dell' algoritmo è -> ", predizioni)
    return modello

def esegui_decision_tree(X: pd.DataFrame, Y: pd.Series) -> DecisionTreeClassifier:
    print("------------------------------DecisionTreeClassifier-----------------------------")
    modello = DecisionTreeClassifier()
    modello.fit(X, Y)
    score = modello.score(X, Y)
    predizioni = modello.predict(X)
    print("Lo score dell' algoritmo Decision è -> ", score)
    print("La prediction dell' algoritmo è -> ", predizioni)
    return modello

def mostra_grafici(modello_rf: RandomForestClassifier, modello_dt: DecisionTreeClassifier, X: pd.DataFrame) -> None:
    plt.bar(X.columns, modello_rf.feature_importances_)
    plt.title("Cosa conta per l'IA?")
    plt.show()

    plot_tree(modello_dt, feature_names=X.columns, class_names=['NORMAL', 'PREMIUM'], filled=True)
    plt.title("Cosa conta per l'IA?")
    plt.show()

def salva_modelli(modello_dt: DecisionTreeClassifier, modello_rf: RandomForestClassifier) -> None:
    joblib.dump(modello_dt, 'model.pkl')
    print("Primo file salvato con successo!✅")
    joblib.dump(modello_rf, 'model2.pkl')
    print("Secondo file salvato con successo!✅")

if __name__ == '__main__':
    X, Y = carica_features_target('shop_cleaned.csv')
    modello_rf = esegui_random_forest(X, Y)
    modello_dt = esegui_decision_tree(X, Y)
    mostra_grafici(modello_rf, modello_dt, X)
    salva_modelli(modello_dt, modello_rf)






