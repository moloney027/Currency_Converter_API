from pymodm import connect

connect('mongodb://root:pass@test_mongodb:27017/exchange_rates?authSource=admin')
