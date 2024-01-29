from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)#创建一个Flask应用程序实例，——name__是Python预定义变量，它被设置为使用本模块的模块名
app.debug=True#启用调试模式，这样可以在代码修改后自动重新加载
app.config['SECRET_KEY'] = 'your-secret-key'#设置一个密钥，以便我们可以使用Flask-WTF扩展来防止跨站点请求伪造
login=LoginManager(app)
login.login_view = 'login'
#login.login_view = 'login'告诉Flask-Login登录视图的函数是哪个，
#如果用户访问未登录用户才能访问的页面，那么Flask-Login会闪现一条消息并重定向到登录视图
#视图函数login在app/routes.py中定义，因此在这里使用字符串'login'引用它
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
#此处的app.db是数据库文件的名称，它将保存在应用程序的主目录中


db=SQLAlchemy(app)
migrate=Migrate(app,db)
#数据库实例db和迁移引擎migrate
from app import routes,models

