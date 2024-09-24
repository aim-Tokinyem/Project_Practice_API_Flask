from flask import Flask, render_template, request
from Currency_API.get_currency import get_currency_value

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/currencyGet", methods=['GET'])
def currencyGet():
    choice1 = request.args.get('choice1')
    choice2 = request.args.get('choice2')

    result = get_currency_value(choice1, choice2)
    print(result)
    return result


if __name__ == "__main__":
    app.run(debug=True)