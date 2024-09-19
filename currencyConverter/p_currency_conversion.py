from currency_converter import CurrencyConverter

cc = CurrencyConverter()

amount = float(input("amount:"))
from_currency = input('from:').upper()
to_currency = input("to:").upper()

converted_amount = cc.convert(amount, from_currency, to_currency)
print(amount, from_currency, "is equivalent to", converted_amount, to_currency)

