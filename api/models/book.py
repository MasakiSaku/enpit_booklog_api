from api.database import db, ma
from sqlalchemy import Column, String, Integer, BigInteger

class Book(db.Model):
    __tablename__ = 'book'
    isbn = Column(BigInteger, primary_key=True)
    place = Column(String)

    def __repr__(self):
        return "Book<{}, {}>".format(self.id, self.isbn)

    def getBookList():

        book_list = db.session.query(Book).all()

        return book_list

    def insert_book(isbn,place):
        book = Book(isbn = int(isbn), place = place)
        db.session.add(book)
        db.session.commit()
        return 'success'

    def delete_book(isbn):
        db.session.query(Book).filter(Book.isbn == isbn).delete()
        db.session.commit()


#json変換用
class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book