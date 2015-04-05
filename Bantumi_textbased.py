# -*- coding: utf-8 -*-
import os
import re
import sys

class Bantumi():

    def __init__(self):
        self._board = []
        for i in range(0, 15, 1):
            self._board.insert(i, 3)
        self._board[0]=0
        self._board[14]=0

        self.draw_gameboard()
        

    def draw_gameboard(self):

        # Zeichne zuerst die obere, der KI gehoerende Reihe des Spielfelds
        # und zwar von links nach rechts
        # der loop geht damit von 13 bis 7,
        # wobei Feld 14 das Heimfeld der KI ist

        sys.stdout.write("     ")
        for i in range(13, 7, -1):
            if self._board[i]<10: sys.stdout.write("0") 
            print self._board[i],
            print " ",

        # Neue Zeile
        print
        
        # Mittlere Zeile mit den Heimfeldern zeichnen
        sys.stdout.write("   ")

        # Zeichne Heimfeld des Spielers
        print self._board[0],

        for i in range(0,25):
            if i%4 == 0: sys.stdout.write("|")
            else: sys.stdout.write("-")

        # Zeichne Heimfeld der KI
        print self._board[14],

        # Neue Zeile
        print
        sys.stdout.write("     ")
        # Zeichne Spielfelder des Humanoiden
        # das sind die Felder 1 - 7
        for i in range(1,7):
            if self._board[i]<10: sys.stdout.write("0")
            print self._board[i],
            print " ",

Bantumi()
