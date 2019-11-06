from api.database import db, ma
from sqlalchemy import Column, String, Integer, BigInteger

class BookShelf(db.Model):
    __tablename__ = 'bookshelf'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return "BookShelf<{}, {}>".format(self.id, self.name)

    def getBookShelfList():

        bookshelf_list = db.session.query(BookShelf).all()
        
        return bookshelf_list

    def insert_bookshelf(name):
        bookshelf = BookShelf(name = name)
        db.session.add(bookshelf)
        db.session.commit()
        return 'success'

    def edit_bookshelf(id, name):
        editbook = db.session.query(BookShelf).filter(BookShelf.id == id).first()
        editbook.name = name
        db.session.commit()

    def delete_bookshelf(id):
        db.session.query(BookShelf).filter(BookShelf.id == id).delete()
        db.session.commit()


#json変換用
class BookShelfSchema(ma.ModelSchema):
    class Meta:
        model = BookShelf