
# Les tuples en Python
Les tuples en Python sont des structures de données qui permettent de stocker une collection ordonnée d'objets. Les tuples sont très similaires aux listes, mais contrairement aux listes, les tuples sont immuables, ce qui signifie que les éléments d'un tuple ne peuvent pas être modifiés une fois qu'ils ont été définis.

## Création d'un tuple
Un tuple en Python est créé à l'aide de parenthèses ( ). Les valeurs du tuple sont séparées par des virgules. Voici un exemple de création d'un tuple :

```python
mon_tuple = (1, 2, 3, 4, 5)
```
Dans cet exemple, on crée un tuple mon_tuple qui contient les valeurs 1, 2, 3, 4 et 5.

## Accès aux éléments d'un tuple
On peut accéder aux éléments d'un tuple en utilisant leur indice, qui commence à 0. Pour accéder au premier élément du tuple, on utilise l'indice 0. Pour accéder au deuxième élément, on utilise l'indice 1, et ainsi de suite. Voici un exemple :

```python
mon_tuple = (1, 2, 3, 4, 5)
print(mon_tuple[0])  # affiche 1
print(mon_tuple[1])  # affiche 2
print(mon_tuple[2])  # affiche 3
```
On peut également accéder aux éléments d'un tuple en utilisant des indices négatifs, qui permettent d'accéder aux éléments depuis la fin du tuple. L'indice -1 permet d'accéder au dernier élément du tuple, l'indice -2 permet d'accéder à l'avant-dernier élément, et ainsi de suite.

## Modification des éléments d'un tuple
Comme mentionné précédemment, les tuples sont immuables, ce qui signifie que les éléments d'un tuple ne peuvent pas être modifiés une fois qu'ils ont été définis. Si vous essayez de modifier un élément d'un tuple, vous obtiendrez une erreur.
L'intéret de cette propriété est de pouvoir être utilisée comme clef de dictionnaire. 

## Utilisation de tuples avec des fonctions
Les tuples sont souvent utilisés en Python pour retourner plusieurs valeurs à partir d'une fonction. Par exemple, voici une fonction qui retourne le minimum et le maximum d'une liste :

```python
def min_max(lst):
    return min(lst), max(lst)
```
Cette fonction retourne un tuple contenant le minimum et le maximum de la liste passée en argument.


Pour que la fonction retourne une liste il ne faut pas oublier les []. 

```python
def min_max(lst):
    return [min(lst), max(lst)]
```
