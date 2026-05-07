from inventory import inventario
from make_report import make_report
from make_file import save_file

print(save_file(make_report(inventario), "reporte_wms.txt"))