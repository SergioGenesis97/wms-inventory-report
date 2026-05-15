from fastapi import FastAPI, UploadFile, File
import csv
import io
from app.data_handler import read_file
from app.services import make_report

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API Funcionando"}

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
    