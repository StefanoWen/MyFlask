from flask_script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command("runserver",
                    Server(host="0.0.0.0", port=8080, use_debugger=True))

if __name__ == '__main__':
    # app.run(port=8080)
    manager.run()
