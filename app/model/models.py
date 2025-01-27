from app.infra.db import db

class User(db.Model):
    __tablename__ = 'tb_users'

    id = db.Column(db.Integer, primary_key=True)
    google_resource_name = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    display_name = db.Column(db.String(80), nullable=False)
    token = db.Column(db.String(1024), nullable=False)
    bookmark_contact = db.relationship('BookmarkContacts', backref='bookmark_contacts')

class BookmarkContacts(db.Model):
    __tablename__ = 'tb_bookmark_contacts'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('tb_users.id'))
    email = db.Column(db.String(80), nullable=False)
