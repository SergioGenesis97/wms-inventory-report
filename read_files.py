import csv
from pathlib import Path


def read_file(path: str) -> dict:

    # Ruta del archivo 
    route_file = Path(path).resolve()

    with open(route_file, encoding='utf-8') as file:
        
        reader = csv.DictReader(file)

        return {row['sku']: int(row['cantidad']) for row in reader}