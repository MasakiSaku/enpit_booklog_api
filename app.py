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

engine = create_engine('postgresql://hogehoge:hogehoge@localhost:5432/test_db')#"postgresql://ユーザー名:パスワード@アドレス:ポート/データベース名"で指定
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

#本のリストを返す
@app.route('/get/all_list', methods=["GET"])
def all_list():
    entries = session.query(Book).all()
    entries_schema = EntrySchema(many=True)
    return jsonify({'entries': entries_schema.dump(entries)})

#本の登録
@app.route('/post/insert_book', methods=["POST"])
def insert_book():
    isbn, place = request.form.get('isbn'), request.form.get('place')
    book = Book(isbn = int(isbn), place = place)
    session.add(book)
    session.commit()
    return 'success'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))