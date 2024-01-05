# app/routes.py
from flask import render_template, request
from ipaddress import IPv4Network, AddressValueError
from app import app

# Sample data
csv_file_path = 'data/sample_data.csv'

def read_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines]

ip_addresses = read_csv(csv_file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    print("Received POST request") 
    print(request.form)
    query = request.form.get('search_query')

    
    if '/' in query:
        try:
            search_network = IPv4Network(query, strict=False)
        except AddressValueError as e:
            print(f"Error: {e}")
            return render_template('results.html', results=[])
    else:
        
        results = [entry for entry in ip_addresses if query.lower() in entry[1].lower() or query.lower() in entry[2].lower()]
        return render_template('results.html', results=results)

    
    results = []
    for entry in ip_addresses:
        try:
            entry_network = IPv4Network(entry[0], strict=False)
            if entry_network == search_network or entry_network.subnet_of(search_network):
                results.append(entry)
            elif query.lower() in entry[1].lower() or query.lower() in entry[2].lower():
                results.append(entry)
        except AddressValueError as e:
            print(f"Error: {e} in entry: {entry}")

    return render_template('results.html', results=results)
