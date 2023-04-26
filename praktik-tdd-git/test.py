from main import faktorial

import unittest

class TestFaktorial(unittest.TestCase):
    # We will implement the test here
    def test_non_numeric_input(self):
        self.assertEqual(faktorial("1.5"), "Harap masukkan input numerik (0-9)")

    def test_numeric_input(self):
        self.assertEqual(faktorial("4"), "Nilai faktorialnya adalah 24")
    
if __name__ == "__main__":
    unittest.main()