from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    html_content = """
    <html>
        <style>
        .center {
            text-align: center;
        }   
        </style>
        <body>
            <h1 class="center">Ecommerce application</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)