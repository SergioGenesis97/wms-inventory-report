def save_file(message: str, file_name: str) -> str:
    with open(rf"C:\Users\Sergio Rosas\Documents\pruebas scripts\Nueva carpeta\Python\Mini-Proyect-2\files\{file_name}", 'w', encoding='utf-8') as f:
        f.write(message)
    
    return f"\n✅ El Reporte: {file_name} generado exitosamente en la carpeta files.\n"
