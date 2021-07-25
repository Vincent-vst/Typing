import curses 
import time 
import random 
import sqlite3 
from datetime import date 
import sys
import os

def randomPangram() -> str : 
    line = open('assets/pangram.txt').read().splitlines()
    return random.choice(line)

typing_text = randomPangram() 


def addToDatabase(accuracy, wpm, date) : 
    try :
        connection = sqlite3.connect('assets/statsForNerds')
        cursor = connection.cursor()
        cursor.execute(f"insert into logs values({accuracy}, {wpm}, '{date}')")
        cursor.execute('commit')
    except Exception as e :
        print(e)



def main(stdscr) : 
    
    curses.start_color()
    curses.use_default_colors()

    curses.curs_set(0)

    # get screen size in order to center the text 
    rows, cols = stdscr.getmaxyx()
    center_x = int(rows/2)
    center_y = int(cols/2)

    # Set the color-pair (-1 is for having no background)
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    # Print the line in blue
    stdscr.addstr(1,int((cols - len(typing_text))/2),typing_text, curses.color_pair(5))
    # Print the line in grey
    stdscr.addstr(2,int((cols - len(typing_text))/2),typing_text + "\n", curses.color_pair(244))
   
    
    # User input    
    start = time.time()
    mistakes = 0 
    for i in range(len(typing_text)) : 
  
        choice = stdscr.getkey()
        if (choice == typing_text[i]) : 
            stdscr.addstr(2,int((cols - len(typing_text))/2) + i ,choice)
            curses.curs_set(1)
        else :
            mistakes += 1
            stdscr.addstr(2,int((cols - len(typing_text))/2) + i,choice, curses.color_pair(2))
            curses.curs_set(1)
    end = time.time()
    
    # Print the time 
    typing_time = "Time : " + str(round(end-start,2)) + "s"
    stdscr.addstr(4,int((cols - len(typing_time))/2),typing_time, curses.color_pair(12))

    # Print the typing speed
    wpm = "WPM : " + str(round(len(typing_text.split()) / ((end-start)/60),2)) + " wpm"
    stdscr.addstr(5,int((cols - len (wpm))/2), wpm, curses.color_pair(12))

    # Print the accuracy 
    accuracy = "Accuracy : " + str(round(100 - ((mistakes*100)/len(typing_text)),2)) + "%"
    stdscr.addstr(6,int((cols - len(accuracy))/2), accuracy , curses.color_pair(12)) 

    # Add the stats to the database (in assets/statsForNerds)    
    today = date.today().strftime("%d/%m/%Y")
    addToDatabase(round(100 - ((mistakes*100)/len(typing_text)),2), round(len(typing_text.split()) / ((end-start)/60),2), str(today))

    # Ask if it wants to play again...
    end_choice = "[p] : Play again | [qq] : Quit "
    stdscr.addstr(7,int((cols - len(end_choice))/2), end_choice, curses.color_pair(5))
    
    user_end_choice = stdscr.getkey()
    
    if user_end_choice == 'p' : 
        # sys.exit(0)
        os.system('python main.py') 
        # curses.wrapper(main)
    else : 
        while user_end_choice != 'q' : 
            user_end_choice = stdscr.getkey() 
        stdscr.getch()
        # sys.exit(0)        

if __name__ == "__main__" : 
    curses.wrapper(main)


