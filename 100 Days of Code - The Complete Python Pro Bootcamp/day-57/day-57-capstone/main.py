from flask import Flask, render_template
from post import Post

app = Flask(__name__)

blog_post = Post()
posts = blog_post.get_blog()


@app.route('/blog')
def home():
    return render_template("index.html",
                           posts=posts)


@app.route('/post/<blog_id>')
def get_blog(blog_id):
    print(blog_id)
    return render_template('post.html',
                           posts=posts,
                           blog_id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)
