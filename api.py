from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import keygen
import storage


app = FastAPI(title="Link Shorter API")


class LinkRequest(BaseModel):
    link: str


@app.post("/shorten") # метод POST вызывает функцию вставки пары в БД
def shorten_link(request: LinkRequest):
    new_key = keygen.key_generator()
    success = storage.add_link(new_key, request.link)

    while not success:
        new_key = keygen.key_generator()
        success = storage.add_link(new_key, request.link)
    return {"key": new_key, "short_url": f"http://ваш-сервер/{new_key}"}


@app.get("/find/{value}") # метод GET вызывает функцию поиска ссылки в БД
def find_link(value: str):
    result = storage.find(value)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"result": result}


@app.get("/show") # метод GET вызывает функцию показа всех записей в БД
def show_all():
    return {"links": storage.show()}