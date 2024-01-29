from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from datetime import datetime, timezone

@login.user_loader
def load_user(id):
        return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me: so.Mapped[Optional[str]] = so.mapped_column(sa.String(140))
    from datetime import datetime, timezone
    # Import the datetime module

    last_seen: so.Mapped[Optional[datetime]] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc))
    def avatar(self, size):
        digest=md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest,size)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)
    #__repr是一个类方法，它返回一个可读性的字符串表示模型，可在调试和测试时使用，也可用于生成日志。
    #__repr__方法告诉Python如何打印对象，而__str__方法则告诉Python如何将对象转换为字符串。

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)
