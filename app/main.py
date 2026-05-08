from fastapi import FastAPI
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