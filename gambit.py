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

from tkinter import *
import tkinter          #Import the module needed for creating a GUI
import random           #Import the module needed for generatinf random numbers
import time

class Gambit:
    def __init__(self):
        '''
        The initializer creates a window to contain the widgets that will be used in playing the game
        '''

        self.color_pick = []          #List of possible colors to be picked
        self.score_board = 0            #Sets the starting score of the user to 0 until the game begins
        self.time_remain = 45           #Sets each game round timer to start at 45 secs
        self.interface = Interface()
        self.interface.score = self.score_board
        self.interface.time_left = self.time_remain



        self.extract_color()
        # print(self.color_pick)
        self.next_color_word()
        # self.game_over()
        self.game_timer()

        # self.interface.game_hub.bind('<Return>', self.game_over())              #Run the game_over() function when the Enter key is pressed


        # Always last
        self.interface.game_hub.mainloop()

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
        # global time_remain          #Use globally declared 'playtime' variable above

        if self.time_remain > 0:         #Condition runs if game is currently in session
            self.time_remain -= 1        #Decreases the amount of time left on the timer
            # self.interface.timerLabel.config(text = 'Time remaining: ' + str(self.time_remain))       #Updates the time remaining label
            self.interface.timer_label(time_left=self.time_remain)

            self.interface.timer_label.after(1000, self.game_timer())                             #Runs the function again after each second

    def extract_color(self):
        '''
        Gets colors from the text file and put them into a list to be used by the game
        :return:
        '''

        theFile = open('color.txt', 'r')
        myColors = theFile.readlines()
        for i in myColors:
            i = i[:-1]
            self.color_pick.append(i)
        theFile.close()

    def next_color_word(self):
        '''
        Chooses and displays the next color word text to display and the color for printing the text
        :return:
        '''

        # global score_board          #Use globally declared 'scores' variable above
        # global time_remian          #Use globally declared 'playtime' variable above

        # x = random.choice(self.color_pick)
        # print(x)
        # word = random.choice(self.color_pick)
        # color = random.choice(self.color_pick)
        # self.interface.print_out(word, color)
        # print(word)

        if self.time_remain > 0:         #Condition runs if game is currently in session
            # self.interface.textbox()#.text_entry.focus_set()  #Makes the text entry box active if game is in session

            word = random.choice(self.color_pick)
            color = random.choice(self.color_pick)
            self.interface.print_out(word, color)

            if self.interface.inputValue == word:     #Checks if color entered by user equals the text color
                #     print(random.choice(self.color_pick))
                self.score_board += 1                                #Adds one to the score of the user

            # self.interface.text_entry.delete(0, tkinter.END)                   #Clears the text entry box
            random.shuffle(self.color_pick)                     #Shuffle the list of colors

            self.interface.print_out(word, color)
            self.interface.score_label(score=self.score_board)


                #Changes the color to type by changing the color and text to a random color value
            # self.interface.
            # self.interface.color_label() #.colorLabel.config(fg = str(random.choice(self.color_pick)), text = str(random.choice(self.color_pick)))
            # self.interface.score_label() #.config(text = 'Your score: ' + str(self.score_board))     #Updates the score board
            # self.interface.scoresLabel = tkinter.Label(self.interface.game_hub, text = 'Your score is: ' + str(self.score_board), font = ('Tahoma', 12))


    # def game_over(self):
    #     '''
    #     Checks if game has not began and starts the timer
    #     :return:
    #     '''
    #
    #     if self.time_remain == 45:               #Condition runs if there is still time left on the countdown timer
    #         self.game_timer()                        #Start the countdown timer

class Interface:
    def __init__(self):
        '''

        '''

        # self.gambit = gambit
        self.game_hub = tkinter.Tk()            #Creates a GUI window for the game
        self.rule = ''
        self.scoresLabel = ''
        self.timerLabel = ''
        self.colorLabel = ''
        # self.text_entry = self.textbox()
        self.showword = ''
        self.inputValue = ''
        self.build_GUI()
        self.start_label()
        self.score_label(score=self.scoresLabel)
        # self.print_out(word=self.showword, color=self.showword)
        self.textbox()
        self.timer_label(time_left=self.timerLabel)
        self.retrieve_input()
        # self.color_label()

    def build_GUI(self):
        '''

        :return:
        '''

        self.game_hub.title('GUESS THE COLOR')        #Sets the title for the GUI window
        self.game_hub.geometry('375x250')     #Sets the size of the GUI window

        #Add an instructions label to the GUI
        self.rule = tkinter.Label(self.game_hub, text = 'Type in the color of the word. NOT the word text!', font = ('Tahoma', 12))
        self.rule.pack()         #Add the widget to the GUI

    def start_label(self):
        '''

        :return:
        '''

        #Add a scores label to the GUI
        self.startLabel = tkinter.Label(self.game_hub, text = 'Press Enter to begin the game.', font = ('Tahoma', 12))
        self.startLabel.pack()         #Add the widget to the GUI

    def print_out(self, word, color):
        '''

        :return:
        '''

        self.showword = tkinter.Label(self.game_hub, text = str(word), font = ('Tahoma', 50))
        self.showword.configure(foreground = color)
        self.showword.pack()

    def score_label(self, score):
        '''

        :return:
        '''

        self.scoresLabel = tkinter.Label(self.game_hub, text = 'Your score is: ' + str(score), font = ('Tahoma', 12))
        self.scoresLabel.pack()


    def timer_label(self, time_left):
        '''

        :return:
        '''

        #Add a time remaining label to the GUI
        self.timerLabel = tkinter.Label(self.game_hub, text = 'Time remaining: ' + str(time_left), font = ('Tahoma', 12))
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

        # self.text_entry = tkinter.Entry(self.game_hub)       #Creates the text entry box for the user to type in the colors
        self.text_entry = Text(self.game_hub, height = 1, width = 20)
        self.text_entry.pack()           #Add the widget to the GUI
        self.text_entry.focus_set()      #Sets the focus of the cursor in the text entry box
        buttonCommit = Button(self.game_hub, height = 1, width = 10, text = 'Submit', command = lambda: self.retrieve_input())
        buttonCommit.pack(pady=10)

    def retrieve_input(self):
        '''

        :return:
        '''

        inputValue = self.text_entry.get("1.0", 'end-1c')
        print(inputValue)


def main():
    '''

    :return:
    '''
    g = Gambit()

if __name__ == "__main__":
    main()
