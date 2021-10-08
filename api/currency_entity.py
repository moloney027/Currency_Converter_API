from pymodm import fields, MongoModel


class Currency(MongoModel):
    char_code = fields.CharField(required=True)
    currency = fields.CharField(required=True)
    rate = fields.FloatField(required=True)
