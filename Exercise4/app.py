from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/about")
def about():
    return jsonify(
        name="Simple REST API",
        description="This is a simple REST API built with Flask.",
        version="1.0",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
