from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        'name': "mystore",
        'items': [
            {'name': 'pen', 'price': 20}
        ]
    }
]


# post - used to recieve data
# get - to send data
@app.route("/")
def home():
    return render_template("index.html")


# post /store data: {name:}
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'],
                 'items': []}
    stores.append(new_store)
    return jsonify(new_store)


# get /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for s in stores:
        if s['name'] == name:
            return jsonify(s)
    else:
        return jsonify({"error": "could not find store"})


# get store
@app.route("/store")
def store():
    return jsonify({'stores': stores})


# post /store/<string:name>/item {name:,price:}
@app.route("/store/<string:store_name>/item", methods=['POST'])
def add_item(store_name):
    req_data = request.get_json()
    for s in stores:
        if s['name'] == store_name:
            new_item = {'name': req_data['name'],
                        'price': req_data['price']}
            s['items'].append(req_data)
            return jsonify(new_item)
    return jsonify({'error': 'no store'})


# get /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item(name):
    for s in stores:
        if s['name'] == name:
            return jsonify(s['items'])
    return jsonify({'error': "empty store"})


app.run(port=5000)

# HTTP verbs = GET,POST,PUT,DELETE

# REST Principles

# Stateless ? One request does not depend on other request.
