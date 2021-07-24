import curses 
import time 

typing_text = 'The quick brown fox jumps over the lazy dog'


def main(stdscr) : 
    curses.start_color()
    curses.use_default_colors()
    
    # Set the color-pair (-1 is for having no background)
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)

    # Print the line in red 
    stdscr.addstr(0,0,typing_text, curses.color_pair(5))
    # Print the line in grey
    stdscr.addstr(1,0,typing_text, curses.color_pair(244))
   
    
    # User input    
    start = time.time()
    mistakes = 0 
    for i in range(len(typing_text)) : 
        
        choice = stdscr.getkey()
        if (choice == typing_text[i]) : 
            stdscr.addstr(1,i,choice)
        else :
            mistakes += 1
            stdscr.addstr(1,i,choice, curses.color_pair(2))
    end = time.time()
    
    # Print the time 
    typing_time = "Time : " + str(end-start)[0:4] + " s"
    stdscr.addstr(3,0,typing_time, curses.color_pair(12))

    # Print the typing speed
    wpm = len(typing_text.split()) / ((end-start)/60)
    stdscr.addstr(4,0, "WPM : " + str(wpm)[0:4]+ " wpm", curses.color_pair(12))

    # Print the accuracy 
    stdscr.addstr(5,0, "Accuracy : " + str(100 - ((mistakes*100)/len(typing_text)))[0:4] + "%", curses.color_pair(12)) 

    stdscr.getch()

if __name__ == "__main__" : 
    curses.wrapper(main)


# TODO : 
# - add accuracy 
# - center everything 
# - maybe change some colors 
# - possible bug : using [0:4] it's not a good way to truncate the number. 
