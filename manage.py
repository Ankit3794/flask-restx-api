from flask_script import Manager
from main import create_app
import os

app = create_app(os.getenv('CONFIG_NAME', 'dev'))
manager = Manager(app)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
