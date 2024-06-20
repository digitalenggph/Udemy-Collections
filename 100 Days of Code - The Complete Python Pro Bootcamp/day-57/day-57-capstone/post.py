import requests


class Post:
    def __init__(self):
        self.url = 'https://api.npoint.io/f14658c6e58c834c01e0'

    def get_blog(self):
        blog_data = requests.get(url=self.url)
        blog_data.raise_for_status()
        posts = blog_data.json()
        return posts


