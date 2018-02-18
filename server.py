#!flask/bin/python
from flask import Flask
from flask import abort
from flask import jsonify
from flask import request

server = Flask(__name__)


books = [
    {
        "id": 1,
        "title": "harry potter and the philosopher's stone",
        "author": "J. K. Rowling"
    },
    {
        "id": 2,
        "title": "Open society and its enemies",
        "author": "Karl Popper"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell"
    },
    {
        "id": 4,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen"
    },
]
@server.route('/')
def welcome():
    return "Welcome to my bookstore!"

@server.route('/hogwarts/api/v1.0/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@server.route('/hogwarts/api/v1.0/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({'book': book[0]})

@server.route('/hogwarts/api/v1.0/books', methods=['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }

    books.append(new_book)
    return jsonify({'books': books}), 201

if __name__ == '__main__':
    server.run(debug=True)

