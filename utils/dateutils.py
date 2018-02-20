# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import calendar


def numer_of_days(start, end):
    delta = end - start
    return delta.days


def parse_date(date_string):
    if len(date_string) == 10:
        fmt = '%d/%m/%Y'
    else:
        fmt = '%d/%m/%Y %H:%M:%S'
    return datetime.datetime.strptime(date_string, fmt)


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12)
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def add_days(sourcedate, days):
    return sourcedate + datetime.timedelta(days=days)


def pretty_date(d):
    diff = datetime.datetime.now() - d
    s = diff.seconds
    if diff.days > 365 or diff.days < 0:
        return d.strftime('%d %b %y')
    elif 60 > diff.days > 30:
        return '1 mês atrás'
    elif diff.days > 60:
        return '{} meses atrás'.format(diff.days/30)
    elif diff.days == 1:
        return '1 dia atrás'
    elif diff.days > 1:
        return '{} dias atrás'.format(diff.days)
    elif s <= 1:
        return 'agora'
    elif s < 60:
        return '{} segundos atrás'.format(s)
    elif s < 120:
        return '1 minuto atrás'
    elif s < 3600:
        return '{} minutos atrás'.format(s/60)
    elif s < 7200:
        return '1 hora atrás'
    else:
        return '{} horas atrás'.format(s/3600)