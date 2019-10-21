from flask import Blueprint, request, jsonify
from api.models import Book, BookSchema
import json

# ルーティング設定
book_router = Blueprint('book_router', __name__)


@book_router.route('/')
def hello_world():
    return 'BookLogAPIへようこそ'

#POSTされたisbnを返す（テスト用）
@book_router.route('/request_test', methods=["POST"])
def request_test():
    isbn, place = request.form.get('isbn'), request.form.get('place')
    return f'isbn :{isbn}, place :{place}\n'


#本の一覧
@book_router.route('/books', methods=["GET"])
def book_list():
    books = Book.getBookList()
    book_schema = BookSchema(many=True)
    return jsonify({'entries': book_schema.dump(books)})


#本の登録
@book_router.route('/books', methods=["POST"])
def insert_book():
    isbn, place = request.form.get('isbn'), request.form.get('place')
    Book.insert_book(isbn,place)
    return 'success'


#本の削除
@book_router.route('/books/<int:isbn>', methods=["DELETE"])
def delete_book(isbn):
    Book.delete_book(isbn)
    return ''