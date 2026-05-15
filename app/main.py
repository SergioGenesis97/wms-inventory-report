from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request

from app.data_handler import read_file
from app.services import make_report


import csv
import io

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html", 
        request=request
    )

@app.get("/inventario")
def obtener_inventario():
    datos = read_file('files/stock.csv')
    return datos

@app.get("/reporte")
def obtener_reporte_detallado():
    datos = read_file('data/stock.csv')
    txt_reporte = make_report(datos)
    return {"reporte_completo": txt_reporte}

@app.post("/upload-inventory")
async def upload_inventoy(file: UploadFile = File(...)):
    contenido = await file.read()
    texto = contenido.decode("utf-8")
    reader = csv.DictReader(io.StringIO(texto))
    inventario = {row['sku']: int(row['cantidad']) for row in reader}
    reporte_final = make_report(inventario)
    return {
        "filename": file.filename,
        "reporte": reporte_final
    }
    