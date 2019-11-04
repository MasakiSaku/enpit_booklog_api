from flask import Blueprint, request, jsonify
from api.models import Book, BookSchema
import json

# ルーティング設定
book_router = Blueprint('book_router', __name__)


@book_router.route('/')
def hello_world():
    return 'BookLogAPIへようこそ'

#POSTされたtitleを返す（テスト用）
@book_router.route('/request_test', methods=["POST"])
def request_test():
    title, place_id = request.form.get('title'), request.form.get('place_id')
    return f'title :{title}, place_id :{place_id}\n'


#本の一覧
@book_router.route('/books', methods=["GET"])
def book_list():
    books = Book.getBookList()
    book_schema = BookSchema(many=True)
    return jsonify({'entries': book_schema.dump(books)})


#本の登録
@book_router.route('/books', methods=["POST"])
def insert_book():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    title, place_id = data['title'], data['place_id']
    Book.insert_book(title,place_id)
    return 'success'

#本の編集
@book_router.route('/books/<int:id>', methods=["PATCH"])
def edit_book(id):
    data = request.data.decode('utf-8')
    data = json.loads(data)
    title, place_id = data['title'], data['place_id']
    Book.edit_book(id, title, place_id)
    return 'success'


#本の削除
@book_router.route('/books/<int:id>', methods=["DELETE"])
def delete_book(id):
    Book.delete_book(id)
    return ''