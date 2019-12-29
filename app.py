from flask import Flask

app = Flask(__name__)


@app.route('/get-hello-world-msg')
def get_hello_world_msg():
    return 'Hello World'


app.run(port=5000)
