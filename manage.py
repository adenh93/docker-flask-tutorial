import os
from webapp import db, migrate, create_app
from webapp.blog.models import Post, Tag
from webapp.auth.models import User, Role

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Tag=Tag, Role=Role, migrate=migrate)
