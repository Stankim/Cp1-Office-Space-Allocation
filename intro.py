import os
import sys
import time
import click
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

def intro_dojo():
    os.system('clear')
    with click.progressbar(range(20000),
                           label=click.secho(
            '\t\t\tLOADING DOJO....',
                           blink=True, bold=True),
                           fill_char=click.style('  ', bg='cyan')) as prog_bar:
        for i in prog_bar:
            pass
    click.secho("   ")        
    time.sleep(0.6)
    click.secho('=' * 75, fg='yellow')
    click.secho("   ")
    init(strip=not sys.stdout.isatty())  
    cprint(figlet_format('Dojo', font='roman'),
           'cyan', attrs=['bold'])
    click.secho('=' * 75, fg='yellow')
    click.secho("   ")
    intro = click.secho('Welcome to the Dojo office allocation!' \
    + ' (type help for a list of commands.)',bold=True, fg='green')
    click.secho("   ")
