
from flask import Flask

from views import query_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(query_blueprint)


if __name__ == "__main__":
    app.run()

