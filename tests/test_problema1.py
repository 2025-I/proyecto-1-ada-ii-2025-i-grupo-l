import unittest
import test_problema1bruta
import test_problema1dinamica
import test_problema1voraz

# Crear un conjunto de pruebas unificado
def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_problema1bruta))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_problema1dinamica))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_problema1voraz))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())