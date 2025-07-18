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
@app.route('/products')
def load_json_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def load_csv_data(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products = load_json_data('products.json')
    else:
        # Convertir les prix de string à float pour CSV
        products = load_csv_data('products.csv')
        if products:
            for product in products:
                product['price'] = float(product['price'])

    if products is None:
        return render_template('product_display.html', error="Failed to read data")

    if product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if int(product['id']) == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    return render_template('product_display.html', products=products)
app.run(debug=True, port=5000)