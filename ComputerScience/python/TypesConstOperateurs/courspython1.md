# Introduction à Python
Python est un langage de programmation de haut niveau et facile à apprendre. Il est très populaire pour la création de scripts, l'analyse de données, la construction d'applications web et bien plus encore. Dans ce cours, nous allons apprendre les bases de la programmation en Python.

## Les types de données en Python
Python a plusieurs types de données intégrés. Les types de données les plus courants sont:

### Entiers (int)
Les entiers sont des nombres entiers sans décimale. Par exemple:

```python

x = 5
y = -10
```

Flottants (float)
Les flottants sont des nombres décimaux. Par exemple:

```python

x = 3.14
y = -0.5
```

Booléens (bool)
Les booléens ne peuvent avoir que deux valeurs: True ou False. Par exemple:

```python

x = True
y = False
```
Chaînes de caractères (str)
Les chaînes de caractères sont des séquences de caractères. Elles sont entourées de guillemets simples ou doubles. Par exemple:

```python

x = "Hello, World!"
y = 'Bonjour le monde!'
```
## Les opérateurs en Python
Python a plusieurs opérateurs intégrés. Les opérateurs les plus courants sont:

### Opérateurs arithmétiques
Les opérateurs arithmétiques sont utilisés pour effectuer des opérations mathématiques. Les opérateurs arithmétiques les plus courants sont:

```python

x = 10
y = 3

print(x + y)  # addition
print(x - y)  # soustraction
print(x * y)  # multiplication
print(x / y)  # division
print(x % y)  # modulo (reste de la division)
print(x ** y) # puissance
```

## Les opérateurs logiques en Python
En Python, il existe trois opérateurs logiques :

and (et)
or (ou)
not (non)
Ces opérateurs sont utilisés pour évaluer des expressions logiques.

### L'opérateur and
L'opérateur and renvoie True si et seulement si les deux expressions qu'il relie sont toutes deux évaluées à True. Sinon, il renvoie False.

Voici un exemple :

```python
>>> x = 5
>>> y = 10
>>> x < 10 and y > 5
True
>>> x > 10 and y > 5
False
Dans le premier exemple, les deux expressions sont vraies, donc l'opérateur and renvoie True. Dans le deuxième exemple, la première expression est fausse, donc l'opérateur and renvoie False.

### L'opérateur or
L'opérateur or renvoie True si au moins l'une des deux expressions qu'il relie est évaluée à True. Sinon, il renvoie False.

Voici un exemple :

```python
>>> x = 5
>>> y = 10
>>> x < 10 or y < 5
True
>>> x > 10 or y < 5
False
````

Dans le premier exemple, l'expression x < 10 est vraie, donc l'opérateur or renvoie True. Dans le deuxième exemple, les deux expressions sont fausses, donc l'opérateur or renvoie False.

### L'opérateur not
L'opérateur not inverse la valeur de l'expression qui le suit. S'il est utilisé avec une expression évaluée à True, il renvoie False. S'il est utilisé avec une expression évaluée à False, il renvoie True.

Voici un exemple :

```python
>>> x = 5
>>> not x == 5
False
>>> not x > 10
True
````

Dans le premier exemple, l'expression x == 5 est vraie, donc l'opérateur not renvoie False. Dans le deuxième exemple, l'expression x > 10 est fausse, donc l'opérateur not renvoie True.

## Des opérateurs fainéants

Les opérateurs sont dit fainéants c'est à dire que si la valeur de vérité peut être connus dès l'évaluation du premier membre d'un and ou d'un or alors le deuxième membre n'est pas évalué.

Cela permet de définir des *gardes* le test du premier membre permettant d'éviter le calcul du deuxième. 

Par exemple dans le code suivant on a une fonction f qui calcule une valeur et qui met ajour une variable a, si la variable a est None alors il faut calculer sinon c'est déja fait.

```python
a != None or f()
```
