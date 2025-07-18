from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/items')
def item():
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)
@app.route('/product_display')
def product_display():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            # Lire et charger les données JSON
            with open('products.json', 'r') as file:
                products = json.load(file)
        else:
            # Lire et charger les données CSV
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = list(reader)
                # Convertir les valeurs de prix de CSV string en float et id en int
                for product in products:
                    product['price'] = float(product['price'])
                    product['id'] = int(product['id'])

        if product_id:
            try:
                product_id = int(product_id)
                products = [product for product in products if product['id'] == product_id]
                if not products:
                    return render_template('product_display.html', error="Product not found")
            except ValueError:
                return render_template('product_display.html', error="Invalid ID format")

        return render_template('product_display.html', products=products)

    except FileNotFoundError:
        return render_template('product_display.html', error="File not found")
    except Exception as e:
        return render_template('product_display.html', error=f"An error occurred: {str(e)}")

    app.run(debug=True, port=5000)