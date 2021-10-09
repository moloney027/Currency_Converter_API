from .currency_entity import Currency


class CurrencyDao:
    def __init__(self, char_code, currency, rate):
        self.char_code = char_code
        self.currency = currency
        self.rate = rate
