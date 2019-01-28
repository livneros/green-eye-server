from flask import Flask, render_template, request

import kmeans_pre_processor

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
        'images_section.html', results=kmeans_pre_processor.run(int(n_clusters))
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
