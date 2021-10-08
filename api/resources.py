from flask_restful import Resource, reqparse
from flask import request
from .currency_dao import CurrencyDAO
import api.currency_crud as repo


class ConverterResource(Resource):

    def __init__(self):
        self.req_parse = reqparse.RequestParser()
        self.req_parse.add_argument('from', required=True, type=str, location=('json', 'values'))
        self.req_parse.add_argument('to', required=True, type=str, location=('json', 'values'))
        self.req_parse.add_argument('value', required=True, type=float, location=('json', 'values'))
        super(ConverterResource, self).__init__()

    def get(self):
        args = self.req_parse.parse_args()
        arg_from = args['from']
        arg_to = args['to']
        arg_value = args['value']
        cur_from = repo.get_currency_by_code(arg_from)
        cur_to = repo.get_currency_by_code(arg_to)
        converter_result = (cur_from.rate / cur_to.rate) * arg_value
        return {"from": {"char_code": arg_from, "rate": cur_from.rate},
                "to": {"char_code": arg_to, "rate": cur_to.rate}, "value": arg_value, "result": converter_result}


class CurrencyResource(Resource):

    def __init__(self):
        self.req_parse = reqparse.RequestParser()
        self.req_parse.add_argument('char_code', required=True, type=str, location=('json', 'values'))
        self.req_parse.add_argument('currency', required=True, type=str, location=('json', 'values'))
        self.req_parse.add_argument('rate', required=True, type=float, location=('json', 'values'))
        super(CurrencyResource, self).__init__()

    def post(self):
        args = self.req_parse.parse_args()
        if repo.is_char_code_unique(args['char_code']):
            new_currency = repo.create_currency(args['char_code'], args['currency'], args['rate'])
            return CurrencyDAO(new_currency.char_code, new_currency.currency, new_currency.rate).__dict__
        else:
            raise ValueError('не уникальный буквенный код')

    def get(self):
        if request.args.get('char_code') is None:
            list_currency = [CurrencyDAO(cur.char_code, cur.currency, cur.rate).__dict__
                             for cur in repo.get_all_currency()]
            return list_currency
        else:
            cur_by_code = repo.get_currency_by_code(request.args.get('char_code'))
            return CurrencyDAO(cur_by_code.char_code, cur_by_code.currency, cur_by_code.rate).__dict__

    def put(self):
        args = self.req_parse.parse_args()
        if not repo.is_char_code_unique(args['char_code']):
            upd_currency = repo.update_currency(args['char_code'], currency=args['currency'], rate=args['rate'])
            return CurrencyDAO(upd_currency.char_code, upd_currency.currency, upd_currency.rate).__dict__
        else:
            raise ValueError('новый буквенный код. нужен post')

    def delete(self):
        ch_cd = request.args.get('char_code')
        if not repo.is_char_code_unique(ch_cd):
            repo.delete_currency(ch_cd)
            return {"message": "Done"}, 200
        else:
            raise ValueError('неизвестный буквенный код')
