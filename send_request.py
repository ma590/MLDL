# Exemple d'envoi d'une requête POST depuis PyCharm
import requests
import numpy as np

# Définir l'URL de l'endpoint POST de votre application Flask
url = "http://localhost:5000/predict"

# Définir les données à envoyer dans la requête POST
data = {"data": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}

#data = np.genfromtxt('AMZN.csv', delimiter=',', names=True)
#tableau= data["Close"]
# Remplacez ces données par vos propres valeurs temporelles ou autres données nécessaires.

# Effectuer la requête POST
response = requests.post(url, json=data)
print("Contenu de la réponse :", response.text)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    # Afficher la réponse telle quelle (peut être du texte, JSON, etc.)
    print("Réponse:", response.text)
else:
    print("La requête n'a pas réussi.")
