#!/usr/bin/env python
# coding: utf-8

# rick vanel, njike ngassam, Groupe b
# 
# <eventuelles autres personnes ayant travaillé avec vous>
# 
# # DM d'Algorithmie
# 
# Bonjour, 
# 
# Ce Devoir Maison d'algorithmie sera noté et comptera pour moitié de la note de Contrôle Continu avec la note sur le projet de jeu textuel que vous aurez à réaliser.
# 
# ## Etape 1 : Renommer
# Dans un premier temps merci de renommer ce fichier comme suit :
# 
# DM_Algo_groupeX_prenom_nom
# 
# où X correspond à la lettre de votre groupe à savoir A, B ou C.
# 
# Pour cela soit vous modifier directement le nom du fichier dans l'explorateur de fichier soit vous allez sur File>Rename.
# 
# ## Etape 2 : Ajouter Prenom Nom au début de la feuille
# 
# Remplacer le "prenom, nom, Groupe X" écrit en haut de cette cellule.
# 
# ex : Vincent, Reynaert, Groupe P
# 
# Pour cela double cliquez sur la cellule. Une fois la modification apportée l'appliquer en appuyant sur le bouton Exécuter ou avec le raccourci clavier Ctrl+Enter
# 
# ## Etape 3 : Répondre aux QCM
# 
# Pour répondre aux QCM merci de suivre la méthode suivante :
# 
# * Pour répondre à ce QCM il faudra afficher la/les réponses via un print. ex Si la réponse est A,B et D alors il faudra écrire **print("ABD")**
# * A chaque cellule Markdown de question correspond une cellule python de réponse où il sera indiqué en commentaire le numéro de la question correspondante.
# 
# Vous pourrez également vous référer à l'exemple Question 0.
# 
# Le non-respect de ces directives **entraîne un malus** sur la note finale.
# 
# __Un QCM est un questionnaire à CHOIX MULTIPLES__ Plusieurs réponses sont donc parfois possible !
# * Une question peut avoir **une ou plusieurs**réponses. 
# * Une réponse fausse, l’absence de réponse et la sélection d’une réponse fausse avec une réponse bonne vaudront **0 point** pour la question associée. 
# * Une réponse partielle à la question (ex : donner une seule réponse lorsque plusieurs sont attendue) vaudra **le pourcentage de points associés** à cette réponse (ex : bonne réponse est ABC, vous répondez A, vous aurez ⅓ de point sur cette question).
# * Si toutes les réponses sont sélectionnées pour une question **des points négatifs** seront comptabilisés.
# 
# ## Etape 4 : Réponde aux questions ouvertes de code Python
# 
# __Lisez attentivement la consigne pour chacune de ces questions !__
# 
# ## Etape 5 : Rendu du DM
# 
# Le rendu attendu est ce fichier que vous aurez modifié en suivant les consignes ci-dessus.
# 
# Il devra être déposé sur le disk partagé L1A,B ou C dépendamment de votre groupe.
# 
# ## ATTENTION
# 
# Merci de ne pas tricher en recopiant bêtement le fichier du collègue. **Un malus sera appliqué aux deux rendus jugé trop proches/identiques.**
# 
# Merci également dans le cas où vous auriez travaillé ce DM par binôme ou trinôme de le préciser en haut de cette cellule en indiquant le prénom et nom et groupe de la/les personne.s avec qui vous avez collaboré. Cependant le rendu reste individuel et on évite donc les copier coller avec les mêmes erreurs que ses camarades.
# 
# ## NB 1
# 
# Si certaines notions de ce DM n'ont pas encore été abordée en cours (dépendamment de votre groupe nous sommes plus ou moins avancés) merci de le préciser dans un commentaire (utilisez #), mais d'essayer tout de même de répondre à la question en se référant aux slides du cours (ou toutes autres resources en ligne) :  https://docs.google.com/presentation/d/193qqeLBneT02sMBcREZZjqO2LFeL0fK6PC94U5s-EI4/edit?usp=sharing
# 
# ### NB 2
# 
# La cellule que j'ai utilisé ici est de type Markdown. Il s'agit d'un langage balisé comme le HTML. Ce n'est pas un langage de programmation et donc il ne s'agit pas de code informatique.
# 
# Aussi le Markdown possède une syntaxe particulière comme vous le remarquerez probablement lorsque vous double-cliquerez sur la cellule pour la modifier.
# 
# #### Astuce
# 
# N'oubliez pas que vous êtes dans un éditeur de code...
# 
# ### NB 3
# 
# Bon courage pour ce DM

# ## QCM

# ### Question 0
# Parmis les affirmations suivantes la/lesquelle.s est/sont vraie.s ?
# * A. Toujours donner la même réponse à un QCM est forcément un bon choix.
# * B. Lire les consignes ne sert à rien et fait perdre du temps autant y aller directement.
# * C. Pour répondre à ce QCM il faudra afficher la/les réponses via un print.
# * D. A chaque cellule Markdown de question correspond une cellule python de réponse où il sera indiqué en commentaire le numéro de la question correspondante.

# In[1]:


#Réponse 0
print("CD")


# ### Question 1
# Un algorithme c'est :
# * A. un programme informatique.
# * B. une suite d'instructions et d’opérations sans ordre précis permettant de résoudre certains problèmes ou d’effectuer certaines actions.
# * C. une recette de cuisine.
# * D. une suite finie et non ambiguë d'instructions et d’opérations permettant de résoudre certains problèmes ou d’effectuer certaines actions.

# In[2]:


#Réponse 1
print("CD")


# ### Question 2
# Pour écrire un algorithme :
# * A. on peut utiliser une représentation graphique.
# * B. on doit l'écrire dans un langage informatique comme le Python.
# * C. on peut l'écrire en français grace à un pseudo langage.
# * D. on doit réfléchir aux procédures et aux décisions qui seront nécessaire pour le faire fonctionner.

# In[3]:


#Réponse 2
print("ACD")


# ### Question 3
# Soit l'algorithme suivant (si l'image ne s'affiche pas correctement merci de vous référer au fichier Algo_42.PNG disponible dans le dossier d'archive que je vous ai partagé) :
# 
# ![Diagram_42](Algo_42.png)
# 
# Parmis les affirmations suivantes la/lesquelle.s est/sont vraie.s :
# * A. Cet aLgorithme vérifie si un utilisateur sait que La réponse universelle est 42 et le félicite si c'est le cas.
# * B. Ce diagramme n'est pas un algorithme.
# * C. Cet algorithme va demander en boucle à l'utilisateur d'entrer un nombre jusqu'à ce qu'il le fasse.
# * D. Cet algorithme calcule une moyenne.

# In[12]:


#Réponse 3
print("AC")


# ### Question 4
# #### Variables
# Parmis les affirmations suivantes la/lesquelle.s est/sont vraie.s :
# * A. Point de vie est un nom de variable acceptable.
# * B. La définition d'une variable c'est qu'elle varie.
# * C. Une variable c'est une sorte de carton avec une étiquette qui permet de stocker de la donnée.
# * D. Une variable qui est de type booléen stockera la valeur Vrai ou la valeur Faux.

# In[5]:


#Réponse 4
print("BCD")


# ### Question 5
# #### Opérations
# Parmis les opérations (en python) suivantes la/lesquelle.s est/sont valide.s :
# * A. "le résultat est " + str(10+2^2*3)
# * B. 1/(3//5)
# * C. "le résultat est " + 42
# * D. "attention la division par zéro n'est pas valide" +str(42/(4-(2*2)))

# In[18]:


#Réponse 5
print("AD")


# ### Question 6
# #### Si, Sinon si, Sinon
# Soit le pseudo code suivant :
# ```
# pv_ennemi ← 5
# points_de_degats_joueur ← 6
# pv_ennemi ← pv_ennemi - points_de_degats_joueur
# Si pv_ennemi>0 alors
#     Afficher "L'ennemi n'est pas mort"
# Sinon Si pv_ennemi==0 alors
#     Afficher "L'ennemi est comateux"
# Sinon
#     Afficher "L'ennemi est mort"
# Fin Si
# ```
# Parmis les affirmations suivantes la/lesquelle.s est/sont vraie.s :
# * A. Cet algorithme va afficher une erreur 
# * B. Cet algorithme va afficher "L'ennemi n'est pas mort"
# * C. Cet algorithme va afficher "L'ennemi est comateux"
# * D. Cet algorithme va afficher "L'ennemi est mort"

# In[7]:


#Réponse 6
print("D")


# ### Question 7
# #### Boucles
# Soit la figure suivante (si elle ne s'affiche pas correctement merci de vous référer au fichier Demo_rosace.gif) :
# 
# ![rosace](Demo_rosace.gif)
# 
# Parmis les pseudocodes suivants le/lesquel.s permet.tent d'obtenir cette figure sans devoir écrire 150 lignes ou plus :
# * A. 
# ```
# Poser le crayon à la position (0,0)
# Dessiner cercle de rayon 8
# Tourner vers la gauche sur 360/30 degrés 
# Dessiner cercle de rayon 8
# Tourner vers la gauche sur 360/30 degrés
# Dessiner cercle de rayon 8
# Tourner vers la gauche sur 360/30 degrés
# Dessiner cercle de rayon 8
# ...
# ```
# * B.
# ```
# Poser le crayon à la position (0,0)
# compteur ← 30
# Tant que compteur > 0 faire
#     Dessiner cercle de rayon 8
#     Tourner vers la gauche sur 360/30 degrés 
#     compteur ← compteur - 1
# Fin Tant que
# ```
# * C.
# ```
# Poser le crayon à la position (0,0)
# Tant que Vrai faire
#     Dessiner cercle de rayon 8
#     Tourner vers la gauche sur 360/30 degrés 
# Fin Tant que
# ```
# * D.
# ```
# Poser le crayon à la position (0,0)
# Pour compteur allant de 0 à 30 faire
#     Dessiner cercle de rayon 8
#     Tourner vers la gauche sur 360/30 degrés 
# Fin Tant que
# ```

# In[8]:


#Réponse 7
print("BD")


# ### Question 8
# #### Fonctions
# Parmis les affirmations suivantes la/lesquelle.s est/sont vraie.s :
# * A. Une fonction prédéfinie pour Afficher du texte en console existe dans quasiment tous les langages de programmations récents. 
# * B. Une fonction est une portion de code informatique nommée, qui accomplit une tâche spécifique.
# * C. Il n'existe pas de fonctions prédéfinies, il faut impérativement toutes les réécrire.
# * D. Ecrire une fonction permet de réutiliser du code sans avoir à faire de copier coller dans tous les sens.

# In[9]:


#Réponse 8
print("ABD")


# ### Question 9
# Parmis les code python suivants le/lesquelle.s est/sont valide.s :
# * A.
# ```
# fonctionDeBase(#parametre):
#     return résultat
# print(fonctionDeBase("test"))
# ```
# * B.
# ```
# def fonctionDeBase():
#     pass
# print(fonctionDeBase())
# ```
# * C.
# ```
# def nomDeMaFonction(param):
#     param = param - 1
#     return param
# print(nomDeMaFonction("test"))
# ```
# * D.
# ```
# def nomDeMaFonction(param1,param2):
#     param1 = param1 + param2
#     return param1
# print(nomDeMaFonction("test",2))
# ```

# In[10]:


#Réponse 9
print("D")


# ### Question 10
# Parmis les affirmations suivantes la/lesquelle.s est/sont vraie.s :
# * A. Une liste ou un tableau est une structure de données qui permet de stocker plusieurs valeurs de même type comme des notes d'étudiants.  
# * B. Une liste et un tableau c'est exactement la même chose ça sert à stocker plusieurs valeurs de même type comme des notes d'étudiants.
# * C. Une liste et un tableau c'est complétement différent, il n'y a aucun rapport entre ces deux types de données.
# * D. Une liste peut stocker un nombre indéfini de données (normalement de même type) mais l'accès en mémoire est plus lent, le tableau quant à lui, ne peut stocker qu'un nombre fini de données de même type mais les rend plus rapidement accessible.

# In[11]:


#Réponse 10
print("A")


# ## Python
# Merci pour cette partie de suivre attentivement la consigne de chaque exercice. 
# 
# Merci également de ne pas laisser vos cellules de tests et de les supprimer avant de me rendre le fichier et de ne mettre que les fonctions ou bout de code demandés dans les cellules de réponse.
#  
# Les 5 premières questions seront 'simples' et ne vaudront qu'1 point chacune. 
# Une consigne qui ne sera pas suivi à la lettre rendra l'exercice invalide et vaudra donc 0.
# 
# L'exercice 6 étant potentiellement un peu plus compliqué pourra valoir jusqu'à 2 points. 
# 
# L'exercice 7 sera plus ouvert et pourra valoir jusqu'à 5 points et le pseudo code pourra y être accepté. (toutefois 0 points seront accordé si ce qui est écrit n'a aucun sens par rapport à la question posée)(n'oubliez pas que les commentaires existent)
# 
# L'exercice 8 laissez libre court à votre imagination et proposez moi un joli dessin fait en python (jusqu'à 3 points si c'est fait de façon smart): 
# * soit avec Turtle dont un exemple de code est disponible dans les programmes qui sont sur vos disques partagés sinon (cf.[https://realpython.com/beginners-guide-python-turtle/])
# * soit avec Tkinter (cf. [https://zetcode.com/tkinter/drawing/])
# * soit avec Pillow et Images (cf. [https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/])
# 
# # NB
# Comme vous pouvez le constater avec 10 points pour le QCM et 5+2+5+3=15 points pour les exercices, 5 points sont en bonus (qui pourront être reporté à un ratio de 50% sur la note du projet de jeu textuel, c'est à dire que si ce DM est réalisez à 100% vous pouvez obtenir jusqu'à 2.5 points d'avance sur le projet).

# ### Exercice 1
# Afficher le résultat suivant :
# ```
# Hello World !
# ```

# In[34]:


#Exercice 1
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>^
print("hello world")


# ### Exercice 2
# Afficher le résultat suivant en utilisant le moins de lignes de code possible (1-4 lignes) :
# ```
# Hello World 1
# Hello World 2
# Hello World 3
# Hello World 4
# Hello World 5
# Hello World 6
# Hello World 7
# Hello World 8
# Hello World 9
# Hello World 10
# Hello World 11
# ```

# In[30]:


#Exercice 2
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>
for i in range(1,12):
    print("hello world",i)


# ### Exercice 3
# Créez une fonction *milieu* qui prend en paramètre, deux nombres entiers correspondant au minimum et au maximimum d'un intervalle et qui (comme son nom l'indique si bien) calcule le milieu de l'intervalle. 
# 
# *ATTENTION* le résultat attendu doit être un nombre entier !
# 
# Astuce : on peut considérer que cette fonction calcule la moyenne entre minimum et maximum.
# 
# Exemple :
# ```
# print(milieu(4,6))
# print(milieu(0,500))
# print(milieu(1024,2048))
# ```
# affichera :
# ```
# 5
# 250
# 1536
# ```

# In[35]:


#Exercice 3
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>
def milieu(a,b):
    return (a+b)//2


# ### Exercice 4
# Traduisez cette algorithme écrit en pseudo langage vers du langage python :
# ```
# pv_ennemi ← 299
# degat_joueur ← 3
# Tant que pv_ennemi > 0 faire
#     Afficher pv_ennemi
#     pv_ennemi ← pv_ennemi - degat_joueur
# Afficher “l’ennemi est mort”
# ```

# In[36]:


#Exercice 4
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>
pv_ennemi = 299
degat_joueur = 3
while pv_ennemi > 0:
    print(pv_ennemi)
    pv_ennemi -= degat_joueur
print("l'ennemi est mort")


# ### Exercice 5
# Créez une fonction *mean* qui prend en paramètre, une liste de nombre de type float ou int  et qui (comme son nom l'indique si bien) calcule la moyenne de cette liste (comme on le ferait pour calculer la moyenne d'une classe) et retourne le résultat. 
# 
# *ATTENTION* le résultat attendu doit être un nombre à virgule (type float) !
# 
# Astuce : la fonction sum() calcule et retourne la somme des éléments d'une liste et la fonction len() retourne le nombre d'éléments présents dans la liste.
# 
# Exemple :
# ```
# maListe = [10,15,20,17]
# print(sum(maListe))
# print(len(maListe))
# print(mean(maListe))
# ```
# affichera :
# ```
# 62
# 4
# 15.5
# ```

# In[37]:


#Exercice 5
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>
def mean(top):
    return sum(top)/len(top)


# ### Exercice 6
# Traduisez cette algorithme présenté sous forme de diagramme vers du langage python :
# 
# ![Diagram_42](Algo_42.png)

# In[38]:


#Exercice 6
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>


# ### Exercice 7
# laissez libre court à votre imagination et proposez moi un joli dessin fait en python: 
# * soit avec Turtle dont un exemple de code est disponible dans les programmes qui sont sur vos disques partagés sinon (cf.[https://realpython.com/beginners-guide-python-turtle/])
# * soit avec Tkinter (cf. [https://zetcode.com/tkinter/drawing/])
# * soit avec Pillow et Images (cf. [https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/])

# In[114]:


#Exercice 7
#<écrivez votre code dans cette cellule juste en dessous de cette ligne>


# ### Exercice 8 
# #### problème ouvert
# En considérant le code suivant qui permet de récupérer une image et la convertir en niveau de gris et la stocker dans un tableau de tableau 64x64 (autrement appelé matrice) qui contient les données de chaque pixel (soit un nombre entier allant de 0 à 255 correspondant au niveau de gris où 0 = noir et 255 = blanc).
# 
# 
# ```
# %matplotlib inline
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# from PIL import Image
# 
# def convertImageToGrayArray(imgFile = "pixel_art_exemple_by_Mustachioed_Pizza.png"):
#     img = Image.open(imgFile).convert('L')
#     img.thumbnail((64, 64), Image.ANTIALIAS)
#     grayscale_array = np.asarray(img)
#     return grayscale_array
# ```
# 
# * écrivez une fonction qui, à partir de ce type de matrice, converti l'image en texte comme dans l'exemple suivant (il s'agit d'asciiArt):
# 
# Voici la liste de caractères utilisés pour convertir notre image en asciiart : 
# ```
# ['@@', '00', '##', 'xx', '**', '..', '--', '~~', '  ']
# ```
# Dans cette liste de charactère on considère que l'on va du noir vers le plus claire mais libre à vous de la changer (indice plus vous mettez de caractère par élément de votre liste plus votre image sera large
# ![babou](babouin.png)
# ```
# ..**..**********xxxxxxxxxxxxxxxxxxxxxxxx####xxxxxxxxxxxxxxxx##**xx********xxxx##xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx**xx**xx**....**..
# ....****..****xxxxxxxxxxxx####xxxx######xx########xxxx******xxxxxx******xx######xx########################xx##xxxxxx**xx**--....
# **....**..xx**xx##xx################################xxxx##xxxx##xxxx################0000########################xxxx****........
# ....**..******xxxx################000000000000##########################00########xx**....xx##00##############xxxx******....**--
# ..****....****xx##############0000xx********xx00####00##00####xx########xx**xx00xx~~--**--~~**00##xx########xxxx**..****........
# ..........****xx################00..~~**xx--~~xx##xx##0000############xx**xx0000**~~--xx--~~..00xx..xx##xxxxxxxx******....**..**
# ............****xxxx######xxxx##00**~~--..~~--##00xxxx##00########00##xxxx##0000##..  ~~~~..##00**..**xxxxxx**xx**..****....****
# **..........********xxxxxx****##00##..~~~~--xx0000##xx##0000##xx####xx**##xx**0000##xx****##00xx..**xxxxxx************..**......
# ......**....**********xxxxxx**xx##0000####00@@00xxxxxxxx########xx**xxxx##xxxx####00000000##xx**..xx####xxxxxx******............
# ****--..**....********xxxxxxxx**xx##000000####xx****xx####**xx******xx####xx**xxxxxxxx##xx**..**xx##xxxxxxxxxx**..**..--........
# ........**....**********xxxxxxxxxxxxxxxxxxxx****xxxx##00##**xx**....**xx####xxxx********....**####xxxxxxxx**xx**..**............
# ....**....****..******xxxx**xx####xx**********xx####xx##xx****......xx**########xxxxxxxxxx####xxxxxxxxxxxx**xx**..****..--..**..
# **..........**....****xx**xxxxxx##############xxxx##00##..**xx------**xx####**xx******xxxx######xxxxxxxx**xxxx****..............
# ****..**....**....**xxxxxxxx############xxxxxxxx****##xx..**xx..----..##00xx..--..****xxxxxx####xx##xxxxxx******................
# ..............****..**xxxxxxxxxx######xxxx********..xxxx--..**--  ----xx##**--..****xxxxxxxxxx####xxxxxx**xx****..****....**....
# **......**....**********##########xxxxxxxx**........****  ....~~  --~~..xx....**..****xxxxxxxxxx####xxxxxxxx****..****..........
# **..........****..xxxxxx########xxxxxxxx**xx..........--~~--..~~  ~~~~~~**..........**xxxxxxxxxxxxxxxxxxxxxx********......**....
# **....xx....******xx##xxxxxx##xxxxxxxx******..--....~~~~  ----~~      ~~..**........**xxxxxxxxxxxxxxxxxxxxxxxx**********....**..
# ********....************xx####xx****xx****....------~~~~  ~~~~          ..**......******xxxxxx**xx##xxxx**xx******....**........
# **..****....**********xxxxxx##xx****xx****......----~~    ~~~~          --**..--..********xxxx**xxxxxx**xx******................
# ****..****..**************xxxxxxxx****xx****....----    ~~~~  ~~        ~~**..--....****xxxx****xxxx**xx************..........**
# **xx********..**********xx##xxxxxx**..****..**....--                    --**----....**********xxxxxxxxxxxx******..**....**......
# **..********..********xx####xxxxxx**..****..**....--                    --..--........********xxxxxxxxxxxx******....**....****..
# ..********......****xxxx####xxxxxx********..**....--                    --..--........**..****xxxxxxxx##**xx******....**..******
# ******....********xx**xx####xx**xx******......**..--                    --................****xx**xxxxxxxx********........******
# ********......********######****xxxx**..........**~~          ~~        --..........**....**xxxx**xxxx##xx**xxxx**..****..******
# xx******xx....********####xxxx**xxxx**......--..**~~          ~~        --..........**....****xx**xxxx##xxxxxx**..****..********
# **xx********..******xx####xxxx****xx**......--..**~~        ~~~~        --......--......****xx****xxxx##xxxx********************
# **xxxxxx**xx******##xxxx##xxxx****xx**......--..**~~        ~~~~        --****----......****xx****xx########********..********xx
# ##xxxxxxxxxxxxxx**xxxxxx##xxxx****xx**......----**~~        ~~~~        --**..--........**xx******xx####xxxxxxxx************xxxx
# ####xxxx##xxxx####xxxx##00xx##xx******..--....--..~~        ~~~~        --**..--....--..****..**xxxx####xx**xxxx******xxxx**xxxx
# xx##xxxxxxxx**xx####xx##00xxxxxx**..**..--....--..~~        ~~~~~~      --**..--..----..****..****xx######xx****xx****xxxxxxxxxx
# xxxxxxxx######xx######0000xx**##**..****--....--..~~        ~~~~        --**--....----..**....****######xxxxxxxxxx**xx****xxxxxx
# xxxx########xx########00@@xx**xxxx....**..--..--..~~        ----~~      --**--....----****..****xx####xx##xxxxxxxxxxxxxxxxxxxxxx
# ****xxxxxx##xx####xx##00@@##**xxxx....**......--..~~        ~~--~~      ..**--....--..**....****xx######xxxxxxxxxxxxxxxxxxxxxxxx
# ..**xxxxxx##############@@00xx**xx..........**....--        ----~~      ....--..----**..--..**xxxx######xxxxxxxxxxxxxxxxxxxxxxxx
# ........####00########000000##**xx**--....--....----        --~~~~    ~~..--....----**..--****xxxx00######xxxxxxxxxxxxxx##xxxxxx
# --..**xx00########00##000000##******--..**----..----        ~~~~~~    ~~..--....--....~~--****xx########xx####xxxxxxxxxxxxxx####
# ..xx########00####00##000000##xx**xx----**..--....--~~      ~~~~      --....**----**..--..**xxxx####00####xxxxxxxxxxxxxxxxxxxx##
# ....****####00##000000##0000##xx**xx..--**..........~~      ~~~~      --......--..**....******xx0000########xxxxxxxxxxxxxxxxxxxx
# --..**xx00####0000####000000####******....**--......~~      ~~~~      ....**......**--********##0000########xxxxxxxx##xxxxxxxxxx
# ....****xx####000000######0000##xx**xx..****--......~~      ~~~~    ~~....**..--****..**xx**xx############xxxxxxxx####xxxxxxxxxx
# ..******xx####0000####00000000##xx**xx******........        ~~~~    ~~--..**....xx****xxxxxxxx################xxxxxxxxxxxxxxxxxx
# ......**##00######xx######0000####xxxxxx**xx**....--        ~~        --****..**xx****xx**xx##xx##############xxxxxxxxxxxxxxxxxx
# --....xx####00000000####00000000xxxxxx##**xx**....~~        ~~        ~~****..xxxxxx**xx**####xx################xxxx##xxxxxxxxxx
# ----..##########00####xx####0000xxxxxxxx****xx..--                    ~~**....xx******xx##xx##xxxx####xxxx####xxxxxx##xxxxxxxxxx
# ~~--..**xx########xx**xx##########xx######xx**--                        --..**xx**xxxxxxxxxx################xxxxxx####xxxxxxxxxx
# ~~--****xx##xxxx********######xx######xx..--~~                            --..xx**xxxxxxxx##xxxxxxxx######xxxxxxxxxxxxxxxxxxxxxx
# ~~--..**xx####........**xx##########**~~                                      --**xxxxxxxx##xxxxxxxxxxxxxxxx**xx**xxxxxxxxxxxxxx
# ~~--..**xx##**..........xx00######xx--  ~~                                      ~~**xxxxxxxxxx######xxxxxxxxxxxxxx****xxxxxxxxxx
# ~~~~..**xxxx**..........**####xxxx..~~    ~~~~    ~~                              ~~**xxxxxxxxxxxxxx####xxxxxxxxxxxxxx****xx##xx
# ~~~~..**xxxx**..........**######xx--      ~~..**~~  ~~~~~~~~  ~~~~    --..--        --**xxxxxxxxxx**xxxxxxxxxxxxxxxxxxxxxxxxxxxx
#   --..****xx**....----..**xx####xx--          --**~~    ~~~~~~      ..**--~~        ~~**xxxxxx##xxxxxxxxxx**xx******xxxxxxxxxxxx
# ~~~~--**xx**....----......xx####xx--            ~~..~~            ----              ~~**xxxxxxxxxxxxxxxxxxxx************xxxxxxxx
# ~~~~--**xx**......--......**xxxx##--                ~~          ~~                  ~~**xxxxxxxxxxxxxxxx********************xxxx
# ~~~~--****........------....**xx##..~~                ~~~~  ~~~~                    --**xxxxxxxxxxxxxx********....********xxxxxx
# ~~~~~~..**........----......**xxxx**--                ~~~~                        ~~..xxxxxxxxxx******..****............****xxxx
# ~~~~--..........------....**....**xx..~~                                          --****xxxx**xxxx....xx****............******xx
# ~~~~--..--......----..........--..****--~~                                        ..******xxxx....--..xxxx..............****xxxx
# ~~~~------........----..--......--..**..--~~            ~~                      --************--..**....**................****xx
# ~~--~~----........------..--..**..----....--~~~~        ~~~~                  --..****....----....xxxx............--......****xx
# ----------....**..------..--........----....----~~~~~~~~~~~~~~            ~~--**......--------**xx******..............**********
# ------..--..........------............--------........----------~~~~~~--~~--....----------....**xx**..**..............**********
# ------..--..............--........--....----------..............------..--..------------..**..****xx******............**********
# 
# ```
# 
# Voici un autre exemple avec moins de nuance de "couleur" et une image qui s'affichera en moins large puisque moins de caractère par élément de la liste : 
# ```
# ['@', '#', '*', '.', '-', '~', ' ']
# ```
# 
# ```
# -.......*.**.*....*****...*...*..----..**.......*******.*.*.--.-
# -...-..***************#***.--.*.....********#******#******...---
# .--.-..*****##############*****#****###**#############***...--.-
# --.-...***##################*#*#*#####*##**.**#########**...--.-
# ...--..**#*######******#*#####****##*..#*-.*...#********.-...---
# -.---..*#*##***##..*#*.*#.#########*..##.-.*...#.-.***...-.--...
# ------...****..*#...*..#@*.####*###*.*#@#.--..*#.-.***...-..--..
# .----......*...#@#..-.*@#**####*##*.***###****#*--.*......--.---
# .--........*...**####@@#***.####***.#*.######*..-.**....--------
# ..--.--......*...*###***-.*##*****.*#*....**.--.***.....--------
# ----.--........*.........**##*#.*...***.....--.****.....--------
# --.--..-.......*#*.....****#***...*.***.....*#**...*....-..---.-
# ..-.--.--....**.*###***..##*.*#...*.#*---~--.***..**...---------
# ..-.--.--.**..**##*.------#*-*#....##.~~~--...****.**...--------
# ..--.--..-.*****#**.------**-**...-*#-~~------.*****....-.------
# .-...--.....#**#*.-..-~~~-**-**.....*~~-~~~--...******..-..-----
# ....-...-********.----~~~-*.-**......~~~~~------.*.***...-------
# ...*.....***.**.-.-----~~-*..**......-~~~~-----.**......--..----
# ....--......***------~-~~-*..*.......-~~~-----.-.*....-.--------
# .....-...-...**------~~~~-.-.......-.-~~~-~------.....-.--------
# .............*..------~-~-.........-.-~~~~~------....-.--------.
# **....-.....**----~--~--~-.-.........-~~~~~------....-----------
# ......-....*#*----~--~--~-...........~~~~~~--~----....--------.-
# .....-.-..****-------~--~-...........~~~~~~-~-----.*...----.-...
# ....-....*..**-------~~-~-...........~~~~~--~-----.......----.-.
# ...........*#.-----~-~~~~-.....-.....~~~~~-~~-----.*.-...--.-.--
# **..*--....*#.-----~~~~~~-....--....-~-~~~-~~~----.**..------..-
# .*........*#*--~--~~~~~~--.....--...-~-~~-~~~-----.*.*....--....
# ****.....****--~---~~~~~--....--....---~~-~~~-----****--.--..-..
# #******..****-.----~~~~~--....--....---~~~~~---~--**....--......
# ##.*#******#*-.-~--~~-~~~-....--....--~~-~~~--~~-.**...........*
# ******.*##*##-.----~~-~~-.....--....--~~-~~~--~~-.****........*.
# ****##***#*##--.-~--~~-~-.....--....--~--~~---~--.**.**......**.
# ***#*#**####@.-.-~--~~-~~.....--....-~~-~~~--~---.*.**......*...
# ..*****##*##@*~--~~--~-~~.....-~-...-~~-~~~-~~---.*************.
# ..****###**#@*--.~~--~--~-....---...-~~-~~--~~---***.....*****..
# -.-.*#######@#--.-~--~~-~-....---...-~~~~~-~~---.#***.*.**..**.*
# --.*########@#.---~~-~~-~~.....-...-~~-~~--~~~--*##*****.*******
# .**#*#########.---~~-~~-~~.....-...-~~-~~--~----*##*************
# ..***#######@#.----~-----~.........-~--~~-~~----###****.**.*****
# ...*########@#*.---~--~--~-........-~--~--~----.##****.*********
# ..***######**##.------~~--.........-~.-~.-~----*************.***
# ....*#####*####..-.--.----.*.......~--~~.---.-.****************.
# ....###*#***###*.-..-.----.........-.-~-*--.-...**##*****.******
# ...*###########*..-*-.-~--.........-.-~...-.-*...***********.***
# --.#######***##*....-..--............--.----*....***************
# --.**#****..*#***.**..--............-~-.-.....******************
# --..***..-..*#****...--..............--.-....*....****...*******
# --..*#*-----*******....................--....*.***........******
# --..**.-----*#***.*...-........................*...........*****
# --..**.-----.**.**.....---........-----...........**.........***
# --.***.-----.*****....**.-----.----.**....................**.**.
# ~-.*.*.-----..****.....*#...-----.**..........***..........*..*.
# --.**...-----.***......-.*...--..*.-.-..........*.......--..****
# --..*..------..***........*....-.............**.****...-..-.....
# --.*...-.------*#*...........................***.**...----......
# ---..-...-~---.*.............-.............*.***...-..------...*
# ---.....-~------............................**..*--*.------.....
# --.....---.----~-............................*.-.--**-------..**
# -----.-..-------~---...........................-..----------...*
# ----..-..------.-~~--....................*.----.-..---------....
# ---.-..*.----------~-.-.................-------.*...----.--.....
# ---.-.....------.--~~~-----.-.........----------*.-.------......
# ---...-.....-------.---------------.---------.-....-.----.......
# ```

# In[112]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

def convertImageToGrayArray(imgFile = "babouin.png",nombre_pixels = 64):
    img = Image.open(imgFile).convert('L') #charge l'image et la converti directement en image sur des niveaux de gris
    img.thumbnail((nombre_pixels, nombre_pixels), Image.ANTIALIAS) #modifie la taille de l'image pour par défaut l'avoir en 64/64 pixels 
    grayscale_array = np.asarray(img) #converti notre image en tableau d'entier avec chaque case correspondant à des pixels allant de 0 à 255
    return grayscale_array

gray_array = convertImageToGrayArray()  
print(gray_array)
plt.imshow(gray_array, cmap="gray") #affiche une matrice en image avec une colormap de nuances de gris


# In[129]:


#Exercice 8 à vous de jouer !
#<écrivez votre code dans cette cellule juste en dessous de cette ligne> (ici je ne vous tiendrais pas rigueur si vous faites votre code dans plusieurs cellules)


# In[ ]:




