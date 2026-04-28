from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import datetime
import os

app = FastAPI()

# 1. Визитка в JSON (для тех, кто хочет данные программно)
@app.get("/")
def визитка():
    return {
        "имя": "Вадим",
        "навыки": ["FastAPI", "Python", "Создание API"],
        "контакты": {
            "telegram": "@",
            "email": "ireallifel883@gmail.com"
        }
    }

# 2. HTML-форма для отправки сообщения (для людей в браузере)
@app.get("/form", response_class=HTMLResponse)
def показать_форму():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Обратная связь</title>
    </head>
    <body>
        <h1>Оставьте сообщение</h1>
        <form action="/feedback" method="post">
            <textarea name="message" rows="4" cols="50" placeholder="Ваше сообщение..."></textarea><br><br>
            <button type="submit">Отправить</button>
        </form>
        <p>После отправки вы увидите подтверждение.</p>
    </body>
    </html>
    """

# 3. Приём сообщения и сохранение в файл
@app.post("/feedback")
async def сохранить_сообщение(message: str = Form(...)):
    # Записываем сообщение вместе с текущим временем в файл
    with open("feedback.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

    # Возвращаем ответ (браузер получит JSON, потому что форма отправилась без JavaScript)
    # Но можно добавить HTML-подтверждение или вернуть JSON.
    return {"статус": "получено", "сообщение": message}
