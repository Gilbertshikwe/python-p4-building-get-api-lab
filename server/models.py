from datetime import datetime
from flask_sqlalchemy import SQLAlchemy #type:ignore
from sqlalchemy import MetaData #type:ignore
from sqlalchemy_serializer import SerializerMixin #type:ignore

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    baked_goods = db.relationship('BakedGood', backref='bakery', lazy='dynamic')

class BakedGood(db.Model):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)