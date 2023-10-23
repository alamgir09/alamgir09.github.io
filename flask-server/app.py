from flask import Flask, request
app = Flask(__name__)


# Creating home page route
@app.route("/home")
def home():
    return {"Hello" : "This actually works!"}

if __name__ == "__main__":
    app.run(debug=True)