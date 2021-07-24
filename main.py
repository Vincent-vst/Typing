import curses 
import time 

typing_text = 'The quick brown fox jumps over the lazy dog'


def main(stdscr) : 
    curses.start_color()
    curses.use_default_colors()
 
    # get screen size in order to center the text 
    rows, cols = stdscr.getmaxyx()
    center_x = int(rows/2)
    center_y = int(cols/2)

    # Set the color-pair (-1 is for having no background)
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    # Print the line in red 
    stdscr.addstr(1,int((cols - len(typing_text))/2),typing_text, curses.color_pair(5))
    # Print the line in grey
    stdscr.addstr(2,int((cols - len(typing_text))/2),typing_text, curses.color_pair(244))
   
    
    # User input    
    start = time.time()
    mistakes = 0 
    for i in range(len(typing_text)) : 
        
        choice = stdscr.getkey()
        if (choice == typing_text[i]) : 
            stdscr.addstr(2,int((cols - len(typing_text))/2) + i ,choice)
        else :
            mistakes += 1
            stdscr.addstr(2,int((cols - len(typing_text))/2) + i,choice, curses.color_pair(2))
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

    stdscr.getch()

if __name__ == "__main__" : 
    curses.wrapper(main)



