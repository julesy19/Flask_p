
++++---
p^Éfrom flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>'
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Martaux', 'barcode': '231985128446', 'price': 150},
        {'id': 4, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 5, 'name': 'polk', 'barcode': '231985128446', 'price': 950},
        {'id': 6, 'name': 'Molfd', 'barcode': '231985128446', 'price': 650},
        {'id': 7, 'name': 'Pboard', 'barcode': '231985128446', 'price': 21150},
        {'id': 8, 'name': 'doc', 'barcode': '231985128446', 'price': 2350}
        ]
    return render_template('market.html', items=items)


if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=8080,host='0.0.0.0')