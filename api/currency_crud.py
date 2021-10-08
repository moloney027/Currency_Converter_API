from api.db_connection import *
from .currency_entity import Currency


def get_all_currency():
    return Currency.objects.all()


def get_currency_by_code(char_code):
    return Currency.objects.get({'char_code': char_code})


def create_currency(char_code, currency, rate):
    n_cur = Currency(char_code, currency, rate)
    n_cur.save()
    return n_cur


def delete_currency(char_code):
    result_del = get_currency_by_code(char_code)
    result_del.delete()


def update_currency(char_code, **param):
    if len(param.keys()) > 2:
        raise ValueError('слишком много параметров')
    for name, val in param.items():
        if name != 'currency' and name != 'rate':
            raise ValueError('неверное имя параметра')
        if name == 'currency' and type(val) != str:
            raise ValueError('неверный тип данных')
        if name == 'rate' and type(val) != float:
            raise ValueError('неверный тип данных')
    count_upd = Currency.objects.raw({'char_code': char_code}).update({'$set': param})
    if count_upd == 1:
        return get_currency_by_code(char_code)
    else:
        raise ValueError('неудалось обновить')


def is_char_code_unique(char_code):
    return Currency.objects.raw({"char_code": char_code}).count() == 0
