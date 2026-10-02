import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier

ddf = pd.read_csv('shop_cleaned.csv')

X = ddf[['GENERE', 'ETA', 'SPESA_ANNUA']]
Y = ddf['PREMIUM']

print("------------------------------RandomForrestClassifier-----------------------------")
model_2 = RandomForestClassifier()
model_2.fit(X, Y)

score_2 = model_2.score(X, Y)

prediction_2 = model_2.predict(X)

print("Lo score dell' algoritmo Decision è -> ", score_2)

print("La prediction dell' algoritmo è -> ", prediction_2)

print("------------------------------DecisionTreeClassifier-----------------------------")
model = DecisionTreeClassifier()
model.fit(X, Y)

score = model.score(X, Y)

prediction = model.predict(X)

print("Lo score dell' algoritmo Decision è -> ", score)

print("La prediction dell' algoritmo è -> ", prediction)

plt.bar(X.columns, model_2.feature_importances_)
plt.title("Cosa conta per l'IA?")
plt.show()

plot_tree(model, feature_names=X.columns, class_names=['NORMAL', 'PREMIUM'], filled=True)
plt.title("Cosa conta per l'IA?")
plt.show()

joblib.dump(model, 'model.pkl')
print("Primo file salvato con successo!✅")
joblib.dump(model_2, 'model2.pkl')
print("Secondo file salvato con successo!✅")






