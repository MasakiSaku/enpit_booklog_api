import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

engine = create_engine('postgresql://hogehoge:hogehoge@localhost:5432/test_db')#"postgresql://ユーザー名:パスワード@localhost:ポート/データベース名"で指定
Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(Integer)

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

#本のリストを返す
@app.route('/get/all_list', methods=["GET"])
def all_list():
    entries = session.query(Book).all()
    entries_schema = EntrySchema(many=True)
    return jsonify({'entries': entries_schema.dump(entries)})
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))