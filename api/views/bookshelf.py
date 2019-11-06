from flask import Blueprint, request, jsonify
from api.models import BookShelf, BookShelfSchema
import json

# ルーティング設定
bookshelf_router = Blueprint('bookshelf_router', __name__)


#本棚の一覧
@bookshelf_router.route('/bookshelfs', methods=["GET"])
def bookshelf_list():
    bookshelfs = BookShelf.getBookShelfList()
    bookshelf_schema = BookShelfSchema(many=True)
    return jsonify({'entries': bookshelf_schema.dump(bookshelfs)})


#本棚の登録
@bookshelf_router.route('/bookshelfs', methods=["POST"])
def insert_bookshelf():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    name = data['name']
    BookShelf.insert_bookshelf(name)
    return 'success'

#本棚の編集
@bookshelf_router.route('/bookshelfs/<int:id>', methods=["PATCH"])
def edit_bookshelf(id):
    data = request.data.decode('utf-8')
    data = json.loads(data)
    name = data['name']
    BookShelf.edit_bookshelf(id, name)
    return 'success'

#本棚の削除
@bookshelf_router.route('/bookshelfs/<int:id>', methods=["DELETE"])
def delete_bookshelf(id):
    BookShelf.delete_bookshelf(id)
    return ''