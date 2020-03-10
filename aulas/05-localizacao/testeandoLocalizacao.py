import babel
from babel.numbers import format_number, format_decimal, format_percent
from datetime import date
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time
import gettext
gettext.install('cli', localedir='locale')

if __name__ == '__main__':
    today = date.today()
    print(format_date(today, format='full'))
    number = 240000000000.32212
    print(format_number(1099))
    name = input(_('Input your name: '))
    print(_('Hello {}').format(name))