
# Les générateurs en Python
Les générateurs en Python sont des fonctions qui permettent de générer des séquences de valeurs. Ils sont très utiles pour manipuler des données volumineuses, car ils ne génèrent les données qu'au fur et à mesure de leur utilisation, ce qui permet de réduire la consommation de mémoire.

### Définition
Un générateur est une fonction qui contient au moins une instruction yield. La fonction ne retourne pas de valeur avec l'instruction return, mais suspend l'exécution et renvoie une valeur avec yield. À chaque appel de la fonction, celle-ci reprend l'exécution à l'instruction yield où elle s'était arrêtée, et continue jusqu'à atteindre la fin de la fonction ou une nouvelle instruction yield.

Voici un exemple simple de générateur :

python
Copy code
def generateur():
    yield 1
    yield 2
    yield 3
Ce générateur permet de générer la séquence de valeurs 1, 2 et 3. Pour utiliser ce générateur, on peut l'appeler dans une boucle for, comme ceci :

python
Copy code
for valeur in generateur():
    print(valeur)
Ce code affiche les valeurs 1, 2 et 3.

### Avantages des générateurs
Les générateurs présentent plusieurs avantages :

Ils permettent de générer des séquences de valeurs de manière efficace, en ne générant que les valeurs nécessaires.
Ils permettent de manipuler des données volumineuses, sans avoir à les stocker en mémoire.
Ils peuvent être combinés avec d'autres fonctions, comme les fonctions map() et filter(), pour manipuler les valeurs générées.
Méthodes de générateurs
Les générateurs disposent de plusieurs méthodes pour manipuler la séquence de valeurs qu'ils génèrent. Voici les principales méthodes :

send(value): envoie une valeur à la fonction yield suivante, et reprend l'exécution de la fonction. Cette méthode permet de modifier la valeur générée par le générateur.
throw(type[, value[, traceback]]): envoie une exception à la fonction yield suivante, et reprend l'exécution de la fonction. Cette méthode permet de lever une exception dans le générateur.
close(): termine le générateur en envoyant une exception GeneratorExit à la fonction yield suivante. Cette méthode permet de terminer l'exécution du générateur.

### Conclusion
Les générateurs en Python sont un outil très puissant pour manipuler des données volumineuses et générer des séquences de valeurs efficacement. Ils permettent de réduire la consommation de mémoire et de simplifier la compréhension du code. Les générateurs peuvent être combinés avec d'autres fonctions pour manipuler les valeurs générées, et disposent de méthodes pour contrôler leur exécution.




