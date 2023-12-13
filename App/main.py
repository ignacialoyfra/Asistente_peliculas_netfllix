from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Form
from fastapi.staticfiles import StaticFiles
from pathlib import Path

templates = Jinja2Templates(directory="App/templates")


app = FastAPI()

@app.get("/index", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
# Almacenamiento temporal de la selección del usuario
usuario_seleccion = None
@app.post("/tu-endpoint")
async def manejar_seleccion(seleccion: str = Form(...)):
    # Procesar la selección aquí
    # Por ejemplo, simplemente devolvemos la selección en un div
    if seleccion == 4:
        print("AQUIIII:",str(seleccion))
    else:
        None

    return HTMLResponse(content=f"<div>Selección recibida: {seleccion}</div>")
# @app.get("/dropdown-data")
# async def dropdown_data():
#     opciones = [1, 2, 3, 4]
#     opciones_html = "".join(f"<option value='{opcion}'>{opcion}</option>" for opcion in opciones)
#     return HTMLResponse(content=f"<select id='seleccion' name='seleccion'>{opciones_html}</select>")

# @app.post("/submit")
# async def submit(seleccion: str = Form(...)):
#     global seleccion_usuario
#     seleccion_usuario = seleccion 
#     # Aquí puedes procesar la selección del usuario
#     print(seleccion_usuario)
#     return HTMLResponse(content=f"<div>Selección recibida: {seleccion}</div>")
# # @app.post("/submit")
# async def submit(texto: str = Form(...)):
#     return HTMLResponse(content=f"<div>{texto}</div>")

@app.get("/")
def read_root():
    return {"Hello": "World"}


