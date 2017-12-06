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
import time

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

    def game_timer(self):
        '''
        Creates a timer that will be used for playing the game
        :return:
        '''
        global time_remain          #Use globally declared 'playtime' variable above

        if time_remain > 0:         #Condition runs if game is currently in session
            time_remain -= 1        #Decreases the amount of time left on the timer
            timerLabel.config(text = 'Time remaining: ' + str(time_remain))       #Updates the time remaining label
            timerLabel.after(1000, game_timer)                                    #Runs the function again after each second

    def extract_color(self):
        '''
        Gets colors from the text file and put them into a list to be used by the game
        :return:
        '''
        theFile = open('color.txt', 'r')
        while True:
            myColors = theFile.readline()
            self.color_pick.append(myColors)
            break
        theFile.close()

    def next_color_word(self):
        '''
        Chooses and displays the next color word text to display and the color for printing the text
        :return:
        '''
        global score_board          #Use globally declared 'scores' variable above
        global time_remian          #Use globally declared 'playtime' variable above

        if time_remian > 0:         #Condition runs if game is currently in session
            text_entry.set_focus()  #Makes the text entry box active if game is in session

            if text_entry.get().lower() = color_pick[1].lower():      #Checks if color entered by user equals the text color
                score_board += 1                                #Adds one to the score of the user

            text_entry.delete(0, tkinter.END)                   #Clears the text entry box
            random.shuffle(self.color_pick)                     #Shuffke the list of colors
            label.config(fg = str(color_pick[1]), text = str(color_pick[0]))    #Changes the color to type by
                                                                                #changing the color and text to a
                                                                                #random color value
            scoresLabel.config(text = 'Your score: ' + str(score_board))     #Updates the score board

    def game_over(self):
        '''
        Checks if game has not began and starts the timer
        :return:
        '''
        if time_remain == 45:               #Condition runs if there is still time left on the countdown timer
            game_timer()                        #Start the countdown timer
