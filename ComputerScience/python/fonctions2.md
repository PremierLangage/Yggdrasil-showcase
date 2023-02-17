

## Arguments variables
Il est possible de définir des fonctions avec un nombre variable d'arguments, en utilisant les *args et **kwargs.

*args permet de passer un nombre variable d'arguments positionnels à la fonction, sous la forme d'un tuple.

**kwargs permet de passer un nombre variable d'arguments nommés à la fonction, sous la forme d'un dictionnaire.

Voici un exemple :

python
Copy code
def ma_fonction(*args, **kwargs):
    for arg in args:
        print(arg)
    for cle, valeur in kwargs.items():
        print(f"{cle} = {valeur}")

ma_fonction(1, 2, 3, a="foo", b="bar")
Dans cet exemple, la fonction `mafonction` prend un nombre variable d'arguments positionnels (*args) et un nombre variable d'arguments nommés (**kwargs). Dans le corps de la fonction, on parcourt les arguments positionnels avec une boucle for, et on affiche chaque argument. Ensuite, on parcourt les arguments nommés avec une boucle for, et on affiche chaque clé-valeur.

Lors de l'appel de la fonction, on peut passer un nombre variable d'arguments positionnels, qui seront regroupés dans un tuple, et un nombre variable d'arguments nommés, qui seront regroupés dans un dictionnaire.

## Fonctions lambda
En Python, il est possible de définir des fonctions anonymes, appelées fonctions lambda. Les fonctions lambda sont utiles pour définir des fonctions courtes et simples, sans avoir à écrire une fonction complète.

Voici un exemple :

python
Copy code
ma_fonction = lambda x, y: x + y
resultat = ma_fonction(5, 10)
print(resultat)  # affiche 15
Dans cet exemple, on définit une fonction lambda qui prend deux arguments x et y, et qui retourne la somme des deux arguments. On appelle ensuite la fonction lambda avec les arguments 5 et 10, et on affiche le résultat.