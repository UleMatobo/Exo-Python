#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Script d'entrée en boîte de nuit :

# Demander l'âge à l'utilisateur
age = int(input("Quel est votre âge ? "))

# Vérification de l'âge
if age >= 18 and age < 42:
    print(f"Vous pouvez entrer, vous êtes majeur et avez {age} ans.")
elif age >= 42:
    print("Vous êtes maintenant le patron de la boîte de nuit.")
else:
    print(f"Vous ne pouvez pas entrer, vous n'êtes pas majeur et avez {age} ans.")
    


# In[ ]:


# Algorithme de retour de température en fonction d'un nombre aléatoire :
import random

# Générer un nombre aléatoire entre 0 et 30
rand = random.randint(0, 30)

# Utiliser une condition pour retourner le message en fonction de la valeur de rand
if 0 <= rand <= 10:
    print("Cool")
elif 11 <= rand <= 20:
    print("Tepid")
elif 21 <= rand <= 30:
    print("Warm")


# In[6]:


import datetime

# Obtenir le jour de la semaine actuel avec datetime
jour = datetime.datetime.today().strftime("%A")

# Utiliser des conditions pour afficher le message correspondant au jour de la semaine
if   jour == "Monday":
    print("Nous sommes lundi.")
elif jour == "Tuesday":
    print("Nous sommes mardi.")
elif jour == "Wednesday":
    print("Nous sommes mercredi.")
elif jour == "Thursday":
    print("Nous sommes jeudi.")
elif jour == "Friday":
    print("Nous sommes vendredi.")
elif jour == "Saturday":
    print("Nous sommes samedi.")
elif jour == "Sunday":
    print("Nous sommes dimanche.")
else:
    print("Jour non reconnu.")


# In[ ]:


# Condition ternaire pour vérifier si une variable existe :
# Demander à l'utilisateur de commencer l'histoire
print("Bienvenue dans cette aventure !")
reponse1 = input("Vous trouvez une clé sur le sol, que faites-vous ? (saisissez 'prendre' ou 'ignorer') ")

# Conditions imbriquées basées sur la réponse de l'utilisateur
if reponse1.lower() == "prendre":
    reponse2 = input("Vous ouvrez une porte avec la clé et entrez dans une pièce sombre. 
                     Allumez-vous une torche ? (saisissez 'oui' ou 'non') ")
    if reponse2.lower() == "oui":
        print("Vous découvrez un trésor caché ! La grande réponse sur la vie, l'univers et le reste !")
    else:
        print("Vous vous perdez dans l'obscurité...")
else:
    print("Vous continuez votre chemin sans la clé.")


# In[ ]:


# Calcul du prix d'un article après remise :
# Vérifier si une variable existe et afficher un message en conséquence
resultat = "42" if "ma_variable" in locals() else "Cette variable n'existe pas"
print(resultat)


# In[ ]:



# Demander le prix initial de l'article et le pourcentage de remise à l'utilisateur
prix_initial = float(input("Entrez le prix initial de l'article : "))
remise_percent = float(input("Entrez le pourcentage de remise : "))

# Calculer le montant de la remise et le prix final après remise
montant_remise = prix_initial * (remise_percent / 100)
prix_final = prix_initial - montant_remise

# Vérifier si le prix final est supérieur à la moitié du prix initial
if prix_final > prix_initial / 2:
    print(f"Le prix final après remise est : {prix_final:.2f} €")
else:
    print("Désolé, la remise est trop élevée.")


# In[ ]:


#Vérification si un nombre saisi par l'utilisateur est pair ou impair :
# Demander à l'utilisateur d'entrer un nombre entier
nombre = int(input("Entrez un nombre entier : "))

# Vérifier si le nombre est pair ou impair
if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre n'est pas pair.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




