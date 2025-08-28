##CASOS DE PRUEBA##
## cuando no se tienen elementos, promedio() debe dar como respuesta un elemento nulo o un error
## caudno se tiene un solo elemento, promedio() debe ser el mismo elemento existente en el conjunto
## cuando se tienen dos elementos, promedio() debe ser la suma de los elementos del conjunto dividido entre 2
## cuando se tienen n elementos, promedio() es la suma de los elementos del conjunto dividido el numero de elementos


import unittest
from kataTDDpractica.src.katatddpractica.conjunto import Conjunto


class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_un_elemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(conjunto.promedio(), 5)

    def test_conjunto_dos_elementos(self):
        conjunto = Conjunto([5, 7])
        self.assertEqual(conjunto.promedio(), 6)

    def test_conjunto_n_elementos(self):
        conjunto = Conjunto([2,3,4,7,34,23,3,4])
        self.assertEqual(conjunto.promedio(), (2+3+4+7+34+23+3+4)/8)