from classification_inventory import classify_stock

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