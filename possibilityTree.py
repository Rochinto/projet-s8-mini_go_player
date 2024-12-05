# -*- coding: utf-8 -*-

'''
Class to define a possibility tree in a recursive way
A leaf must not have 'None' value if the user wants to compute minmax (or maxmin)
'''
class Tree():

    def __init__(self):
        self.childs = []
        self.value = None
        self.board = None
        self.move = None
    
    def is_leaf(self):
        return (len(self.childs)<=0)

    def add_child(self, child_tree):
        self.childs.append(child_tree)



def dfs_print(tree):
    print(tree.board, end="")
    print("PTS", tree.value)
    print("")
    for child in tree.childs:
        dfs_print(child)

'''
minimax function
'''

def minimax(tree, maximizingPlayer=True):
    if tree.is_leaf():
        return tree.value

    best = 10**9    
    if maximizingPlayer:
        best = -best
        for child in tree.childs:
            best = max(best, minimax(child, False))
        tree.value = best
        return best
    #else (Minimizing player)
    for child in tree.childs:
        best = min(best, minimax(child, True))
    tree.value = best
    return best

def is_values_constant(tree):
    pass
