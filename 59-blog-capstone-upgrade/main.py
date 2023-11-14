from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
GMAIL_PSW = os.getenv("GMAIL_PSW")
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/66b20ef4e6ceda5be835").json()


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(GMAIL_EMAIL, GMAIL_PSW)
            connection.sendmail(
                from_addr=GMAIL_EMAIL,
                to_addrs=GMAIL_EMAIL,
                msg=f"Subject:Contact form submit:\n\n"
                    f"Name: {data['name']}\n"
                    f"Email: {data['email']}\n"
                    f"Phone: {data['phone']}\n"
                    f"Message: {data['message']}\n"
            )
        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)


@app.route("/post/<int:post_id>")
def blog_post(post_id):
    post_data = [post for post in posts if post["id"] == post_id]
    return render_template("post.html", post=post_data[0])


if __name__ == "__main__":
    app.run(debug=True)
