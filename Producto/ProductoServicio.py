from Constantes.Naturaleza import Naturaleza
from Producto.Producto import Producto

class ProductoServicio(Producto):
  def __init__ (self):
    Producto.__init__(self,Naturaleza.SERVICIO)

  def facturar (self):
    return 100.0+Naturaleza.SERVICIO