#!/usr/bin/python
import os
import re
import sys

class Awari(): # aka. Bantumi 

   def __init__(self):
      self._board = []
      self._playermove = 0
      self._invalid_move = 0
      for i in range(0,14): self._board.insert(i,3)
      self._board[6]  = 0 # Heimfeld des Spielers
      self._board[13] = 0 # Heimfeld der KI
      
      self.zeichne_spielfeld()
      self.spielzug()


   def zeichne_spielfeld(self):

      # Bildschirm leeren
      if os.name != 'nt':
         os.system("clear")
      else:
         os.system("cls")
   
      print "   ",
      for i in range(12, 6, -1):
         if self._board[i] < 10: print "0"+str(self._board[i]) + " ", 
   
      print ; print self._board[6],

      for i in range(0,14):
         print "-",
      
      print self._board[13]

      print "   ",
      for i in range(0,6):
         if self._board[i] < 10: print "0"+str(self._board[i]) + " ", 

      if self._invalid_move != 0:
         print "\n\nUngueltiger Zug:",
         
         if self._invalid_move == 1:
            print "ist nicht dein Feld"
         elif self._invalid_move == 2:
            print "keine Bohnen auf diesem Feld"  
       
         

   
   def spielzug(self):
      self._invalid_move = 0
      
      print "\n\nDein Spielzug? (Feld: 1 - 6)"
      playermove = raw_input()
      if not re.match("[0-9]", playermove):
         if re.match("q|Q", playermove):
            sys.exit()
         else:
            self._invalid_move = 1
            self.zeichne_spielfeld()
            self.spielzug()
      else:
        self._playermove = int(playermove)
        self._playermove -=1
      
      if self._playermove < 0 or self._playermove > 6:
         self._invalid_move = 1
         self.zeichne_spielfeld()
         self.spielzug()
      elif self._board[self._playermove] == 0:
         self._invalid_move = 2
         self.zeichne_spielfeld()
         self.spielzug()
      else:
         self._invalid_move = 0
         self.spielzug_ausfuehren()
          
   def spielzug_ausfuehren(self):
      current_field = self._playermove + 1
      current_field_val = self._board[self._playermove]
      self._board[self._playermove] = 0
      for beans in range(current_field_val, 0, -1):
         self._board[current_field] += 1
         current_field += 1
         if current_field > 13: current_field = 0
      self.zeichne_spielfeld()
      self.spielzug()

Awari()
