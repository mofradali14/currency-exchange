from flask import Flask, render_template, request, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
from converter import ForexConvert
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "currency"
# debug = DebugToolbarExtension(app)
forex_convert = ForexConvert()

CURR = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF',
        'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']


@app.route('/')
def index_form():
    convert_from = request.form.get('convert-from')
    convert_to = request.form.get('convert-to')
    amount = request.form.get('amount')
    return render_template('index.html', convert_from=convert_from, convert_to=convert_to, amount=amount)


@app.route('/result', methods=["POST"])
def result():
    convert_from = request.form.get('convert-from')
    convert_to = request.form.get('convert-to')
    amount = request.form.get('amount')
    convert_from = convert_from.upper()
    convert_to = convert_to.upper()

    if convert_from not in CURR:
        flash(f"Invalid currency code {convert_from}")
        return redirect('/')
    elif convert_to not in CURR:
        flash(f"Invalid currency code {convert_to}")
        return redirect('/')
    elif float(amount) <= 0:
        flash('Invalid amount')
        return redirect('/')
    res = forex_convert.response(convert_from, convert_to, float(amount))

    return render_template('result.html', res=res)
