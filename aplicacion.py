from Producto.Producto import Producto
from Constantes.Naturaleza import Naturaleza
from Factoria.FactoryFactura import FactoryFactura

def aplicacion ():
  producto = Producto(Naturaleza.ALIMENTARIA) # IVA 5,5% 
  precio_neto = FactoryFactura.crear(producto).facturar() 
  print(precio_neto) 
  producto = Producto(Naturaleza.SERVICIO) # IVA 20% 
  precio_neto = FactoryFactura.crear(producto).facturar() 
  print(precio_neto) 