import curses
import datetime
from click import open_file

def draw(stdscr, transactions, ledger):
    # Clear screen
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    cursor_x = 0
    cursor_y = 0

    # Color pair for new entry
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Color pair for existing entry
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # Color pair for status bar
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)


    # Sort ledger
    ledger.entries.sort(key=lambda x:  datetime.datetime.strptime(x.date, '%Y/%m/%d'))

    stdscr.addstr(0, int(width/2), 'Ledger Suite', curses.color_pair(1))

    statusbarstr = "Press 'y' to accept | Height: {}, Width: {} | {} entries".format(height, width, len(ledger.entries))

    # Render status bar
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height-1, 0, statusbarstr)


    # For each new transaction
    # draw the 3? surrounding ledger entries
    y_pos=4
    for i, entry in enumerate(transactions):
        j = max(max([i for i, s in enumerate(ledger.entries) if entry.date == s.date], [-1]))
        first = ledger.entries[j]
        t_size = len(entry.amounts)+2
        first_size = len(first.amounts)+2
        if y_pos <= height-t_size-5:
            # Ledger entry above
            stdscr.addstr(y_pos, 0, str(first), curses.color_pair(2))
            # New entry
            stdscr.addstr(y_pos+first_size, 0, str(entry), curses.color_pair(1))
            # Ledger entry below
            # stdscr.addstr(y_pos+6, 0, str(entry), curses.color_pair(1))

        y_pos = y_pos + first_size + t_size

    stdscr.refresh()
    stdscr.getkey()
