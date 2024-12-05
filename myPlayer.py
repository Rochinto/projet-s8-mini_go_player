# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import Goban 
from random import sample
from playerInterface import *
from possibilityTree import *

from tensorflow import keras
import numpy as np

def board_to_matrix(board):
    matrix = np.zeros((9,9,2))

    for x in range(9):
        for y in range(9):
            if board[y*9+x]==1:
                matrix[x,y,0] = 1
            elif board[y*9+x]==2:
                matrix[x,y,1] = 1

    return np.array([matrix])

class myPlayer(PlayerInterface):
    ''' Example of a random player for the go. The only tricky part is to be able to handle
    the internal representation of moves given by legal_moves() and used by push() and 
    to translate them to the GO-move strings "A1", ..., "J8", "PASS". Easy!

    '''

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None
        self.tree = None
        self.move = 0
        self.model = keras.models.load_model("go_heuristic")

    def getPlayerName(self):
        return "Rochinto"
    
    def evalBoard(self):
        if self.move < 25:
            heuristic = self.model.predict(board_to_matrix(self._board._board), verbose=0)[0]
            if self._mycolor == Goban.Board._BLACK:
                return heuristic[0]
            elif self._mycolor == Goban.Board._WHITE:
                return heuristic[1]
            #else
            print("{"+self.getPlayerName()+"} Error in evalBoard(): player color invalid")
            return None
        else:
            scores = self._board.compute_score()
            if self._mycolor == Goban.Board._BLACK:
                return scores[0]-scores[1]
            elif self._mycolor == Goban.Board._WHITE:
                return scores[1]-scores[0]
            #else
            print("{"+self.getPlayerName()+"} Error in evalBoard(): player color invalid")
            return None

        


    def create_possibilityTree(self, depth_max=1, monteCarlo=2):
        node = Tree()
        
        if (depth_max <= 0) or (self._board.is_game_over()):
            node.value = self.evalBoard()
            return node
        #else
        moves = self._board.legal_moves()
        if monteCarlo < len(moves):
            moves = sample(moves, monteCarlo)

        for move in moves:
            self._board.push(move)
            node.add_child(self.create_possibilityTree(depth_max-1, monteCarlo))
            node.childs[-1].move = move
            self._board.pop()
        
        if node.is_leaf():
            node.value = self.evalBoard()
        return node
    

    def getPlayerMove(self):
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS"
        

        tree = self.create_possibilityTree(2,10)
        best = minimax(tree)
        #dfs_print(tree)

        move = -1 #PASS
        for child in tree.childs:
            if child.value >= best:
                move = child.move
                break
        #print(move)

        self._board.push(move)
        self.move += 1

        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        print("My current board :")
        self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string
        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        print("Opponent played ", move) # New here
        # the board needs an internal represetation to push the move.  Not a string
        self._board.push(Goban.Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")



