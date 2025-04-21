from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Create Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Import your custom backend logic
from add_book import add_book
from delete_book import delete_book
from search_book import search_book
from show_books import show_books
from update_book import update_book

from add_user import add_user
from delete_user import delete_user
from search_user import search_user
from show_users import show_users
from update_user import update_user

from borrow import borrow_book
from return_ import return_book
from show_borrow import show_borrow  # ✅ make sure this is defined in show_borrow.py

# ---------------- Book APIs ----------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_book', methods=['POST'])
def route_add_book():
    data = request.json.get('values', [])
    result = add_book(data)
    return jsonify(result)

@app.route('/delete_book', methods=['POST'])
def route_delete_book():
    data = request.json.get('values', [])
    result = delete_book(data)
    return jsonify(result)

@app.route('/search_book', methods=['POST'])
def route_search_book():
    data = request.json.get('values', [])
    result = search_book(data)
    return jsonify(result)

@app.route('/show_books', methods=['GET'])
def route_show_books():
    result = show_books()
    return jsonify(result)

@app.route('/update_book', methods=['POST'])
def route_update_book():
    data = request.json.get('values', [])
    result = update_book(data)
    return jsonify(result)

# ---------------- User APIs ----------------
@app.route('/add_user', methods=['POST'])
def route_add_user():
    data = request.json.get('values', [])
    result = add_user(data)
    return jsonify(result)

@app.route('/delete_user', methods=['POST'])
def route_delete_user():
    data = request.json.get('values', [])
    result = delete_user(data)
    return jsonify(result)

@app.route('/search_user', methods=['POST'])
def route_search_user():
    data = request.json.get('values', [])
    result = search_user(data)
    return jsonify(result)

@app.route('/show_users', methods=['GET'])
def route_show_users():
    result = show_users()
    return jsonify(result)

@app.route('/update_user', methods=['POST'])
def route_update_user():
    data = request.json.get('values', [])
    result = update_user(data)
    return jsonify(result)

# ---------------- Borrow / Return APIs ----------------
@app.route('/borrow', methods=['POST'])
def route_borrow_book():
    data = request.json.get('values', [])
    result = borrow_book(data)
    return jsonify(result)

@app.route('/return', methods=['POST'])
def route_return_book():
    data = request.json.get('values', [])
    result = return_book(data)
    return jsonify(result)

@app.route('/show_borrow', methods=['GET'])
def route_show_borrow():
    result = show_borrow()
    return jsonify(result)

# ---------------- Main ----------------
if __name__ == '__main__':
    app.run(debug=True)
