import unittest
from controlador_peliculas import calculariva  

class TestCalcularIva(unittest.TestCase):
    def test_calcular_iva(self):
        self.assertEqual(calculariva(100), 21)

if __name__ == "__main__":
    unittest.main()

