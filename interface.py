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
from gambit import Gambit


class Interface:
    def __init__(self):
        '''

        '''

        self.game_hub = tkinter.Tk()            #Creates a GUI window for the game
        self.rule = ''
        self.scoresLabel = ''
        self.timerLabel = ''
        self.colorLabel = ''
        self.text_entry = ''
        self.build_GUI()
        self.score_label()
        self.textbox()
        self.timer_label()
        # self.color_label()


        # self.gambit = Gambit()



    def build_GUI(self):
        '''

        :return:
        '''

        self.game_hub.title('COOL GAME')        #Sets the title for the GUI window
        self.game_hub.geometry('375x200')     #Sets the size of the GUI window

        #Add an instructions label to the GUI
        self.rule = tkinter.Label(self.game_hub, text = 'Type in the color of the word. NOT the word text!', font = ('Tahoma', 12))
        self.rule.pack()         #Add the widget to the GUI

    def score_label(self):
        '''

        :return:
        '''

        #Add a scores label to the GUI
        self.scoresLabel = tkinter.Label(self.game_hub, text = 'Press Enter to begin the game.', font = ('Tahoma', 12))
        self.scoresLabel.pack()         #Add the widget to the GUI
        self.game_hub.bind('<Return>', Gambit.game_over(self))              #Run the game_over() function when the Enter key is pressed

    def timer_label(self):
        '''

        :return:
        '''

        #Add a time remaining label to the GUI
        self.timerLabel = tkinter.Label(self.game_hub, text = 'Time remaining: ' + "0", font = ('Tahoma', 12))  #FIXME str(time_remain) (self.gambit.time_remain)
        self.timerLabel.pack()           #Adds the widget to the GUI

    # def color_label(self):
    #     '''
    #
    #     :return:
    #     '''
    #
    #     #Add a color label to the GUI to display the colors
    #     self.colorLabel = tkinter.Label(self.game_hub, font = ('Tahoma', 50))
    #     self.colorLabel.pack()       #Adds the widget to the GUI

    def textbox(self):
        '''

        :return:
        '''
        self.text_entry = tkinter.Entry(self.game_hub)       #Creates the text entry box for the user to type in the colors

        self.text_entry.pack()           #Add the widget to the GUI
        self.text_entry.focus_set()      #Sets the focus of the cursor in the text entry box
