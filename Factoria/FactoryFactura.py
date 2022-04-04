from Constantes.Naturaleza import Naturaleza
from Producto.ProductoAlimentario import ProductoAlimentario
from Producto.ProductoServicio import ProductoServicio

class FactoryFactura:
  @classmethod
  def crear (cls,producto):
    if producto.naturaleza== Naturaleza.ALIMENTARIA:
      return ProductoAlimentario()
    if producto.naturaleza== Naturaleza.SERVICIO:
      return ProductoServicio()
      