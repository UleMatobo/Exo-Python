#!/usr/bin/env python
# coding: utf-8

# In[23]:


'My Python Code every day'


# In[1]:


# Déclaration de variables de différents types
my_integer = 42
my_float = 42.0
my_string = "quarante-deux"
my_boolean = True
my_list = [4, 2]
my_tuple = (4, 2)
my_set = {4, 2}
my_dict = {"a": 4, "b": 2}


# In[26]:


# Nombre de caractères dans la variable my_string
my42count = "quarante-deux"
my_string_length = len(my42count)


# In[32]:


# Vérification de l'existence d'une variable et affectation conditionnelle
my_existe_variable = my_integer if 'my_integer' in locals() else 42


# In[30]:


# Création d'un tableau (list) avec une lettre par index
myArray42 = ['q', 'u', 'a', 'r', 'a', 'n', 't', 'e', 'd', 'e', 'u', 'x']


# In[7]:


# Nombre d'éléments dans myArray42
myArray42Len = len(myArray42)


# In[18]:


# Recomposition du mot dans une variable de type string et concaténation avec une phrase
my_recomposed_string = ''.join(myArray42) + " La grande réponse sur la vie, l'univers et le reste !"

print(my_recomposed_string)


# In[12]:


# Génération d'un nombre aléatoire entre 1 et 42, et vérification s'il est égal à 42
import random
rand = random.randint(1, 42)


is_equal_to_42 = (rand == 42)


# In[40]:


# Détection des types de variables
#my42Type = type(my_integer).__name__  # Retourne le nom du type de la variable (ex: "int" pour un entier)
my42Type=print(type(my_boolean).__name__)


# In[19]:


# Multiplication donnant 42 puis conversion en string
compute42 = 6 * 7
compute42_str = str(compute42)


# In[20]:


# Remplacement des occurrences de "42" dans une chaîne de caractères
my_string_with_numbers = "42424242"
my_string_replaced = my_string_with_numbers.replace("42", "quarante-deux ")


# In[34]:


# Échange de valeurs entre deux variables
a = 24
b = 42
a, b = b, a  # Transfert de la valeur de a vers b et de b vers a


# In[35]:


# Affichage des résultats
print("my_integer:", my_integer)
print("my_float:", my_float)
print("my_string:", my_string)
print("my_boolean:", my_boolean)
print("my_list:", my_list)
print("my_tuple:", my_tuple)
print("my_set:", my_set)
print("my_dict:", my_dict)
print("my_string_length:", my_string_length)
print("my_existe_variable:", my_existe_variable)
print("myArray42:", myArray42)
print("myArray42Len:", myArray42Len)
print("my_recomposed_string:", my_recomposed_string)
print("rand:", rand)
print("is_equal_to_42:", is_equal_to_42)
print("my42Type:", my42Type)
print("compute42_str:", compute42_str)
print("my_string_replaced:", my_string_replaced)
print("a:", a, "b:", b)


# In[ ]:




