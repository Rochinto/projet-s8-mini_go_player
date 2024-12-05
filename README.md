# Projet IA : joueur de mini Go

Projet académique ayant pour but de réaliser en individuel une implémentation d'un joueur de mini Go (le jeu de Go mais avec un plateau réduit).

L'objectif étant d'obtenir un joueur (programme Python) le plus intelligent possible afin de gagner face à son adversaire.

Les joueurs de chaque élèves seront mis en compétition dans un grand tournoi automatisé.

## Utilisation

Le programme `Tester.py` permet de lancer une simulation de plusieurs parties entre deux joueurs implémentés.

Ce répertoire possède deux implémentations de joueurs:
- `myPlayer.py` le joueur utilisé pour la compétetion finale.
- `randomPlayer.py` un joueur pour les tests qui joue aléatoirement

## Description et fonctionnement du joueur obtenu

Pour chaque coup le joueur `myPlayer.py` joue selon l'algorithme décrit ci-dessous.

Il crée un arbre de possibilités (de profondeur 2) en explorant au hasard 10 coups.
Et effectue une recherche minimax depuis les noeuds terminaux pour choisir le coup qui lui semble le plus favorable, en utilisant **l'heuristique** pour valeurs.\
*La profondeur et le nombre de coups explorés ont étés choisis pour respecter les contraintes de temps de la compétition finale.*

Il utilise comme heuristique:\
**Pour ses 25 premiers coups** => une heuristique obtenue par une analyse de données d'un grand nombre d'ouvertures et obtention d'un modèle par Machine Learning (le modèle keras est enregistré dans le dossier `go_heuristic`).\
**Pour les coups suivants** => le score du plateau donné par le programme `Goban.py`, c'est à dire la valeur du plateau (du joueur) selon la convention des règles chinoises.

Le joueur (`myPlayer.py`) dépend des bibliothèques:
- `tensorflow`
- `keras`
- `numpy`
- `random`
Et fichiers:
- `playerInterface.py`
- `possibilityTree.py`
- `Goban.py`
