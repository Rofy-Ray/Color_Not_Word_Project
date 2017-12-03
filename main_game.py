####################################################################################
# Author: Raymond Okyere-Forson
# Username: okyereforsonr
#
# Game: COLOR NOT WORD
# Purpose: Create a program where the user interacts with a GUI by typing the color of words that appear in the window.
#          The user MUST NOT type the word text itself, ONLY the color the text is written in.
#          The user tries to get as many points before the timer runs out.
####################################################################################
# Acknowledgements:
#   Instructor: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter          #Import the module needed for creating a GUI
import random           #Import the module needed for generatinf random numbers

class Gambit:
    def __init__(self):
        '''
        The initializer creates a window to contain the widgets that will be used in playing the game
        '''
        self.color_pick = []            #List of possible colors to be picked
        self.score_board = 0            #Sets the starting score of the user to 0 until the game begins
        self.time_remain = 45           #Sets each game round timer to start at 45 secs
        self.game_hub = tkinter.Tk()    #Creates the root window where all the widgets will be added


    def __str__(self):
        '''
        Makes the str() function work with Gambits
        :return: A formatted string for better printing
        '''
        return "()".format(self.color_pick)

    def game_over(self):
        '''

        :return:
        '''
        if self.time_remain == 45:
            countdown()

