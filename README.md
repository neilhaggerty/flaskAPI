# flaskAPI

This is a simple API that will create, delete, and list posts in addition to
liking and unliking them.

## Running

`./run.sh`

Builds the Docker image and runs the container so you can interact with the api.

The api is running on port 5000 locally

`GET /` will show the current contents of `posts.json`
`POST /post` will create a new post in `posts.json`. The request should contain the object:
```
{
    "title": "this is a post title"
}
```
`DELETE /post/<id>` will delete the specified post from `posts.json`
`POST /like/<id>` will "like" the specified post. Incrementing the `likes` value in `posts.json` by 1
`POST /dislike/<id>` will "dislike" the specified post. Decrementing the `likes` value in `posts.json` (negatives are allowed)

# Caveats

The json file is note exported from the container so restarting the container
will cause the data to dissapear.

There's no tests or error handling currently.
