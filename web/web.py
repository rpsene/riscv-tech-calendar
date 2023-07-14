from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def homepage():
    # HTML file is named 'index.html' and 
    # located in a directory named 'static' 
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)