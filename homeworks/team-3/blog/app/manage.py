import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from blog import blog, db

blog.config.from_object(os.environ['APP_SETTINGS'])
import post
import comment

migrate = Migrate(blog, db)
manager = Manager(blog)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
