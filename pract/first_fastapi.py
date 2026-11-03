from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Подключаем папки со стилями и шаблонами
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# 1. Главная страница: просто показываем HTML
@app.get("/", response_class=HTMLResponse)
def main_page(request: Request):
    return templates.TemplateResponse(request=request, name="main.html")


# 2. Страница с приветствием: имя берём из адреса
@app.get("/hello/{name}", response_class=HTMLResponse)
def hello(request: Request, name: str):
    return templates.TemplateResponse(
        request=request,
        name="hello.html",
        context={"name": name},
    )


# 3. Обычный API: возвращает JSON, а не страницу
@app.get("/api/ping")
def ping():
    return {"message": "pong"}