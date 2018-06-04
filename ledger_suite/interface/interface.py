import curses
import AddEntriesInterface

from curses import wrapper
from AddEntriesInterface import draw
from ledger_suite.ledger.Transaction import Transaction

def main():
    wrapper(draw, [], [])

if __name__ == "__main__":
    main()
