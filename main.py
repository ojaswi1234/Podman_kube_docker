from Flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return "This is an flask app running in a docker container!"



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)