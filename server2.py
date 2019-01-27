from flask import Flask, render_template, request, jsonify
import Main
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template("homepage.html")
    if request.method == 'POST':
        return kmeans()


def kmeans():
    n_clusters = request.get_json()['n_clusters']
    return render_template(
        'homepage.html', results=Main.run(n_clusters)['centers']
    )


if __name__ == "__main__":
    app.run(port=443)
