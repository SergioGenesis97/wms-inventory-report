def classify_stock(quantity: int) -> str:
    return "Reabastecer" if quantity < 10 else ("Stock Bajo" if quantity <= 50 else "Stock Suficiente")
