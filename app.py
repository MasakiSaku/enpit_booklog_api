import os
from sqlalchemy import create_engine, Column, String, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

db_url = os.environ.get('DATABASE_URL') or "postgresql://hogehoge:hogehoge@localhost:5432/test_db"
engine = create_engine(db_url)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    isbn = Column(BigInteger, primary_key=True)
    place = Column(String)

    def __repr__(self):
        return "Book<{}, {}>".format(self.id, self.isbn)

#json変換用
class EntrySchema(ma.ModelSchema):
    class Meta:
        model = Book

Base.metadata.create_all(engine)
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

@app.route('/')
def hello_world():
    return 'BookLogAPIへようこそ'

#POSTされたisbnを返す（テスト用）
@app.route('/request_test', methods=["POST"])
def request_test():
    isbn, place = request.form.get('isbn'), request.form.get('place')
    return f'isbn :{isbn}, place :{place}\n'

#本の一覧
@app.route('/books', methods=["GET"])
def book_list():
    entries = session.query(Book).all()
    entries_schema = EntrySchema(many=True)
    return jsonify({'entries': entries_schema.dump(entries)})

#本の登録
@app.route('/books', methods=["POST"])
def insert_book():
    isbn, place = request.form.get('isbn'), request.form.get('place')
    book = Book(isbn = int(isbn), place = place)
    session.add(book)
    session.commit()
    return 'success',201

#本の削除
@app.route('/books/<int:isbn>', methods=["DELETE"])
def delete_book(isbn):
    session.query(Book).filter(Book.isbn == isbn).delete()
    session.commit()
    return '',204

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))