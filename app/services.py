#Clasifica el inventario
def classify_stock(quantity: int) -> str:
    if quantity < 10:
        return "Reabastecer"
    elif quantity <= 50:
        return "Stock Bajo"
    else:
        return "Stock Suficiente"


# Realiza el repore del inventario
def make_report(inventory: dict) -> str:
    reporte = {"resumen": "Reporte completo..."}
    reporte["detalles"] = []
    reporte["conteo"] = {}

    report = "\n===== REPORTE DE INVENTARIO =====\n"
    critical = []
    for sku, quantity in inventory.items():
        estado = classify_stock(quantity)
        if estado == 'Reabastecer':
            critical.append(sku)
        report += f"{sku} | {quantity} unidades | {estado}\n"

        reporte["detalles"].append({"sku":sku, "cantidad":int(quantity), "estado":estado})
        if estado not in reporte["conteo"]:
            reporte["conteo"][estado] = 1
        else:
            reporte["conteo"][estado] += 1

    report += "================================\n"
    report += f"CRÍTICOS (reabastecer): {', '.join(critical)}\n"
    
    print(reporte)
    return report

#Guarda el archivo de forma física
def save_file(message: str, file_name: str) -> str:
    with open(rf"C:\Users\Sergio Rosas\Documents\pruebas scripts\Nueva carpeta\Python\Mini-Proyect-2\files\{file_name}", 'w', encoding='utf-8') as f:
        f.write(message)
    
    return f"\n✅ El Reporte: {file_name} generado exitosamente en la carpeta files.\n"
