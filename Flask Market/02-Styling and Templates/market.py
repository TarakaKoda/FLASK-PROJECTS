from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return """<h1>Home Page</h1>
    <p>Welcome to our Home Page</p>
    """

@app.route("/about")
def about_page():
    return "<h1>This is our About Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)

