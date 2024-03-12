from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")

def index():
    return "Puedes explorar /aprender"

@app.get("/aprender", response_class=HTMLResponse)
async def mostrar_aprender():
    html_content = """
    <html>
    <head>

        <title>aprender</title>
    </head>
    <body>
        <h1>APRENDIENDO A USAR FASTAPI</h1>

        <style>
            body {
                font-family: Verdana, Geneva, sans-serif;
                padding: 20px;
                color: red;
            }
           
        </style>
    </body>
    
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)