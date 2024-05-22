#!/usr/bin/env python
# coding: utf-8

# In[1]:


# fonction “computeSurfaceM2”
def computeSurfaceM2(length, width):
    surface = length * width
    return f"Votre surface est de {surface} m2"
m = computeSurfaceM2(12,45)
m


# In[2]:


# onction “myPutStr”
def myPutStr(value):
    if isinstance(value, int):
        return "Et pourquoi pas 42 ?"
    else:
        return str(value)
z = myPutStr(12)
z


# In[2]:


import tkinter as tk
from time import strftime
 
def update_time():
    # Obtenir l'heure actuelle
    current_time = strftime('%H:%M:%S')
    # Mettre à jour le texte de l'étiquette
    time_label.config(text=current_time)
    # Planifier l'appel de cette fonction après 1000 ms (1 seconde)
    time_label.after(1000, update_time)
 
# Créer la fenêtre principale
root = tk.Tk()
root.title("Horloge Numérique")
 
# Créer une étiquette pour afficher l'heure
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
time_label.pack(anchor='center')
 
# Appeler la fonction update_time pour la première fois
update_time()
 
# Démarrer la boucle principale de l'interface graphique
root.mainloop()
 


# In[ ]:


#

def is_palindrome(string):
    return string == string[::-1]


# In[1]:


#
def validMyInternationalPhone(phone_number, country_code):
    if country_code == "FR":
        # Vérifiez le format du numéro français
        return len(phone_number) == 10 and phone_number.startswith("0")
    elif country_code == "US":
        # Vérifiez le format du numéro américain
        return len(phone_number) == 10 and phone_number.isdigit()
    else:
        return False


# In[ ]:


#

def fibonacci(limit):
    fib_sequence = [1, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


# In[ ]:





# In[2]:





# In[ ]:




