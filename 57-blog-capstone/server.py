from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts]


@app.route("/")
def get_blog():
    return render_template("index.html", posts=post_objects)


@app.route("/post/<int:post_id>")
def get_blog_post(post_id):
    post_data = [post for post in post_objects if post.id == post_id]
    return render_template("post.html", post=post_data[0])


if __name__ == "__main__":
    app.run(debug=True)
