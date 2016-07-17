import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from blog import blog

db = SQLAlchemy(blog)

blog.config.from_object(os.environ['APP_SETTINGS'])
import post
import comment

migrate = Migrate(blog, db)
manager = Manager(blog)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
