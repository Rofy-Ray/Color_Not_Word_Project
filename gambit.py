####################################################################################
# Author: Raymond Okyere-Forson
# Username: okyereforsonr
#
# Game: COLOR NOT WORD
# Purpose: Creates a program where the user interacts with a GUI by typing the color of words that appear in the window.
#          The user MUST NOT type the word text itself, ONLY the color the text is written in.
#          The user tries to get as many points before the timer runs out.
####################################################################################
# Acknowledgements:
#   Instructor: Dr. Scott Heggen
#   T.As: Rusty Dotson & Aaron Christon
#   Code Review - Stack Exchange
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################


from tkinter import *   #Import all from the tkinter module
from PIL import ImageTk,Image
import tkinter          #Import the module needed for creating a GUI
import random           #Import the module needed for generatinf random numbers


class Gambit:

    def __init__(self):
        '''
        This initializer creates the necessary variables and functions needed to run and play the game
        '''

        self.current_word = ''          #Variable to hold the random word text from the list of colors
        self.current_color = ''         #Variable to hold the random color of the word text chosen from the list of colors
        self.user_input_color = ''      #Variable that will hold the user input in the text box
        self.color_pick = []            #List of possible colors to be picked
        self.score_board = 0            #Sets the starting score of the user to 0 until the game begins
        self.time_remain = 60           #Sets each game round timer to start at 60 secs
        self.interface = Interface(self)        #This creates a variable that references the Interface class so methods and ojects from that class can be called
        self.interface.time_left = self.time_remain     #This passes the time_remain variable to the parameter time_left in a method in the Interface clas
        self.extract_color()            #Function call that reads all the colors in the text file and appends them to a list to be used by the game
        self.next_color_word()          #Function call that selects the random colors to be used for the word text and the color of the word text being displayed in the GUI
        self.game_timer()               #Function that triggers the countdown timer being used by the game
        self.interface.game_hub.after(1000, self.interface.update_timer_label)      #Runs the function that makes sure the timer counts down after each second
        self.interface.game_hub.bind("<Return>", self.interface.get_user_input)     #Keypress trigger that gets the user input in the text box
        self.interface.game_hub.mainloop()          #Infinitie loop that handles events of the game one at a time

    def __str__(self):
        '''
        Makes the str() function work with Gambits
        :return: A formatted string for better printing
        '''

        return "()".format(self.color_pick)

    def game_timer(self):
        '''
        Creates a timer that will be used for playing the game
        :return: None
        '''

        if self.time_remain > 0:         #Condition runs if game is currently in session
            self.time_remain -= 1        #Decreases the amount of time left on the timer
            self.interface.timer_label(time_left=self.time_remain)          #This displays the timerLabel in the GUI

    def extract_color(self):
        '''
        Gets colors from the text file and put them into a list to be used by the game
        :return: None
        '''

        theFile = open('color.txt', 'r')        #Opens the color.txt file ready to read
        myColors = theFile.readlines()          #Reads each line of the text file
        for i in myColors:                      #Goes through all the color names that have been read from the text file
            i = i[:-1]                          #For each color selected, it removes the break line from the end of the color name
            self.color_pick.append(i)           #Takes all the colors that have been read from the text file and puts them in the list
        theFile.close()                         #Closes out the file after reading the content

    def next_color_word(self):
        '''
        Chooses and displays the next color word text to display and the color for printing the text
        :return: None
        '''

        if self.time_remain > 0:         #Condition runs if game is currently in session
            # self.interface.textbox()#.text_entry.focus_set()  #Makes the text entry box active if game is in session
            self.interface.text_entry.focus_set()               #Sets the focus of the cursor in the text box

            self.current_word = random.choice(self.color_pick)      #Picks a random color from the list of colors and assigns it to the current_word variable
            self.current_color = random.choice(self.color_pick)     #Picks a random color from the list of colors and assigns it to the current_color variable

            self.interface.print_out(self.current_word, self.current_color)         #This displays the word text and the color of the text in the GUI

    def check_for_true(self):
        '''
        Checks to see if the user entry is equal to the randomly chosen text color. If the user entry matches the color of the text, new randomly chosen colors for
        the word text and text color are displayed
        :return: None
        '''

        if self.user_input_color == self.current_color:     #Checks if color entered by user equals the text color
                self.score_board += 1                                #Adds one to the score of the user
                self.interface.update_score_label()                     #Displays the user current score

                self.current_word = random.choice(self.color_pick)      #Picks another random color from the list of colors and assigns it to the current_word variable
                self.current_color = random.choice(self.color_pick)     #Picks another random color from the list of colors and assigns it to the current_color variable
                self.interface.text_entry.delete(1.0, END)                   #Clears the text entry box

                self.interface.game_hub.bind('<Return>', self.interface.get_user_input)     #Gets the user input when the Enter key is pressed after user entry
                self.user_input_color = ''                                                  #Makes sure the user input is not passed as the subsequent user input
                self.interface.update_print_out()                                           #This displays the word text and the color of the text in the GUI

class Interface:

    def __init__(self, game):
        '''
        This initializer creates the labels that will be displayed in the GUI window of the game & creates a window to contain the widgets that will be used in playing the game
        :param game: Reference to the Gambit class
        '''

        self.gambit = game                      #Passes the Gmabit class to the variable gambit
        self.game_hub = tkinter.Tk()            #Creates a GUI window for the game
        self.scoresLabel = ''                   #Initializes the scoresLabel variable in the score_label method
        self.build_GUI()                        #Calls the build_GUI method
        self.score_label(score=self.scoresLabel)            #Calls the score_label method
        self.textbox()                          #Calls the textbox method

    def build_GUI(self):
        '''
        Sets the size of the GUI window, adds a title to the window and also creates a label that tells the user how to play
        :return: None
        '''

        self.game_hub.title('GUESS THE COLOR')        #Sets the title for the GUI window
        self.game_hub.geometry('400x250')     #Sets the size of the GUI window

        #Add an instructions label to the GUI
        self.rule = tkinter.Label(self.game_hub, text = 'Type in the color of the word. NOT the word text!', font = ('Tahoma', 12))
        self.rule.pack()         #Add the widget to the GUI

    def print_out(self, word, color):
        '''
        Creates the label that displayes the colored word text in the GUI
        :return: None
        '''

        self.showword = tkinter.Label(self.game_hub, text = str(word), font = ('Tahoma', 60))
        self.showword.configure(foreground = color)
        self.showword.pack()

    def update_print_out(self):
        '''
        Displays the randomly selected word text and text color as it chnages in the GUI window
        :return: None
        '''

        self.showword.configure(text = str(self.gambit.current_word))
        self.showword.configure(foreground = self.gambit.current_color)

    def score_label(self, score):
        '''
        Creates the label that shows the user score in the GUI window
        :return: None
        '''

        self.scoresLabel = tkinter.Label(self.game_hub, text = 'Your score is: ' + str(self.gambit.score_board), font = ('Tahoma', 12))
        self.scoresLabel.pack()

    def update_score_label(self):
        '''
        Displays the updated score of the user as they play the game
        :return:
        '''

        self.scoresLabel.configure(text = 'Your Score is: {0}'.format(self.gambit.score_board))

    def timer_label(self, time_left):
        '''
        Creates the label that shows the user time remaining in the GUI window
        :return: None
        '''

        #Add a time remaining label to the GUI
        self.timerLabel = tkinter.Label(self.game_hub, text = 'Time remaining: ' + str(time_left), font = ('Tahoma', 12))
        self.timerLabel.pack()          #Adds the widget to the GUI

    def update_timer_label(self):
        '''
        Displays the time as it counts down in the GUI window and then freezes the user text entry box when the timer gets to 0
        :return: None
        '''

        if self.gambit.time_remain > 0:
            self.gambit.time_remain -= 1
            self.timerLabel.configure(text = 'Time remaining: ' + str(self.gambit.time_remain))
            self.game_hub.after(1000, self.update_timer_label)
        else:
            self.text_entry.configure(height = 1, width = 20, state = 'disabled')

    def textbox(self):
        '''
        Creates the text entry box in the GUI window used for user input
        :return: None
        '''

        # self.text_entry = tkinter.Entry(self.game_hub)       #Creates the text entry box for the user to type in the colors
        self.text_entry = Text(self.game_hub, height = 1, width = 20)
        self.text_entry.pack()           #Add the widget to the GUI

    def get_user_input(self, event):
        '''
        Gets the user input and then deletes the user entry in the text box afte each input. Then makes a call to the check_for_true method in the Gmabit class
        :param event:
        :return: None
        '''

        self.gambit.user_input_color = self.text_entry.get('1.0', 'end-1c')[:-1]            #Gets the user input from the text box
        self.text_entry.delete(1.0, END)                                                    #Clears the text box
        self.gambit.check_for_true()                                                      #Calls the check_for_true method in the Gambit class

def main():
    '''
    Calls the Gambit class which runs the game
    :return: None
    '''
    g = Gambit()

if __name__ == '__main__':
    main()
