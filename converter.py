from forex_python.converter import CurrencyRates, CurrencyCodes


class ForexConvert():

    def response(self, convert_from, convert_to, amount):
        c = CurrencyRates()
        code = CurrencyCodes()
        # convert_from = convert_from.upper()
        # convert_to = convert_to.upper()
        converted = c.convert(convert_from, convert_to, float(amount))
        symbol = code.get_symbol(convert_to)
        resp = symbol + str(converted)
        return resp
