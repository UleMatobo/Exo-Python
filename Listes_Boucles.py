#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exo 1 
# Création des tables de multiplication
tables = {
    1: [i * 1 for i in range(1, 11)],
    2: [i * 2 for i in range(1, 11)],
    3: [i * 3 for i in range(1, 11)],
    5: [i * 5 for i in range(1, 11)],
    8: [i * 8 for i in range(1, 11)]
}

# Affichage des tables
for table, values in tables.items():
    print(f"Table de {table}: {values}")


# In[2]:


# Exo 2
# Utilisation d'une boucle for pour la table de 5
table_5_strings = []
for i in range(1, 11):
    table_5_strings.append(f"5 x {i} = {5 * i}")

print("\n".join(table_5_strings))


# In[3]:


# Exo 3
# Utilisation d'une boucle while infinie pour la table de 5
i = 1
while True:
    print(f"5 x {i} = {5 * i}")
    i += 1
    if i > 10:
        break


# In[4]:


# Exo 4
# Manipulation d'un dictionnaire avec opérations spécifiques
data = {"a": 42, "b": 42, "c": 42, "d": 42}
result = 1
for key, value in data.items():
    if key == 'd':
        result -= 42
    else:
        result *= value

print(result)  # Output: 74046


# In[15]:


# Exo 8

for i in range(11):
    print("1" * i)


# In[11]:


# Exo 6
# Implémentation du tri à bulle
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemple d'utilisation
numbers = [5, 4, 3, 2, 1]
bubble_sort(numbers)
print(numbers)  # Output: [1, 2, 3, 4, 5]


# In[12]:


# Exo 7
# Génération d'une liste d'années de 1980 à aujourd'hui
import datetime

current_year = datetime.datetime.now().year
years_list = list(range(1980, current_year + 1))
print(years_list)


# In[13]:


# EXO 5

for i in range(5):
    print("*" * (i + 1), end=" ")
print()


# In[10]:


for i in range(11):
    spaces = " " * (10 - i)
    ones = "[" * i
    
    spaces1 = " " * (10 - i)
    ones1 = "]" * i
    print(spaces + ones + " " + ones1 + spaces1)


# In[ ]:




