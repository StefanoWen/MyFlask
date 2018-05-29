from flask_script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command("runserver",
                    Server(host="127.0.0.1", port=8080, use_debugger=True))

if __name__ == '__main__':
    # app.run(port=8080)
    manager.run()
