import curses
import datetime
import bisect
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
    # ledger.entries.sort(key=lambda x:  datetime.datetime.strptime(x.date, '%Y/%m/%d'))

    stdscr.addstr(0, int(width/2), 'Ledger Suite', curses.color_pair(1))



    # Construct new array of existing ledger entries plus the new pending entries
    # Use a tuple with a boolean or something to denote the new entries that need to be processed
    toProcess = list(map(lambda e: (e, True), ledger.entries))
    toProcess.extend(list(map(lambda e: (e, False), transactions)))
    toProcess.sort(key=lambda xt: xt[0].date)


    # For each new transaction
    # draw the 3? surrounding ledger entries
    # y_pos=4
    # for i, entry in enumerate(transactions):
    #     j = max(max([i for i, s in enumerate(ledger.entries) if entry.date == s.date], [-1]))
    #     first = ledger.entries[j]
    #     t_size = len(entry.amounts)+2
    #     first_size = len(first.amounts)+2
    #     if y_pos <= height-t_size-5:
    #         # Ledger entry above
    #         stdscr.addstr(y_pos, 0, str(first), curses.color_pair(2))
    #         # New entry
    #         stdscr.addstr(y_pos+first_size, 0, str(entry), curses.color_pair(1))
    #         # Ledger entry below
    #         # stdscr.addstr(y_pos+6, 0, str(entry), curses.color_pair(1))

    #     y_pos = y_pos + first_size + t_size



    # SCENARIOS
    # Empty ledger
      # Show sorted unprocessed list
    #

    y_pos=4
    for i, entryBool in enumerate(toProcess):
        if (entryBool[1] == True):
            continue
        else:
            entry = entryBool[0]
            # Jump to next unprocessed
            prevBool = toProcess[i-1]
            prev = prevBool[0]
            prev_size = len(prev.amounts)+2
            t_size = len(entry.amounts)+2
            if y_pos <= height-t_size-5:
                # Ledger entry above
                stdscr.addstr(y_pos, 0, str(prev), color(prevBool))
                # New entry
                stdscr.addstr(y_pos+prev_size, 0, str(entry), color(entryBool))
                # Ledger entries below
                y_pos_two = y_pos
                y = i
                en = toProcess[y+1][0]
                en_size = len(en.amounts)+2
                while (y_pos_two <= height - en_size - 5 and not toProcess[y+1]):
                    en = toProcess[y+1][0]
                    en_size = len(en.amounts)+2
                    stdscr.addstr(y_pos_two+en_size, 0, str(en), color(toProcess[y+1]))
                    y+=1;
                    y_pos_two = y_pos_two + en_size
                y_pos = y_pos + prev_size + t_size
            stdscr.refresh()
            stdscr.getkey()


    statusbarstr = "Press 'y' to accept | Height: {}, Width: {} | {} entries | {}".format(height, width, len(ledger.entries), i)


    # Render status bar
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height-1, 0, statusbarstr)

    stdscr.refresh()
    stdscr.getkey()

def color(transaction):
    if (transaction[1] == True):
        return curses.color_pair(2)
    else:
        return curses.color_pair(1)
