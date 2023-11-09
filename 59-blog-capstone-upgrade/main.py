from flask import Flask, render_template
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/66b20ef4e6ceda5be835").json()


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:post_id>")
def blog_post(post_id):
    post_data = [post for post in posts if post["id"] == post_id]
    return render_template("post.html", post=post_data[0])


if __name__ == "__main__":
    app.run(debug=True)
