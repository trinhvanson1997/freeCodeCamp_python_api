from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def root():
    return "hello"


@app.post("/create_posts")
def create_posts(post: Post):
    return {"aa": post.title, "content": post.content, "published": post.published}

