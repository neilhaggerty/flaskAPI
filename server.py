from flask import Flask, redirect, request, url_for
import json
app = Flask(__name__)

def get_posts_json():
    with open('posts.json') as f:
        posts = json.load(f)
    return posts

def write_json(posts):
    with open('posts.json', 'w') as f:
        f.write(json.dumps(posts))

def find_max_id(posts):
    ids = [post['id'] for post in posts['posts']]
    return max(ids)        

def find_post_by_id(posts, _id):
    for post in posts['posts']:
        if post['id'] == _id:
            return post

@app.route('/')
def list_posts():
    posts = get_posts_json()
    return posts

@app.route('/post', methods=['POST'])
def create_post():
    json_data = request.get_json()
    posts = get_posts_json()
    post_id = find_max_id(posts)+1
    posts['posts'].append({
        'id': post_id,
        'likes': 0,
        **json_data
    })
    write_json(posts)
    return get_posts_json()

@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    posts = get_posts_json()
    post = find_post_by_id(posts, post_id)
    posts['posts'].remove(post)
    write_json(posts)
    return get_posts_json()

@app.route('/like/<int:post_id>', methods=['POST'])
def upvote(post_id):
    posts = get_posts_json()
    post = find_post_by_id(posts, post_id)
    post.update({'likes': post['likes']+1})
    write_json(posts)
    return get_posts_json()

@app.route('/dislike/<int:post_id>', methods=['POST'])
def downvote(post_id):
    posts = get_posts_json()
    post = find_post_by_id(posts, post_id)
    post.update({'likes': post['likes']-1})
    write_json(posts)
    return get_posts_json()
