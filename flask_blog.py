from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>feeling alive rn</h1>"
print(hello())


@app.route("/about")
def about():
    return "<h1>the  home page </h1>"
print(about())

if __name__ == '__main__':
    app.run(debug=True) 