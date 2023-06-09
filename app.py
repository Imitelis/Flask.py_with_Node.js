from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my Flask server!'

@app.route('/flask', methods=['GET'])
def index():
    return "Flask server"

if __name__ == "__main__":
    app.run(port=5000, debug=True)