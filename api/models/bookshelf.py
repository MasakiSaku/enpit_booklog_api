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

    def insert_bookshelf(id, name):
        bookshelf = BookShelf(id = id, name = name)
        db.session.add(bookshelf)
        db.session.commit()
        return 'success'

    def delete_bookshelf(id):
        db.session.query(BookShelf).filter(BookShelf.id == id).delete()
        db.session.commit()


#json変換用
class BookShelfSchema(ma.ModelSchema):
    class Meta:
        model = BookShelf