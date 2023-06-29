from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Endpoint to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to get a specific book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Endpoint to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Endpoint to delete a book by ID
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
