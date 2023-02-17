
Les fonctions en Python
Les fonctions en Python permettent d'organiser son code en réutilisant des blocs de code, qui pourront être appelés à plusieurs reprises dans le programme. Les fonctions permettent de simplifier le code en le découpant en blocs plus petits et plus faciles à comprendre.

Définition d'une fonction
Pour définir une fonction en Python, on utilise le mot-clé def, suivi du nom de la fonction et de ses arguments entre parenthèses. Ensuite, on écrit le bloc de code de la fonction, qui sera indenté.

Voici un exemple :

python
Copy code
def ma_fonction(arg1, arg2):
    resultat = arg1 + arg2
    return resultat
Dans cet exemple, on définit une fonction ma_fonction qui prend deux arguments arg1 et arg2. Le bloc de code de la fonction consiste simplement à additionner les deux arguments et à renvoyer le résultat.

Appel d'une fonction
Pour appeler une fonction en Python, on utilise simplement son nom, suivi des arguments entre parenthèses. Le résultat de la fonction peut être stocké dans une variable.

Voici un exemple :

python
Copy code
resultat = ma_fonction(5, 10)
print(resultat)  # affiche 15
Dans cet exemple, on appelle la fonction ma_fonction avec les arguments 5 et 10. Le résultat de la fonction est 15, qui est stocké dans la variable resultat. On affiche ensuite le résultat avec la fonction print.

Arguments par défaut
Il est possible de définir des valeurs par défaut pour les arguments d'une fonction. Dans ce cas, si l'argument n'est pas précisé lors de l'appel de la fonction, il prendra la valeur par défaut définie.

Voici un exemple :

python
Copy code
def ma_fonction(arg1, arg2=0):
    resultat = arg1 + arg2
    return resultat

resultat1 = ma_fonction(5)
resultat2 = ma_fonction(5, 10)

print(resultat1)  # affiche 5
print(resultat2)  # affiche 15
Dans cet exemple, la fonction ma_fonction prend deux arguments, mais arg2 a une valeur par défaut de 0. Ainsi, si on n'appelle la fonction qu'avec un seul argument, arg2 prendra la valeur 0. Si on appelle la fonction avec deux arguments, arg2 prendra la valeur spécifiée.
