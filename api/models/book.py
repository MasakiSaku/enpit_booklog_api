from api.database import db, ma
from sqlalchemy import Column, String, Integer, BigInteger

class Book(db.Model):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    place_id = Column(Integer)

    def __repr__(self):
        return "Book<{}, {}, {}>".format(self.id, self.title, self.place_id)

    def getBookList():

        book_list = db.session.query(Book).all()
        
        return book_list

    def insert_book(title,place_id):
        book = Book(title = title, place_id = int(place_id))
        db.session.add(book)
        db.session.commit()
        return 'success'

    def edit_book(id, title, place_id):
        editbook = db.session.query(Book).filter(Book.id == id).first()
        editbook.title = title
        editbook.place_id = place_id
        db.session.commit()

    def delete_book(id):
        db.session.query(Book).filter(Book.id == id).delete()
        db.session.commit()


#json変換用
class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book