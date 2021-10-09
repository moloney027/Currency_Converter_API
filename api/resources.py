from flask_restful import Resource, reqparse
from flask import request
from .currency_dao import CurrencyDao
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
        return {"from": arg_from, "to": arg_to, "value": arg_value, "result": converter_result}


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
            return CurrencyDao(new_currency.char_code, new_currency.currency, new_currency.rate).__dict__
        else:
            raise RuntimeError("an object with this char_code already exists: '{}'".format(args['char_code']))

    def get(self):
        if request.args.get('char_code') is None:
            list_currency = [CurrencyDao(cur.char_code, cur.currency, cur.rate).__dict__
                             for cur in repo.get_all_currency()]
            return list_currency
        else:
            cur_by_code = repo.get_currency_by_code(request.args.get('char_code'))
            return CurrencyDao(cur_by_code.char_code, cur_by_code.currency, cur_by_code.rate).__dict__

    def put(self):
        args = self.req_parse.parse_args()
        if not repo.is_char_code_unique(args['char_code']):
            upd_currency = repo.update_currency(args['char_code'], currency=args['currency'], rate=args['rate'])
            return CurrencyDao(upd_currency.char_code, upd_currency.currency, upd_currency.rate).__dict__
        else:
            raise RuntimeError("an object with this char_code does not exist: '{}'".format(args['char_code']))

    def delete(self):
        ch_cd = request.args.get('char_code')
        if not repo.is_char_code_unique(ch_cd):
            repo.delete_currency(ch_cd)
            return {"message": "Done"}, 200
        else:
            raise ValueError("an object with this char_code does not exist: '{}'".format(ch_cd))
