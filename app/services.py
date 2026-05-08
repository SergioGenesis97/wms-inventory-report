from app.services import classify_stock

#Clasifica el inventario
def classify_stock(quantity: int) -> str:
    return "Reabastecer" if quantity < 10 else ("Stock Bajo" if quantity <= 50 else "Stock Suficiente")


# Realiza el repore del inventario
def make_report(inventory: dict) -> str:
    report = "\n===== REPORTE DE INVENTARIO =====\n"
    critical = []
    for sku, quantity in inventory.items():
        estado = classify_stock(quantity)
        if estado == 'Reabastecer':
            critical.append(sku)
        report += f"{sku} | {quantity} unidades | {estado}\n"
    report += "================================\n"
    report += f"CRÍTICOS (reabastecer): {', '.join(critical)}\n"

    return report

#Guarda el archivo de forma física
def save_file(message: str, file_name: str) -> str:
    with open(rf"C:\Users\Sergio Rosas\Documents\pruebas scripts\Nueva carpeta\Python\Mini-Proyect-2\files\{file_name}", 'w', encoding='utf-8') as f:
        f.write(message)
    
    return f"\n✅ El Reporte: {file_name} generado exitosamente en la carpeta files.\n"
