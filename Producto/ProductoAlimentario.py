from Constantes.Naturaleza import Naturaleza
from Producto.Producto import Producto

class ProductoAlimentario(Producto):
  def __init__ (self):
    Producto.__init__(self,Naturaleza.ALIMENTARIA)

  def facturar (self):
    return 100.0+Naturaleza.ALIMENTARIA