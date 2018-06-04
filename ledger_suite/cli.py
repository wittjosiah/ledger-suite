import click
import datetime
from async.CSVReader import CSVReader
from parse.TDCSVParser import TDCSVParser
from ledger.Ledger import Ledger
from interface.AddEntriesInterface import draw
from curses import wrapper


@click.command()
@click.argument('command', default='parse', required=False)
@click.argument('csv_file', type=click.Path('r'), required=False)
@click.argument('ledger', type=click.Path('r'), required=False)
def main(command, csv_file, ledger):
    """Tools for Ledger-CLI"""
    click.echo('{0}, {1}.'.format(csv_file, command))
    data = parseCsv(csv_file)
    l = Ledger.parse(ledger)
    l.entries.sort(key=lambda x:  datetime.datetime.strptime(x.date, '%Y/%m/%d'))
    wrapper(draw, data, l)


def parseCsv(csv_file):
    csvReader = CSVReader()
    tdCsvParser = TDCSVParser('Assets:TD Visa')
    csvData = csvReader.fetch(csv_file, tdCsvParser.fields())
    ledgerData = tdCsvParser.parseAll(csvData)
    return ledgerData

if __name__ == '__main__':
    main()
