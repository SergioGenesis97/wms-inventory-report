from inventory import inventario
from make_report import make_report
from make_file import save_file
from read_files import read_file

datos = read_file('files/stock.csv')

print(save_file(make_report(datos), "reporte_wms.txt"))