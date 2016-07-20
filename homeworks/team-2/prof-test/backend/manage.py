import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import Base

migrate = Migrate(app, Base)
manager = Manager(app)

manager.add_command('Base', MigrateCommand)

if __name__ == '__main__':
    manager.run()
